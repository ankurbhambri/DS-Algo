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


B1 = Employee("B1", "B1", "CEO", ["C1", "C2"])
B2 = Employee("B1", "B1", "CEO", ["C1", "C2"])
