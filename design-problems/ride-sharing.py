'''
Designing a Ride-Sharing Service Like Uber

Requirements

- The ride sharing service should allow passengers to request rides and drivers to accept and fulfill those ride requests.
- Passengers should be able to specify their pickup location, destination, and desired ride type (e.g., regular, premium).
- Drivers should be able to see available ride requests and choose to accept or decline them.
- The system should match ride requests with available drivers based on proximity and other factors.
- The system should calculate the fare for each ride based on distance, time, and ride type.
- The system should handle payments and process transactions between passengers and drivers.
- The system should provide real-time tracking of ongoing rides and notify passengers and drivers about ride status updates.
- The system should handle concurrent requests and ensure data consistency.


####################
Entities
####################

RideType
- SEDAN
- SUV
- AUTO

TripStatus
- REQUESTED
- ASSIGNED
- IN_PROGRESS
- COMPLETED
- CANCELLED

DriverStatus
- OFFLINE
- ONLINE
- IN_TRIP


Location
- latitude: float
- longitude: float

+ distance_to(other: Location) -> float


Vehicle
- license_number: str
- model: str
- type: RideType

+ get_license_number() -> str
+ get_model() -> str
+ get_type() -> RideType


TripObserver (abstract)
+ on_update(trip: Trip)


User (implements TripObserver)
- id: str
- name: str
- contact: str
- trip_history: List[Trip]

+ add_trip_to_history(trip: Trip)
+ get_trip_history() -> List[Trip]
+ get_id() -> str
+ get_name() -> str
+ get_contact() -> str


Rider extends User

+ on_update(trip: Trip)

Driver extends User
- vehicle: Vehicle
- current_location: Location
- status: DriverStatus

+ get_vehicle() -> Vehicle
+ get_status() -> DriverStatus
+ set_status(status: DriverStatus)
+ get_current_location() -> Location
+ set_current_location(location: Location)
+ on_update(trip: Trip)


PricingStrategy (abstract)
+ calculate_fare(pickup: Location, dropoff: Location, ride_type: RideType) -> float
+ FlatRatePricingStrategy
+ VehicleBasedPricingStrategy


DriverMatchingStrategy (abstract)
+ find_drivers(drivers, pickup_location, ride_type) -> List[Driver]
+ NearestDriverMatchingStrategy


TripState (abstract)
+ request(trip)
+ assign(trip, driver)
+ start(trip)
+ end(trip)

    RequestedState
    AssignedState
    InProgressState
    CompletedState


Trip
- id: str
- rider: Rider
- driver: Optional[Driver]
- pickup_location: Location
- dropoff_location: Location
- fare: float
- status: TripStatus
- current_state: TripState
- observers: List[TripObserver]

+ assign_driver(driver: Driver)
+ start_trip()
+ end_trip()

+ add_observer(observer: TripObserver)
+ notify_observers()

+ get_id()
+ get_rider()
+ get_driver()
+ get_status()


TripBuilder
- id
- rider
- pickup_location
- dropoff_location
- fare

+ with_rider()
+ with_pickup_location()
+ with_dropoff_location()
+ with_fare()
+ build() -> Trip


RideSharingService (Singleton)
- riders: Dict[str, Rider]
- drivers: Dict[str, Driver]
- trips: Dict[str, Trip]
- pricing_strategy: PricingStrategy
- driver_matching_strategy: DriverMatchingStrategy

+ register_rider(name, contact) -> Rider
+ register_driver(name, contact, vehicle, location) -> Driver

+ request_ride(rider_id, pickup, dropoff, ride_type) -> Trip
+ accept_ride(driver_id, trip_id)
+ start_trip(trip_id)
+ end_trip(trip_id)

+ set_pricing_strategy(strategy)
+ set_driver_matching_strategy(strategy)
--------------------------------------------------------------------------------
'''


import math
import uuid
import threading
from enum import Enum
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, Optional, List, Dict


class RideType(Enum):
    SEDAN = "SEDAN"
    SUV = "SUV"
    AUTO = "AUTO"


class TripStatus(Enum):
    REQUESTED = "REQUESTED"
    ASSIGNED = "ASSIGNED"
    IN_PROGRESS = "IN_PROGRESS"
    COMPLETED = "COMPLETED"
    CANCELLED = "CANCELLED"


