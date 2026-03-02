'''
Our parking lot will have multiple floors and allow only 2 and 4-wheeler vehicles to be parked.
On each floor, parking spots of either type 2 or 4 will be arranged in rows and columns.

It will support the following features:

- The parking lot should support multiple floors, parking spot types, and vehicle types.
- There should be multiple entry and exit points.
- Customers can pay via cash or card.
- The parking system should show spot availability on display boards at the entrance.
- The system should have a per-hour fee model based on the vehicle type.
- Admins can add parking floors, spots, and display boards.

'''

from abc import ABC, abstractmethod
from enum import Enum, auto
from datetime import datetime
from typing import List, Dict


# -------------------------
# Enum Types
# -------------------------
class ParkingSpotType(Enum):
    COMPACT = auto()
    LARGE = auto()
    HANDICAPPED = auto()
    MOTORCYCLE = auto()


class VehicleType(Enum):
    CAR = auto()
    BIKE = auto()
    TRUCK = auto()


class PaymentStatus(Enum):
    UNPAID = auto()
    COMPLETED = auto()
    CANCELLED = auto()


class PaymentType(Enum):
    CASH = auto()
    CARD = auto()


# -------------------------
# Vehicle Class
# -------------------------
class Vehicle:
    def __init__(self, license_number: str, vehicle_type: VehicleType):
        self.license_number = license_number
        self.vehicle_type = vehicle_type


# -------------------------
# Parking Spot Classes
# -------------------------
class ParkingSpot(ABC):
    def __init__(self, spot_id: int):
        self.spot_id = spot_id
        self.is_available = True
        self.vehicle = None

    def park_vehicle(self, vehicle: Vehicle):
        self.vehicle = vehicle
        self.is_available = False

    def free_spot(self):
        self.vehicle = None
        self.is_available = True

    @abstractmethod
    def get_spot_type(self) -> ParkingSpotType:
        pass


class LargeSpot(ParkingSpot):
    def get_spot_type(self):
        return ParkingSpotType.LARGE


class HandicappedSpot(ParkingSpot):
    def get_spot_type(self):
        return ParkingSpotType.HANDICAPPED


class MotorcycleSpot(ParkingSpot):
    def get_spot_type(self):
        return ParkingSpotType.MOTORCYCLE


# -------------------------
# Display Board
# -------------------------
class DisplayBoard:
    def __init__(self):
        self.free_spots: Dict[ParkingSpotType, int] = {}

    def update_free_spots(self, spot_type: ParkingSpotType, count: int):
        self.free_spots[spot_type] = count
        self.show()

    def show(self):
        print("Spot availability:", self.free_spots)


# -------------------------
# Parking Floor
# -------------------------
class ParkingFloor:
    def __init__(self, floor_id: int):
        self.floor_id = floor_id
        self.spots: Dict[ParkingSpotType, List[ParkingSpot]] = {}
        self.display_board = DisplayBoard()

    def add_spot(self, spot: ParkingSpot):
        self.spots.setdefault(spot.get_spot_type(), []).append(spot)

    def find_available_spot(self, vehicle: Vehicle):
        for spot_type, spots in self.spots.items():
            for s in spots:
                if s.is_available:
                    return s
        return None


# -------------------------
# Ticket & Payment
# -------------------------
class Ticket:
    def __init__(self, ticket_id: int, spot: ParkingSpot, vehicle: Vehicle):
        self.ticket_id = ticket_id
        self.spot = spot
        self.vehicle = vehicle
        self.start_time = datetime.now()
        self.end_time = None
        self.amount = 0
        self.status = PaymentStatus.UNPAID


class PaymentInfo:
    def __init__(self, amount: float, status: PaymentStatus):
        self.amount = amount
        self.status = status


class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, ticket: Ticket) -> PaymentInfo:
        pass


class CashPayment(PaymentStrategy):
    def pay(self, ticket: Ticket) -> PaymentInfo:
        ticket.status = PaymentStatus.COMPLETED
        return PaymentInfo(amount=50.0, status=ticket.status)


class CardPayment(PaymentStrategy):
    def pay(self, ticket: Ticket) -> PaymentInfo:
        ticket.status = PaymentStatus.COMPLETED
        return PaymentInfo(amount=50.0, status=ticket.status)


# -------------------------
# Parking Attendant/Admin
# -------------------------
class ParkingAttendant:
    def create_ticket(self, vehicle: Vehicle, spot: ParkingSpot, ticket_id: int):
        return Ticket(ticket_id, spot, vehicle)


class Admin:
    def add_floor(self, lot, floor: ParkingFloor):
        lot.add_floor(floor)


# -------------------------
# Parking Lot
# -------------------------
class ParkingLot:
    def __init__(self):
        self.floors: List[ParkingFloor] = []
        self.tickets: Dict[int, Ticket] = {}
        self._ticket_counter = 0

    def add_floor(self, floor: ParkingFloor):
        self.floors.append(floor)

    def is_spot_available(self):
        return any(floor.find_available_spot for floor in self.floors)

    def park_vehicle(self, vehicle: Vehicle):
        for floor in self.floors:
            spot = floor.find_available_spot(vehicle)
            if spot:
                spot.park_vehicle(vehicle)
                self._ticket_counter += 1
                ticket = Ticket(self._ticket_counter, spot, vehicle)
                self.tickets[self._ticket_counter] = ticket
                return ticket
        raise Exception("Parking full")

    def exit_vehicle(self, ticket_id: int, payment_type: PaymentType):
        ticket = self.tickets.get(ticket_id)
        if not ticket:
            raise Exception("Invalid ticket")

        ticket.end_time = datetime.now()
        if payment_type == PaymentType.CASH:
            pay_strategy = CashPayment()
        else:
            pay_strategy = CardPayment()

        return pay_strategy.pay(ticket)