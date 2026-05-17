'''
Design a Ride-Sharing Service Like Uber

Requirements

- The ride sharing service should allow passengers to request rides and drivers to accept and fulfill those ride requests.
- Passengers should be able to specify their pickup location, destination, and desired ride type (e.g., regular, premium).
- Drivers should be able to see available ride requests and choose to accept or decline them.
- The system should match ride requests with available drivers based on proximity and other factors.
- The system should calculate the fare for each ride based on distance, time, and ride type.
- The system should handle payments and process transactions between passengers and drivers.
- The system should provide real-time tracking of ongoing rides and notify passengers and drivers about ride status updates.
- The system should handle concurrent requests and ensure data consistency.

--------------------------------------------------------------------------------
'''

from enum import Enum
from threading import Lock
from abc import ABC, abstractmethod


class TripStatus(Enum):
    REQUESTED = 1
    ASSIGNED = 2
    STARTED = 3
    COMPLETED = 4


class RideType(Enum):
    SEDAN = 1
    SUV = 2


class Location:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_to(self, other):
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5


class Rider:

    def __init__(self, name):
        self.name = name


class Driver:

    def __init__(self, name, location, ride_type):

        self.name = name
        self.location = location
        self.ride_type = ride_type
        self.available = True


class Trip:

    def __init__(
        self,
        rider,
        driver,
        pickup,
        drop,
        fare
    ):

        self.rider = rider
        self.driver = driver
        self.pickup = pickup
        self.drop = drop
        self.fare = fare
        self.status = TripStatus.REQUESTED


# STRATEGY PATTERN

class PricingStrategy(ABC):

    @abstractmethod
    def calculate(self, distance):
        pass


class DefaultPricing(PricingStrategy):

    def calculate(self, distance):
        return distance * 10


class DriverMatchingStrategy(ABC):

    @abstractmethod
    def match_driver(self, drivers, ride_type):
        pass


class NearestDriverMatching(DriverMatchingStrategy):

    def match_driver(self, drivers, ride_type):

        for driver in drivers:

            if driver.available and driver.ride_type == ride_type:
                return driver

        return None


class RideService:

    def __init__(self):

        self.lock = Lock()

        self.drivers = []
        self.trips = []

        self.pricing = DefaultPricing()
        self.matcher = NearestDriverMatching()

    def request_ride(
        self,
        rider,
        pickup,
        drop,
        ride_type
    ):

        with self.lock:

            driver = self.matcher.match_driver(
                self.drivers,
                ride_type
            )

            if not driver:
                print("No driver available")
                return

            distance = 10
            fare = self.pricing.calculate(distance)

            trip = Trip(
                rider,
                driver,
                pickup,
                drop,
                fare
            )

            driver.available = False

            self.trips.append(trip)

            return trip

    def complete_trip(self, trip):

        with self.lock:

            trip.status = TripStatus.COMPLETED
            trip.driver.available = True