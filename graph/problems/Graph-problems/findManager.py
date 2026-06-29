# There is a company which has a CEO and a hierarchy of employees. All employees have a unique ID, name and a pointer to their manager and their reports.
# Please implement the who_is_our_boss() method to find the closest manager for two given employees (i.e. the manager farthest from the CEO that both employees report up to).

#            A =
#        B1       B2
#      C1  C2   C3  C4
#    CD1 CD2 C2D3 C2D4 C3D5 C3D6 ...
#    .
#    E1

# employee_mapping dictionary

# [
#     {manager: null, reportee: A}
#     {manager: C1D1, reportee: E1}
#     {manager: C1D1, reportee: E2}
#     {manager: C2D1, reportee: E3}
#     {manager: C3D1, reportee: E4}
# ]


# e1_list = [B1 A]
# e2_list = [A]


class Employee:

    def __init__(self, id, name, manager, reportees, isManager):
        # id: int # unique ID
        # name: str # name (not unique)
        # manager: Employe # None for CEO
        # reports: set # empty set for a non-manager

        self.id = id
        self.name = name
        self.isManager = isManager
        self.manager = manager
        self.reports = []

    # ['A', "B1", "B2", "B1"]
    def find(self, employee):
        if employee.manager != self.manager:
            employee.manager = self.find(employee.manager)
        return employee.manager

    def union(self, emp1, emp2):

        manager1, manager2 = self.find(emp1), self.find(emp2)

        if manager1.manager == manager2.manager:
            return manager1
        else:
            return self.union(manager1, manager2)

    def who_is_our_boss(self, emp1, emp2):
        #
        if emp1.manager == emp2:
            return emp2.manager
        elif emp2.manager == emp1:
            return emp1.manager
        return self.union(emp1, emp2)


# B1 = Employee("B1", "B1", "CEO", ["C1", "C2"])
# B2 = Employee("B1", "B1", "CEO", ["C1", "C2"])

# Another solution


class Employee:
    def __init__(self, name, manager=None):
        self.name = name
        self.manager = manager  # Pointer to the manager object


def who_is_our_boss(e1, e2):
    """
    Find the closest common manager for two employees.

    :param e1: Employee 1
    :param e2: Employee 2
    :return: Closest common manager (Employee object)
    """

    # Helper function to trace the hierarchy up to the CEO
    def get_hierarchy_path(employee):
        path = []
        while employee:
            path.append(employee)
            employee = employee.manager
        return path

    # Get paths for both employees
    e1_path = get_hierarchy_path(e1)
    e2_path = get_hierarchy_path(e2)

    # Reverse the paths to start from the CEO
    e1_path.reverse()
    e2_path.reverse()

    # Find the lowest common ancestor
    closest_manager = None
    for m1, m2 in zip(e1_path, e2_path):
        if m1 == m2:
            closest_manager = m1
        else:
            break
    return closest_manager


ceo = Employee("A")
b1 = Employee("B1", ceo)
b2 = Employee("B2", ceo)
c1 = Employee("C1", b1)
c2 = Employee("C2", b1)
c3 = Employee("C3", b2)
c4 = Employee("C4", b2)
cd1 = Employee("C1D1", c1)
e1 = Employee("E1", cd1)

# Find the closest manager
boss = who_is_our_boss(c1, c2)
print("Closest common manager:", boss.name if boss else "None")  # Output: B1

# TC: O(h), where h is the depth of the hierarchy.
# Space Complexity: O(h)