class DriverStatus(Enum):
    OFFLINE = "OFFLINE"
    ONLINE = "ONLINE"
    IN_TRIP = "IN_TRIP"


class Vehicle:
    def __init__(self, license_number: str, model: str, vehicle_type: RideType):
        self._license_number = license_number
        self._model = model
        self._type = vehicle_type
    
    def get_license_number(self) -> str:
        return self._license_number
    
    def get_model(self) -> str:
        return self._model
    
    def get_type(self) -> RideType:
        return self._type


class TripObserver(ABC):
    @abstractmethod
    def on_update(self, trip: 'Trip'):
        pass


class User(TripObserver):
    def __init__(self, name: str, contact: str):
        self._id = str(uuid.uuid4())
        self._name = name
        self._contact = contact
        self._trip_history: List['Trip'] = []
    
    def add_trip_to_history(self, trip: 'Trip'):
        self._trip_history.append(trip)
    
    def get_trip_history(self) -> List['Trip']:
        return self._trip_history
    
    def get_id(self) -> str:
        return self._id
    
    def get_name(self) -> str:
        return self._name
    
    def get_contact(self) -> str:
        return self._contact


class Location:
    def __init__(self, latitude: float, longitude: float):
        self._latitude = latitude
        self._longitude = longitude
    
    def distance_to(self, other: 'Location') -> float:
        dx = self._latitude - other._latitude
        dy = self._longitude - other._longitude
        return math.sqrt(dx * dx + dy * dy)  # Euclidean for simplicity
    
    def __str__(self) -> str:
        return f"Location({self._latitude}, {self._longitude})"


class PricingStrategy(ABC):
    @abstractmethod
    def calculate_fare(self, pickup: Location, dropoff: Location, ride_type: RideType) -> float:
        pass

class FlatRatePricingStrategy(PricingStrategy):
    BASE_FARE = 5.0
    FLAT_RATE = 1.5
    
    def calculate_fare(self, pickup: Location, dropoff: Location, ride_type: RideType) -> float:
        distance = pickup.distance_to(dropoff)
        return self.BASE_FARE + distance * self.FLAT_RATE

class VehicleBasedPricingStrategy(PricingStrategy):
    BASE_FARE = 2.50
    RATE_PER_KM = {
        RideType.SEDAN: 1.50,
        RideType.SUV: 2.00,
        RideType.AUTO: 1.00
    }
    
    def calculate_fare(self, pickup: Location, dropoff: Location, ride_type: RideType) -> float:
        return self.BASE_FARE + self.RATE_PER_KM[ride_type] * pickup.distance_to(dropoff)


class Driver(User):
    def __init__(self, name: str, contact: str, vehicle: Vehicle, initial_location: Location):
        super().__init__(name, contact)
        self._vehicle = vehicle
        self._current_location = initial_location
        self._status = DriverStatus.OFFLINE  # Default status
    
    def get_vehicle(self) -> Vehicle:
        return self._vehicle
    
    def get_status(self) -> DriverStatus:
        return self._status
    
    def set_status(self, status: DriverStatus):
        self._status = status
        print(f"Driver {self.get_name()} is now {status.value}")
    
    def get_current_location(self) -> Location:
        return self._current_location
    
    def set_current_location(self, current_location: Location):
        self._current_location = current_location
    
    def on_update(self, trip: 'Trip'):
        print(f"--- Notification for Driver {self.get_name()} ---")
        print(f"  Trip {trip.get_id()} status: {trip.get_status().value}.")
        if trip.get_status() == TripStatus.REQUESTED:
            print("  A new ride is available for you to accept.")
        print("--------------------------------\n")


class DriverMatchingStrategy(ABC):
    @abstractmethod
    def find_drivers(self, all_drivers: List[Driver], pickup_location: Location, ride_type: RideType) -> List[Driver]:
        pass

class NearestDriverMatchingStrategy(DriverMatchingStrategy):
    MAX_DISTANCE_KM = 5.0  # Max distance to consider a driver "nearby"
    
    def find_drivers(self, all_drivers: List[Driver], pickup_location: Location, ride_type: RideType) -> List[Driver]:
        print(f"Finding nearest drivers for ride type: {ride_type.value}")
        available_drivers = [
            driver for driver in all_drivers
            if (driver.get_status() == DriverStatus.ONLINE and
                driver.get_vehicle().get_type() == ride_type and
                pickup_location.distance_to(driver.get_current_location()) <= self.MAX_DISTANCE_KM)
        ]
        
        # Sort by distance
        available_drivers.sort(key=lambda d: pickup_location.distance_to(d.get_current_location()))
        return available_drivers
 

