'''
Requirements:
1. System manages 3 elevators serving 10 floors (0-9)
2. Users can request an elevator from any floor (hall call). System decides which elevator to dispatch.
3. Once inside, users can select one or more destination floors
4. Simulation runs in discrete time steps (e.g., a `step()` or `tick()` call advances time)
5. Elevator stops come in two types:
    - Hall calls: Request from a floor with direction (UP or DOWN)
    - Destination: Request from inside elevator (no direction specified)
6. System handles multiple concurrent pickup requests across floors
7. Invalid requests should be rejected (return false)
    - Non-existent floor numbers
8. Requests for the current floor are treated as a no-op / already served (doors out of scope)

Out of scope:
- Weight capacity and passenger limits
- Door open/close mechanics
- Emergency stop functionality
- Dynamic floor/elevator configuration
- UI/rendering layer
'''

import heapq
from enum import Enum


# ---------------- ENUMS ----------------
class Direction(Enum):
    UP = 1
    DOWN = -1
    IDLE = 0


# ---------------- REQUEST ----------------
class Request:
    def __init__(self, floor, direction=None):
        self.floor = floor
        self.direction = direction


# ---------------- ELEVATOR ----------------
class Elevator:
    def __init__(self, id, current_floor=0):
        self.id = id
        self.current_floor = current_floor
        self.direction = Direction.IDLE

        self.up_queue = []     # min heap
        self.down_queue = []   # max heap (store negative)

    def add_request(self, request: Request):

        if request.floor > self.current_floor:
            heapq.heappush(self.up_queue, request.floor)

        elif request.floor < self.current_floor:
            heapq.heappush(self.down_queue, -request.floor)

    def move(self):

        if self.direction == Direction.UP:
            if self.up_queue:
                self.current_floor = heapq.heappop(self.up_queue)
            else:
                self.direction = Direction.DOWN

        elif self.direction == Direction.DOWN:
            if self.down_queue:
                self.current_floor = -heapq.heappop(self.down_queue)
            else:
                self.direction = Direction.UP

        elif self.direction == Direction.IDLE:
            if self.up_queue:
                self.direction = Direction.UP
            elif self.down_queue:
                self.direction = Direction.DOWN

    def __str__(self):
        return f"Elevator {self.id} at floor {self.current_floor} going {self.direction.name}"


# ---------------- DISPATCHER ----------------
class ElevatorSystem:
    def __init__(self, elevators):
        self.elevators = elevators

    def request_elevator(self, request: Request):
        best = self._choose_elevator(request)
        best.add_request(request)

    def _choose_elevator(self, request):
        # Simple strategy: nearest elevator
        best = None
        min_distance = float("inf")

        for elevator in self.elevators:
            distance = abs(elevator.current_floor - request.floor)
            if distance < min_distance:
                min_distance = distance
                best = elevator

        return best

    def step(self):
        for elevator in self.elevators:
            elevator.move()


# ---------------- MAIN ----------------
if __name__ == "__main__":
    elevators = [Elevator(1), Elevator(2), Elevator(3)]
    system = ElevatorSystem(elevators)

    # hall requests
    system.request_elevator(Request(3))
    system.request_elevator(Request(7))
    system.request_elevator(Request(1))

    # simulate movement
    for _ in range(5):
        system.step()
        for e in elevators:
            print(e)
        print("-----")