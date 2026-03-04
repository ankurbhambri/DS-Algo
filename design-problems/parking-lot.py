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

from datetime import datetime
from typing import List, Dict

from enum import Enum, auto
from abc import ABC, abstractmethod

# Note: ABC/abstractmethod still used by PaymentStrategy


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
# Parking Spot
# -------------------------
class ParkingSpot:
    def __init__(self, spot_id: int, spot_type: ParkingSpotType, floor_id: int = None):
        self.spot_id = spot_id
        self.spot_type = spot_type
        self.floor_id = floor_id
        self.is_available = True
        self.vehicle = None

    def park_vehicle(self, vehicle: Vehicle):
        self.vehicle = vehicle
        self.is_available = False

    def free_spot(self):
        self.vehicle = None
        self.is_available = True


# -------------------------
# Entry / Exit Points
# -------------------------
class EntryPoint:
    def __init__(self, entry_id: int, lot: 'ParkingLot'):
        self.entry_id = entry_id
        self.lot = lot

    def get_ticket(self, vehicle: Vehicle) -> 'Ticket':
        return self.lot.park_vehicle(vehicle)


class ExitPoint:
    def __init__(self, exit_id: int, lot: 'ParkingLot'):
        self.exit_id = exit_id
        self.lot = lot

    def process_exit(self, ticket_id: int, payment_type: PaymentType) -> 'PaymentInfo':
        return self.lot.exit_vehicle(ticket_id, payment_type)


# -------------------------
# Display Board
# -------------------------
class DisplayBoard:
    def __init__(self, floor_id: int):
        self.floor_id = floor_id
        self.free_spots: Dict[ParkingSpotType, int] = {}

    def update_free_spots(self, spot_type: ParkingSpotType, count: int):
        self.free_spots[spot_type] = count

    def show(self):
        print(f"Floor {self.floor_id} - Spot availability: {self.free_spots}")


# -------------------------
# Parking Floor
# -------------------------
class ParkingFloor:

    VEHICLE_SPOT_MAP: Dict[VehicleType, List[ParkingSpotType]] = {
        VehicleType.BIKE: [ParkingSpotType.MOTORCYCLE],
        VehicleType.CAR: [ParkingSpotType.COMPACT, ParkingSpotType.HANDICAPPED],
        VehicleType.TRUCK: [ParkingSpotType.LARGE],
    }

    def __init__(self, floor_id: int):
        self.floor_id = floor_id
        self.spots: Dict[ParkingSpotType, List[ParkingSpot]] = {}
        self.display_board = DisplayBoard(floor_id)

    def add_spot(self, spot: ParkingSpot):
        spot.floor_id = self.floor_id
        self.spots.setdefault(spot.spot_type, []).append(spot)
        self._update_display_board()

    def _update_display_board(self):
        for spot_type, spots in self.spots.items():
            free_count = sum(1 for s in spots if s.is_available)
            self.display_board.update_free_spots(spot_type, free_count)

    def find_available_spot(self, vehicle: Vehicle):
        allowed_types = self.VEHICLE_SPOT_MAP.get(vehicle.vehicle_type, [])
        for spot_type, spots in self.spots.items():
            if spot_type not in allowed_types:
                continue
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


# -------------------------
# Per-Hour Rate Model
# -------------------------
HOURLY_RATES: Dict[VehicleType, float] = {
    VehicleType.BIKE: 10.0,
    VehicleType.CAR: 20.0,
    VehicleType.TRUCK: 30.0,
}


def calculate_fee(ticket: Ticket) -> float:
    if ticket.end_time is None:
        ticket.end_time = datetime.now()
    duration = (ticket.end_time - ticket.start_time).total_seconds() / 3600
    hours = max(1, round(duration))  # minimum 1 hour charge
    rate = HOURLY_RATES.get(ticket.vehicle.vehicle_type, 20.0)
    return hours * rate


class CashPayment(PaymentStrategy):
    def pay(self, ticket: Ticket) -> PaymentInfo:
        amount = calculate_fee(ticket)
        ticket.amount = amount
        ticket.status = PaymentStatus.COMPLETED
        return PaymentInfo(amount=amount, status=ticket.status)


class CardPayment(PaymentStrategy):
    def pay(self, ticket: Ticket) -> PaymentInfo:
        amount = calculate_fee(ticket)
        ticket.amount = amount
        ticket.status = PaymentStatus.COMPLETED
        return PaymentInfo(amount=amount, status=ticket.status)


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
        self.entry_points: List[EntryPoint] = []
        self.exit_points: List[ExitPoint] = []
        self.tickets: Dict[int, Ticket] = {}
        self._ticket_counter = 0

    def add_floor(self, floor: ParkingFloor):
        self.floors.append(floor)

    def add_entry_point(self, entry_id: int) -> EntryPoint:
        entry = EntryPoint(entry_id, self)
        self.entry_points.append(entry)
        return entry

    def add_exit_point(self, exit_id: int) -> ExitPoint:
        exit_point = ExitPoint(exit_id, self)
        self.exit_points.append(exit_point)
        return exit_point

    def show_availability(self):
        for floor in self.floors:
            floor.display_board.show()

    def is_spot_available(self, vehicle: Vehicle) -> bool:
        return any(floor.find_available_spot(vehicle) for floor in self.floors)

    def park_vehicle(self, vehicle: Vehicle):
        for floor in self.floors:
            spot = floor.find_available_spot(vehicle)
            if spot:
                spot.park_vehicle(vehicle)
                floor._update_display_board()
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

        # Free the spot and update display board
        ticket.spot.free_spot()
        for floor in self.floors:
            for spots in floor.spots.values():
                if ticket.spot in spots:
                    floor._update_display_board()
                    break

        if payment_type == PaymentType.CASH:
            pay_strategy = CashPayment()
        else:
            pay_strategy = CardPayment()

        payment = pay_strategy.pay(ticket)
        del self.tickets[ticket_id]
        return payment