class Rider(User):
    def __init__(self, name: str, contact: str):
        super().__init__(name, contact)
    
    def on_update(self, trip: 'Trip'):
        print(f"--- Notification for Rider {self.get_name()} ---")
        print(f"  Trip {trip.get_id()} is now {trip.get_status().value}.")
        if trip.get_driver() is not None:
            print(f"  Driver: {trip.get_driver().get_name()} in a {trip.get_driver().get_vehicle().get_model()} "
                  f"({trip.get_driver().get_vehicle().get_license_number()})")
        print("--------------------------------\n")


class TripState(ABC):
    @abstractmethod
    def request(self, trip: 'Trip'):
        pass
    
    @abstractmethod
    def assign(self, trip: 'Trip', driver: 'Driver'):
        pass
    
    @abstractmethod
    def start(self, trip: 'Trip'):
        pass
    
    @abstractmethod
    def end(self, trip: 'Trip'):
        pass


class RequestedState(TripState):
    def request(self, trip: 'Trip'):
        print("Trip is already in requested state.")
    
    def assign(self, trip: 'Trip', driver: 'Driver'):
        trip.set_driver(driver)
        trip.set_status(TripStatus.ASSIGNED)
        trip.set_state(AssignedState())
    
    def start(self, trip: 'Trip'):
        print("Cannot start a trip that has not been assigned a driver.")
    
    def end(self, trip: 'Trip'):
        print("Cannot end a trip that has not been assigned a driver.")

class AssignedState(TripState):
    def request(self, trip: 'Trip'):
        print("Trip has already been requested and assigned.")
    
    def assign(self, trip: 'Trip', driver: 'Driver'):
        print("Trip is already assigned. To re-assign, cancel first.")
    
    def start(self, trip: 'Trip'):
        trip.set_status(TripStatus.IN_PROGRESS)
        trip.set_state(InProgressState())
    
    def end(self, trip: 'Trip'):
        print("Cannot end a trip that has not started.")


class InProgressState(TripState):
    def request(self, trip: 'Trip'):
        print("Trip is already in progress.")
    
    def assign(self, trip: 'Trip', driver: 'Driver'):
        print("Cannot assign a new driver while trip is in progress.")
    
    def start(self, trip: 'Trip'):
        print("Trip is already in progress.")
    
    def end(self, trip: 'Trip'):
        trip.set_status(TripStatus.COMPLETED)
        trip.set_state(CompletedState())


class CompletedState(TripState):
    def request(self, trip: 'Trip'):
        print("Cannot request a trip that is already completed.")
    
    def assign(self, trip: 'Trip', driver: 'Driver'):
        print("Cannot assign a driver to a completed trip.")
    
    def start(self, trip: 'Trip'):
        print("Cannot start a completed trip.")
    
    def end(self, trip: 'Trip'):
        print("Trip is already completed.")

