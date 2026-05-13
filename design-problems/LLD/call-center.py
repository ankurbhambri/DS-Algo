'''
Imagine you have a call center with three levels of employees: respondent
manager, and director. An incoming telephone call must be first allocated
to a respondent who is free. If the respondent can't handle the call, he or
she must escalate the call to a manager. If the manager is not free or not
able to handle it, then the call should be escalated to a director. 

Design the classes and data structures for this problem.

Implement a method dispatchCall() which assigns a call to the first available employee.

'''

from enum import IntEnum
from collections import deque


class Rank(IntEnum):
    RESPONDENT = 0
    MANAGER = 1
    DIRECTOR = 2


class Employee:
    def __init__(self, name, rank):
        self.name = name
        self.rank = rank
        self.is_free = True

    def take_call(self, call):
        self.is_free = False
        print(f"{self.rank.name} {self.name} is handling the call.")

    def finish_call(self):
        self.is_free = True


# super().__init__() is like a bridge that connects a "Child" class to its "Parent" class.
class Respondent(Employee):
    def __init__(self, name):
        super().__init__(name, Rank.RESPONDENT)


class Manager(Employee):
    def __init__(self, name):
        super().__init__(name, Rank.MANAGER)


class Director(Employee):
    def __init__(self, name):
        super().__init__(name, Rank.DIRECTOR)


class CallHandler:
    def __init__(self, respondents: list[Respondent], managers: list[Manager], directors: list[Director]):
        # We store employees in levels for easy access
        self.employee_levels = [respondents, managers, directors]
        self.call_queue = deque()

    def dispatch_call(self, call):
        """
        Assigns the call to the first available employee starting 
        from the lowest rank possible.
        """
        employee = self._get_available_employee()
        
        if employee:
            employee.take_call(call)
        else:
            print("All employees busy. Adding call to waiting queue.")
            self.call_queue.append(call)

    def _get_available_employee(self):
        # Check each level from Respondent (0) to Director (2)
        for level in self.employee_levels:
            for emp in level:
                if emp.is_free:
                    return emp
        return None


# 1. Setup our staff
staff_r = [Respondent("Alice"), Respondent("Bob")]
staff_m = [Manager("Charlie")]
staff_d = [Director("Diana")]

center = CallHandler(staff_r, staff_m, staff_d)

# 2. Simulate incoming calls
print("--- Call 1 ---")
center.dispatch_call("User Help Request") # Alice takes it

print("\n--- Call 2 ---")
center.dispatch_call("Billing Issue")     # Bob takes it

print("\n--- Call 3 ---")
center.dispatch_call("Technical Bug")     # Charlie (Manager) takes it because Alice/Bob are busy

print("\n--- Call 4 ---")
center.dispatch_call("Critical Outage")   # Diana (Director) takes it