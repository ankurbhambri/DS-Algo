'''
Design Elevator System For A Multi-Storey Building

Requirements:

- The elevator can have three states: Stationary, Moving, and Out of Order.

- The elevator can be moving in two directions: Up, and Down.

- The elevator door can only open when the elevator is stationary.

- The elevator will have two types of controls:
    - External control, which is available on the floors for summoning the elevator by pressing the up or down button, depending on which direction the user wants to go in.
    - Internal control, which allows the user to choose the floor that they want to go to.

- An algorithm to decide which direction the elevator should move in, if more than one passenger summons the elevator.

'''

from enum import Enum
from abc import ABC, abstractmethod
from typing import List, Set, Optional
from collections import defaultdict


# ======================== Enums ========================

class ElevatorState(Enum):
    STATIONARY = "STATIONARY"
    MOVING = "MOVING"
    OUT_OF_ORDER = "OUT_OF_ORDER"


class Direction(Enum):
    UP = "UP"
    DOWN = "DOWN"
    IDLE = "IDLE"


class DoorState(Enum):
    OPEN = "OPEN"
    CLOSED = "CLOSED"


# ======================== Request Models (ISP) ========================

class ExternalRequest:
    """Floor-level button press (up or down)."""
    def __init__(self, floor: int, direction: Direction):
        self.floor = floor
        self.direction = direction

    def __repr__(self):
        return f"External(floor={self.floor}, dir={self.direction.value})"


class InternalRequest:
    """Inside-cabin button press (destination floor)."""
    def __init__(self, floor: int):
        self.floor = floor

    def __repr__(self):
        return f"Internal(floor={self.floor})"


# ======================== Scheduling Strategy (OCP + DIP) ========================

class SchedulingStrategy(ABC):
    """Open/Closed: add new algorithms by subclassing, zero changes to Elevator."""
    @abstractmethod
    def next_floor(self, current_floor: int, direction: Direction,
                   up_stops: Set[int], down_stops: Set[int]) -> Optional[int]:
        """Return the next floor to visit, or None if no pending stops."""
        pass

    @abstractmethod
    def next_direction(self, current_floor: int, direction: Direction,
                       up_stops: Set[int], down_stops: Set[int]) -> Direction:
        """Return the direction after servicing a stop."""
        pass


class SCANStrategy(SchedulingStrategy):
    """Classic elevator SCAN (a.k.a. elevator algorithm):
       Keep going in current direction, service all stops, then reverse."""

    def next_floor(self, current_floor: int, direction: Direction,
                   up_stops: Set[int], down_stops: Set[int]) -> Optional[int]:
        all_stops = up_stops | down_stops
        if not all_stops:
            return None

        if direction == Direction.UP:
            # Floors above in ascending order
            ahead = sorted(f for f in all_stops if f > current_floor)
            if ahead:
                return ahead[0]
            # Reverse: pick highest below
            behind = sorted((f for f in all_stops if f < current_floor), reverse=True)
            return behind[0] if behind else None

        elif direction == Direction.DOWN:
            ahead = sorted((f for f in all_stops if f < current_floor), reverse=True)
            if ahead:
                return ahead[0]
            behind = sorted(f for f in all_stops if f > current_floor)
            return behind[0] if behind else None

        else:  # IDLE — go to nearest
            return min(all_stops, key=lambda f: abs(f - current_floor))

    def next_direction(self, current_floor: int, direction: Direction,
                       up_stops: Set[int], down_stops: Set[int]) -> Direction:
        all_stops = up_stops | down_stops
        if not all_stops:
            return Direction.IDLE

        if direction == Direction.UP:
            if any(f > current_floor for f in all_stops):
                return Direction.UP
            return Direction.DOWN

        elif direction == Direction.DOWN:
            if any(f < current_floor for f in all_stops):
                return Direction.DOWN
            return Direction.UP

        else:
            nxt = min(all_stops, key=lambda f: abs(f - current_floor))
            if nxt > current_floor:
                return Direction.UP
            elif nxt < current_floor:
                return Direction.DOWN
            return Direction.IDLE