class Trip:
    def __init__(self, builder: 'TripBuilder'):
        self._id = builder._id
        self._rider = builder._rider
        self._driver: Optional['Driver'] = None
        self._pickup_location = builder._pickup_location
        self._dropoff_location = builder._dropoff_location
        self._fare = builder._fare
        self._status = TripStatus.REQUESTED
        self._current_state = RequestedState()  # Initial state
        self._observers: List[TripObserver] = []
    
    def add_observer(self, observer: TripObserver):
        self._observers.append(observer)
    
    def _notify_observers(self):
        for observer in self._observers:
            observer.on_update(self)
    
    def assign_driver(self, driver: 'Driver'):
        self._current_state.assign(self, driver)
        self.add_observer(driver)
        self._notify_observers()
    
    def start_trip(self):
        self._current_state.start(self)
        self._notify_observers()
    
    def end_trip(self):
        self._current_state.end(self)
        self._notify_observers()
    
    # Getters
    def get_id(self) -> str:
        return self._id
    
    def get_rider(self) -> Rider:
        return self._rider
    
    def get_driver(self) -> Optional['Driver']:
        return self._driver
    
    def get_pickup_location(self) -> Location:
        return self._pickup_location
    
    def get_dropoff_location(self) -> Location:
        return self._dropoff_location
    
    def get_fare(self) -> float:
        return self._fare
    
    def get_status(self) -> TripStatus:
        return self._status
    
    # Setters are protected, only to be called by State objects
    def set_state(self, state: TripState):
        self._current_state = state
    
    def set_status(self, status: TripStatus):
        self._status = status
    
    def set_driver(self, driver: 'Driver'):
        self._driver = driver
    
    def __str__(self) -> str:
        return f"Trip [id={self._id}, status={self._status.value}, fare=${self._fare:.2f}]"
    
    # Builder Pattern
    class TripBuilder:
        def __init__(self):
            self._id = str(uuid.uuid4())
            self._rider: Optional[Rider] = None
            self._pickup_location: Optional[Location] = None
            self._dropoff_location: Optional[Location] = None
            self._fare = 0.0
        
        def with_rider(self, rider: Rider) -> 'Trip.TripBuilder':
            self._rider = rider
            return self
        
        def with_pickup_location(self, pickup_location: Location) -> 'Trip.TripBuilder':
            self._pickup_location = pickup_location
            return self
        
        def with_dropoff_location(self, dropoff_location: Location) -> 'Trip.TripBuilder':
            self._dropoff_location = dropoff_location
            return self
        
        def with_fare(self, fare: float) -> 'Trip.TripBuilder':
            self._fare = fare
            return self
        
        def build(self) -> 'Trip':
            # Basic validation
            if self._rider is None or self._pickup_location is None or self._dropoff_location is None:
                raise ValueError("Rider, pickup, and dropoff locations are required to build a trip.")
            return Trip(self)


class RideSharingService:
    _instance = None
    _lock = threading.Lock()
    
    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
                    cls._instance._initialized = False
        return cls._instance
    
    def __init__(self):
        if not self._initialized:
            self._riders: Dict[str, Rider] = {}
            self._drivers: Dict[str, Driver] = {}
            self._trips: Dict[str, Trip] = {}
            self._pricing_strategy: Optional[PricingStrategy] = None
            self._driver_matching_strategy: Optional[DriverMatchingStrategy] = None
            self._initialized = True
    
    @classmethod
    def get_instance(cls):
        return cls()
    
    # Allow changing strategies at runtime for extensibility
    def set_pricing_strategy(self, pricing_strategy: PricingStrategy):
        self._pricing_strategy = pricing_strategy
    
    def set_driver_matching_strategy(self, driver_matching_strategy: DriverMatchingStrategy):
        self._driver_matching_strategy = driver_matching_strategy
    
    def register_rider(self, name: str, contact: str) -> Rider:
        rider = Rider(name, contact)
        self._riders[rider.get_id()] = rider
        return rider
    
    def register_driver(self, name: str, contact: str, vehicle: Vehicle, initial_location: Location) -> Driver:
        driver = Driver(name, contact, vehicle, initial_location)
        self._drivers[driver.get_id()] = driver
        return driver
    
    def request_ride(self, rider_id: str, pickup: Location, dropoff: Location, ride_type: RideType) -> Optional[Trip]:
        rider = self._riders.get(rider_id)
        if rider is None:
            raise KeyError("Rider not found")
        
        print(f"\n--- New Ride Request from {rider.get_name()} ---")
        
        # 1. Find available drivers
        available_drivers = self._driver_matching_strategy.find_drivers(
            list(self._drivers.values()), pickup, ride_type
        )
        
        if not available_drivers:
            print("No drivers available for your request. Please try again later.")
            return None
        
        print(f"Found {len(available_drivers)} available driver(s).")
        
        # 2. Calculate fare
        fare = self._pricing_strategy.calculate_fare(pickup, dropoff, ride_type)
        print(f"Estimated fare: ${fare:.2f}")
        
        # 3. Create a trip using the Builder
        trip = Trip.TripBuilder() \
            .with_rider(rider) \
            .with_pickup_location(pickup) \
            .with_dropoff_location(dropoff) \
            .with_fare(fare) \
            .build()
        
        self._trips[trip.get_id()] = trip
        
        # 4. Notify nearby drivers (in a real system, this would be a push notification)
        print("Notifying nearby drivers of the new ride request...")
        for driver in available_drivers:
            print(f" > Notifying {driver.get_name()} at {driver.get_current_location()}")
            driver.on_update(trip)
        
        return trip
    
    def accept_ride(self, driver_id: str, trip_id: str):
        driver = self._drivers.get(driver_id)
        trip = self._trips.get(trip_id)
        if driver is None or trip is None:
            raise KeyError("Driver or Trip not found")
        
        print(f"\n--- Driver {driver.get_name()} accepted the ride ---")
        
        driver.set_status(DriverStatus.IN_TRIP)
        trip.assign_driver(driver)
    
    def start_trip(self, trip_id: str):
        trip = self._trips.get(trip_id)
        if trip is None:
            raise KeyError("Trip not found")
        print(f"\n--- Trip {trip.get_id()} is starting ---")
        trip.start_trip()
    
    def end_trip(self, trip_id: str):
        trip = self._trips.get(trip_id)
        if trip is None:
            raise KeyError("Trip not found")
        print(f"\n--- Trip {trip.get_id()} is ending ---")
        trip.end_trip()
        
        # Update statuses and history
        driver = trip.get_driver()
        driver.set_status(DriverStatus.ONLINE)  # Driver is available again
        driver.set_current_location(trip.get_dropoff_location())  # Update driver location
        
        rider = trip.get_rider()
        driver.add_trip_to_history(trip)
        rider.add_trip_to_history(trip)
        
        print(f"Driver {driver.get_name()} is now back online at {driver.get_current_location()}")


