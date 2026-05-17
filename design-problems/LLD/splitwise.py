'''
Design Splitwise

Requirements
- The system should allow users to create accounts and manage their profile information.
- Users should be able to create groups and add other users to the groups.
- Users should be able to add expenses within a group, specifying the amount, description, and participants.
- The system should automatically split the expenses among the participants based on their share.
- Users should be able to view their individual balances with other users and settle up the balances.
- The system should support different split methods, such as equal split, percentage split, and exact amounts.
- Users should be able to view their transaction history and group expenses.
- The system should handle concurrent transactions and ensure data consistency.

'''

from threading import Lock
from abc import ABC, abstractmethod
from collections import defaultdict


class User:
    def __init__(self, user_id, name, email):
        self.id = user_id
        self.name = name
        self.email = email

class Group:

    def __init__(self, group_id, name):
        self.id = group_id
        self.name = name
        self.members = []

    def add_member(self, user):
        self.members.append(user)

class Split:
    def __init__(self, user, amount):
        self.user = user
        self.amount = amount


# STRATEGY PATTERN
class SplitStrategy(ABC):

    @abstractmethod
    def calculate(self, amount, users):
        pass


class EqualSplit(SplitStrategy):

    def calculate(self, amount, users):
        split_amount = amount / len(users)
        return [Split(user, split_amount) for user in users]


class ExactSplit(SplitStrategy):

    def calculate(self, amount, users, amounts):
        return [
            Split(users[i], amounts[i])
            for i in range(len(users))
        ]


class PercentageSplit(SplitStrategy):

    def calculate(self, amount, users, percentages):

        splits = []

        for i in range(len(users)):
            split_amount = amount * percentages[i] / 100
            splits.append(Split(users[i], split_amount))

        return splits

class Expense:

    def __init__(self, description, amount, paid_by, group, splits):
        self.description = description
        self.amount = amount
        self.paid_by = paid_by
        self.group = group
        self.splits = splits


class ExpenseService:

    def __init__(self):
        self.lock = Lock()

        # transaction history
        self.expenses = []

        # balances[A][B]
        # positive means A owes B
        self.balances = defaultdict(lambda: defaultdict(float))

    def add_expense(self, expense):

        with self.lock:

            # store history
            self.expenses.append(expense)

            payer = expense.paid_by

            for split in expense.splits:

                user = split.user
                amount = split.amount

                if user == payer:
                    continue

                # user owes payer
                self.balances[user][payer] += amount
                self.balances[payer][user] -= amount

    def show_balances(self):

        with self.lock:

            visited = set()

            for user in self.balances:

                for other in self.balances[user]:

                    if (other, user) in visited:
                        continue

                    amount = self.balances[user][other]

                    if amount > 0.01:
                        print(
                            f"{user.name} owes "
                            f"{other.name}: {amount:.2f}"
                        )

                    visited.add((user, other))

    def show_expense_history(self):

        for expense in self.expenses:

            print(
                f"{expense.paid_by.name} paid "
                f"{expense.amount} "
                f"for {expense.description}"
            )


if __name__ == "__main__":

    # create users
    alice = User(1, "Alice", "alice@example.com")
    bob = User(2, "Bob", "bobthebuilder@example.com")
    charlie = User(3, "Charlie", "charlie@example.com")

    # create group
    group = Group(1, "Trip")
    group.add_member(alice)
    group.add_member(bob)
    group.add_member(charlie)

    # create expense service
    expense_service = ExpenseService()

    # add expenses
    expense1 = Expense(
        description="Hotel",
        amount=300,
        paid_by=alice,
        group=group,
        splits=EqualSplit().calculate(300, group.members)
    )

    expense_service.add_expense(expense1)
    expense2 = Expense(
        description="Dinner",
        amount=150,
        paid_by=bob,
        group=group,
        splits=PercentageSplit().calculate(150, group.members, [50, 30, 20])
    )

    expense_service.add_expense(expense2)

    # show balances
    expense_service.show_balances()

    # show expense history
    expense_service.show_expense_history()