class LOOKStrategy(SchedulingStrategy):
    """LOOK: like SCAN but reverses as soon as there are no more stops in current direction
       (doesn't go all the way to the end of the shaft)."""

    def next_floor(self, current_floor: int, direction: Direction,
                   up_stops: Set[int], down_stops: Set[int]) -> Optional[int]:
        all_stops = up_stops | down_stops
        if not all_stops:
            return None

        if direction in (Direction.UP, Direction.IDLE):
            ahead = sorted(f for f in all_stops if f > current_floor)
            if ahead:
                return ahead[0]
            behind = sorted((f for f in all_stops if f < current_floor), reverse=True)
            if behind:
                return behind[0]
            # Same floor
            if current_floor in all_stops:
                return current_floor
            return None

        else:  # DOWN
            ahead = sorted((f for f in all_stops if f < current_floor), reverse=True)
            if ahead:
                return ahead[0]
            behind = sorted(f for f in all_stops if f > current_floor)
            if behind:
                return behind[0]
            if current_floor in all_stops:
                return current_floor
            return None

    def next_direction(self, current_floor: int, direction: Direction,
                       up_stops: Set[int], down_stops: Set[int]) -> Direction:
        all_stops = up_stops | down_stops
        if not all_stops:
            return Direction.IDLE

        has_above = any(f > current_floor for f in all_stops)
        has_below = any(f < current_floor for f in all_stops)

        if direction == Direction.UP:
            return Direction.UP if has_above else (Direction.DOWN if has_below else Direction.IDLE)
        elif direction == Direction.DOWN:
            return Direction.DOWN if has_below else (Direction.UP if has_above else Direction.IDLE)
        else:
            if has_above and has_below:
                return Direction.UP  # default bias
            return Direction.UP if has_above else (Direction.DOWN if has_below else Direction.IDLE)


# ======================== Elevator (SRP — state + movement) ========================

class Elevator:
    """SRP: Manages its own state, door, current floor, and pending stops.
       DIP: Uses SchedulingStrategy abstraction for deciding movement."""

    def __init__(self, elevator_id: str, min_floor: int, max_floor: int, strategy: SchedulingStrategy):
        self.elevator_id = elevator_id
        self.min_floor = min_floor
        self.max_floor = max_floor
        self.current_floor = min_floor
        self.state = ElevatorState.STATIONARY
        self.direction = Direction.IDLE
        self.door = DoorState.CLOSED
        self._strategy = strategy

        # Separate stop sets for directional pickups
        self._up_stops: Set[int] = set()
        self._down_stops: Set[int] = set()

    # --- External request (floor button) ---
    def add_external_request(self, request: ExternalRequest):
        self._validate_floor(request.floor)
        if request.direction == Direction.UP:
            self._up_stops.add(request.floor)
        else:
            self._down_stops.add(request.floor)

    # --- Internal request (cabin button) ---
    def add_internal_request(self, request: InternalRequest):
        self._validate_floor(request.floor)
        # Add to the appropriate set based on relative position
        if request.floor > self.current_floor:
            self._up_stops.add(request.floor)
        elif request.floor < self.current_floor:
            self._down_stops.add(request.floor)
        else:
            # Same floor — open door
            self._up_stops.add(request.floor)

    def step(self) -> str:
        """Advance the elevator by one step. Returns a description of what happened."""
        if self.state == ElevatorState.OUT_OF_ORDER:
            return f"Elevator {self.elevator_id} is OUT OF ORDER"

        if not self._up_stops and not self._down_stops:
            self.state = ElevatorState.STATIONARY
            self.direction = Direction.IDLE
            return f"Elevator {self.elevator_id} idle at floor {self.current_floor}"

        # Determine direction
        self.direction = self._strategy.next_direction(
            self.current_floor, self.direction, self._up_stops, self._down_stops)

        # Determine next target
        target = self._strategy.next_floor(
            self.current_floor, self.direction, self._up_stops, self._down_stops)

        if target is None:
            self.state = ElevatorState.STATIONARY
            self.direction = Direction.IDLE
            return f"Elevator {self.elevator_id} idle at floor {self.current_floor}"

        if target == self.current_floor:
            # Service this floor
            return self._service_floor()

        # Move one floor toward target
        self.door = DoorState.CLOSED
        self.state = ElevatorState.MOVING
        if target > self.current_floor:
            self.current_floor += 1
        else:
            self.current_floor -= 1

        # Check if we've arrived at a stop
        if self.current_floor in self._up_stops or self.current_floor in self._down_stops:
            return self._service_floor()

        return f"Elevator {self.elevator_id} moving {self.direction.value} — now at floor {self.current_floor}"

    def set_out_of_order(self):
        self.state = ElevatorState.OUT_OF_ORDER
        self.door = DoorState.CLOSED

    def set_operational(self):
        self.state = ElevatorState.STATIONARY

    @property
    def pending_stops(self) -> Set[int]:
        return self._up_stops | self._down_stops

    @property
    def is_idle(self) -> bool:
        return self.state == ElevatorState.STATIONARY and self.direction == Direction.IDLE

    # --- Private helpers ---

    def _service_floor(self) -> str:
        self.state = ElevatorState.STATIONARY
        self.door = DoorState.OPEN
        self._up_stops.discard(self.current_floor)
        self._down_stops.discard(self.current_floor)

        # Update direction after servicing
        self.direction = self._strategy.next_direction(
            self.current_floor, self.direction, self._up_stops, self._down_stops)

        return (f"Elevator {self.elevator_id} STOPPED at floor {self.current_floor} — "
                f"doors OPEN (dir={self.direction.value})")

    def _validate_floor(self, floor: int):
        if floor < self.min_floor or floor > self.max_floor:
            raise ValueError(f"Floor {floor} is out of range [{self.min_floor}, {self.max_floor}]")

    def __repr__(self):
        return (f"Elevator({self.elevator_id}, floor={self.current_floor}, "
                f"state={self.state.value}, dir={self.direction.value}, door={self.door.value})")