class RideSharingServiceDemo:
    @staticmethod
    def main():
        # 1. Setup the system using singleton instance
        service = RideSharingService.get_instance()
        service.set_driver_matching_strategy(NearestDriverMatchingStrategy())
        service.set_pricing_strategy(VehicleBasedPricingStrategy())
        
        # 2. Register riders and drivers
        alice = service.register_rider("Alice", "123-456-7890")
        
        bob = service.register_driver("Bob",
                                    "243-987-2860",
                                    Vehicle("KA01-1234", "Toyota Prius", RideType.SEDAN),
                                    Location(1.0, 1.0))
        
        charlie = service.register_driver("Charlie",
                                        "313-486-2691",
                                        Vehicle("KA02-5678", "Honda CRV", RideType.SUV),
                                        Location(2.0, 2.0))
        
        david = service.register_driver("David",
                                      "613-586-3241",
                                      Vehicle("KA03-9012", "Honda CRV", RideType.SEDAN),
                                      Location(1.2, 1.2))
        
        # 3. Drivers go online
        bob.set_status(DriverStatus.ONLINE)
        charlie.set_status(DriverStatus.ONLINE)
        david.set_status(DriverStatus.ONLINE)
        
        # David is online but will be too far for the first request
        david.set_current_location(Location(10.0, 10.0))
        
        # 4. Alice requests a ride
        pickup_location = Location(0.0, 0.0)
        dropoff_location = Location(5.0, 5.0)
        
        # Rider wants a SEDAN
        trip1 = service.request_ride(alice.get_id(), pickup_location, dropoff_location, RideType.SEDAN)
        
        if trip1 is not None:
            # 5. One of the nearby drivers accepts the ride
            # In this case, Bob (1.0, 1.0) is closer than David (10.0, 10.0 is too far).
            # Charlie is ignored because he drives an SUV.
            service.accept_ride(bob.get_id(), trip1.get_id())
            
            # 6. The trip progresses
            service.start_trip(trip1.get_id())
            service.end_trip(trip1.get_id())
        
        print("\n--- Checking Trip History ---")
        print(f"Alice's trip history: {alice.get_trip_history()}")
        print(f"Bob's trip history: {bob.get_trip_history()}")
        
        # --- Second ride request ---
        print("\n=============================================")
        harry = service.register_rider("Harry", "167-342-7834")
        
        # Harry requests an SUV
        trip2 = service.request_ride(harry.get_id(),
                                    Location(2.5, 2.5),
                                    Location(8.0, 8.0),
                                    RideType.SUV)
        
        if trip2 is not None:
            # Only Charlie is available for an SUV ride
            service.accept_ride(charlie.get_id(), trip2.get_id())
            service.start_trip(trip2.get_id())
            service.end_trip(trip2.get_id())

if __name__ == "__main__":
    RideSharingServiceDemo.main()