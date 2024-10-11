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

# Another solution


class Employee:
    def __init__(self, id, name, manager=None):
        self.id = id
        self.name = name
        self.manager = manager  # pointer to manager
        self.reports = []  # list of direct reports

    def add_report(self, report):
        self.reports.append(report)
        report.manager = self


def who_is_our_boss(emp1, emp2):
    # Get the chain of managers for emp1 and emp2, including themselves
    def get_chain_of_command(emp):
        chain = []
        while emp:
            chain.append(emp)
            emp = emp.manager
        return chain

    # Get the chains of managers for both employees
    chain1 = get_chain_of_command(emp1)
    chain2 = get_chain_of_command(emp2)

    # Reverse both chains to start from the CEO
    chain1.reverse()
    chain2.reverse()

    # Now find the lowest common manager by comparing both chains
    common_manager = None
    for e1, e2 in zip(chain1, chain2):
        if e1 == e2:
            common_manager = e1
        else:
            break

    return common_manager


# Example Usage
# Create employees as in the diagram
ceo = Employee(1, "A")
b1 = Employee(2, "B1")
b2 = Employee(3, "B2")
c1 = Employee(4, "C1")
c2 = Employee(5, "C2")
c3 = Employee(6, "C3")
c4 = Employee(7, "C4")

# Build hierarchy
ceo.add_report(b1)
ceo.add_report(b2)
b1.add_report(c1)
b1.add_report(c2)
b2.add_report(c3)
b2.add_report(c4)

# Find the common manager for two employees
result = who_is_our_boss(c1, c3)
print(f"The closest common manager is: {result.name}")  # Output: A (the CEO)