# ======================== Controller (SRP — dispatching) ========================

class ElevatorController:
    """SRP: Dispatches external requests to the best elevator.
       DIP: Elevators already use strategy abstraction; controller just picks which elevator."""

    def __init__(self, elevators: List[Elevator]):
        self._elevators = elevators

    def handle_external_request(self, request: ExternalRequest):
        """Assign the request to the best elevator (nearest + same direction or idle)."""
        elevator = self._select_elevator(request)
        elevator.add_external_request(request)
        print(f"  -> Assigned {request} to {elevator.elevator_id}")

    def handle_internal_request(self, elevator_id: str, request: InternalRequest):
        elevator = self._get_elevator(elevator_id)
        elevator.add_internal_request(request)

    def step_all(self) -> List[str]:
        """Advance all elevators by one step."""
        return [e.step() for e in self._elevators]

    def run_until_idle(self, max_steps: int = 200) -> int:
        """Run all elevators until they are all idle. Returns step count."""
        steps = 0
        while steps < max_steps:
            if all(e.is_idle or e.state == ElevatorState.OUT_OF_ORDER for e in self._elevators):
                break
            logs = self.step_all()
            steps += 1
            for log in logs:
                if "idle" not in log.lower():
                    print(f"  Step {steps}: {log}")
        return steps

    def get_status(self) -> List[dict]:
        return [
            {
                "id": e.elevator_id,
                "floor": e.current_floor,
                "state": e.state.value,
                "direction": e.direction.value,
                "pending": sorted(e.pending_stops),
            }
            for e in self._elevators
        ]

    def set_out_of_order(self, elevator_id: str):
        self._get_elevator(elevator_id).set_out_of_order()

    def set_operational(self, elevator_id: str):
        self._get_elevator(elevator_id).set_operational()

    # --- Private ---

    def _select_elevator(self, request: ExternalRequest) -> Elevator:
        """Nearest elevator that is idle or going in the right direction."""
        best = None
        best_score = float('inf')

        for e in self._elevators:
            if e.state == ElevatorState.OUT_OF_ORDER:
                continue

            dist = abs(e.current_floor - request.floor)

            # Prefer idle elevators
            if e.is_idle:
                score = dist
            # Prefer elevator already going toward this floor in same direction
            elif e.direction == request.direction:
                if (request.direction == Direction.UP and e.current_floor <= request.floor) or \
                   (request.direction == Direction.DOWN and e.current_floor >= request.floor):
                    score = dist
                else:
                    score = dist + 100  # wrong side, penalize
            else:
                score = dist + 200  # opposite direction, heavy penalty

            if score < best_score:
                best_score = score
                best = e

        if best is None:
            raise RuntimeError("No operational elevators available")
        return best

    def _get_elevator(self, elevator_id: str) -> Elevator:
        for e in self._elevators:
            if e.elevator_id == elevator_id:
                return e
        raise ValueError(f"Elevator {elevator_id} not found")


# ======================== Building (Facade) ========================

class Building:
    """Facade that wires elevators and controller together."""
    def __init__(self, name: str, num_floors: int, num_elevators: int,
                 strategy: Optional[SchedulingStrategy] = None):
        self.name = name
        self.num_floors = num_floors
        strategy = strategy or SCANStrategy()

        elevators = [
            Elevator(f"E{i+1}", min_floor=0, max_floor=num_floors - 1, strategy=strategy)
            for i in range(num_elevators)
        ]
        self.controller = ElevatorController(elevators)

    def press_up(self, floor: int):
        """External button: someone on `floor` wants to go UP."""
        self.controller.handle_external_request(ExternalRequest(floor, Direction.UP))

    def press_down(self, floor: int):
        """External button: someone on `floor` wants to go DOWN."""
        self.controller.handle_external_request(ExternalRequest(floor, Direction.DOWN))

    def press_floor_button(self, elevator_id: str, floor: int):
        """Internal cabin button: passenger inside elevator selects destination."""
        self.controller.handle_internal_request(elevator_id, InternalRequest(floor))


# ======================== Demo ========================

if __name__ == "__main__":

    # --- 10-floor building with 2 elevators using SCAN ---
    building = Building("Tech Park Tower", num_floors=10, num_elevators=2)

    print("=== Initial Status ===")
    for s in building.controller.get_status():
        print(f"  {s['id']}: floor={s['floor']}, state={s['state']}, dir={s['direction']}")

    # --- Scenario 1: Person on floor 3 presses UP ---
    print("\n=== Person on floor 3 presses UP ===")
    building.press_up(3)
    building.controller.run_until_idle()

    # Passenger enters E1 and presses floor 7
    print("\n=== Passenger in E1 presses floor 7 ===")
    building.press_floor_button("E1", 7)
    building.controller.run_until_idle()

    # --- Scenario 2: Multiple requests ---
    print("\n=== Multiple requests: floor 1 UP, floor 9 DOWN, floor 5 UP ===")
    building.press_up(1)
    building.press_down(9)
    building.press_up(5)
    building.controller.run_until_idle()

    # Passengers press destinations
    print("\n=== Passengers select destinations ===")
    building.press_floor_button("E1", 8)   # person from floor 1 -> 8
    building.press_floor_button("E2", 6)   # person from floor 9 -> 6
    building.press_floor_button("E1", 6)   # person from floor 5 -> 6 (picked up on the way)
    building.controller.run_until_idle()

    # --- Scenario 3: Out of order ---
    print("\n=== E2 goes out of order ===")
    building.controller.set_out_of_order("E2")
    building.press_up(0)
    building.press_down(8)
    steps = building.controller.run_until_idle()

    print(f"\n=== Final Status (after {steps} steps) ===")
    for s in building.controller.get_status():
        print(f"  {s['id']}: floor={s['floor']}, state={s['state']}, dir={s['direction']}, pending={s['pending']}")

    # --- Scenario 4: LOOK strategy ---
    print("\n\n========== LOOK Strategy Demo ==========")
    building2 = Building("Mall Tower", num_floors=15, num_elevators=1, strategy=LOOKStrategy())

    print("\n=== Requests: floor 3 UP, floor 10 DOWN, floor 7 UP ===")
    building2.press_up(3)
    building2.press_down(10)
    building2.press_up(7)
    building2.controller.run_until_idle()

    # Passengers select floors
    building2.press_floor_button("E1", 12)  # from 3 -> 12
    building2.press_floor_button("E1", 5)   # from 10 -> 5
    building2.press_floor_button("E1", 9)   # from 7 -> 9
    print("\n=== Running all passengers to destinations ===")
    building2.controller.run_until_idle()

    print("\n=== Final ===")
    for s in building2.controller.get_status():
        print(f"  {s['id']}: floor={s['floor']}, state={s['state']}")