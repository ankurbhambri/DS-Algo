'''
Design an Expense Sharing System like Splitwise.

Requirements

    Add users who share expenses

    A paying user can split an expense:
    - Equal
    - Exact
    - Percent
    Maintain a running ledger:
    - Who owes whom

    User can view balances:
    - All balances
    - Specific user balance

'''

from enum import Enum


class SplitType(Enum):
    EQUAL = 1
    EXACT = 2
    PERCENT = 3


class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name

    def __str__(self):
        return self.name


class Split:
    def __init__(self, user, amount=0, percent=0):
        self.user = user
        self.amount = amount
        self.percent = percent


class Expense:
    def __init__(self, paid_by, amount, splits, split_type):
        self.paid_by = paid_by
        self.amount = amount
        self.splits = splits
        self.split_type = split_type


from abc import ABC, abstractmethod


class SplitStrategy(ABC):

    @abstractmethod
    def validate(self, expense):
        pass

    @abstractmethod
    def calculate(self, expense):
        pass


class EqualSplitStrategy(SplitStrategy):

    def validate(self, expense):
        return True

    def calculate(self, expense):
        total_users = len(expense.splits)
        amount_per_user = round(expense.amount / total_users, 2)

        for split in expense.splits:
            split.amount = amount_per_user


class ExactSplitStrategy(SplitStrategy):

    def validate(self, expense):
        total = sum(split.amount for split in expense.splits)
        return round(total, 2) == round(expense.amount, 2)

    def calculate(self, expense):
        pass


class PercentSplitStrategy(SplitStrategy):

    def validate(self, expense):
        total_percent = sum(split.percent for split in expense.splits)
        return total_percent == 100

    def calculate(self, expense):
        for split in expense.splits:
            split.amount = round((split.percent * expense.amount) / 100, 2)


class SplitStrategyFactory:

    @staticmethod
    def get_strategy(split_type):

        if split_type == SplitType.EQUAL:
            return EqualSplitStrategy()

        if split_type == SplitType.EXACT:
            return ExactSplitStrategy()

        if split_type == SplitType.PERCENT:
            return PercentSplitStrategy()

        raise Exception("Invalid Split Type")


from collections import defaultdict


class BalanceSheet:

    def __init__(self):
        self.balances = defaultdict(lambda: defaultdict(float))


class ExpenseService:

    def __init__(self):
        self.balance_sheet = BalanceSheet()

    def add_expense(self, expense):

        strategy = SplitStrategyFactory.get_strategy(expense.split_type)

        if not strategy.validate(expense):
            raise Exception("Invalid Expense")

        strategy.calculate(expense)

        paid_by = expense.paid_by

        for split in expense.splits:

            if split.user.user_id == paid_by.user_id:
                continue

            self.balance_sheet.balances[split.user][paid_by] += split.amount
            self.balance_sheet.balances[paid_by][split.user] -= split.amount
    
    def show_balances(self):

        for user in self.balance_sheet.balances:
            for other_user in self.balance_sheet.balances[user]:

                amount = self.balance_sheet.balances[user][other_user]

                if amount > 0:
                    print(f"{user} owes {other_user}: {amount}")


if __name__ == "__main__":

    u1 = User("u1", "A")
    u2 = User("u2", "B")
    u3 = User("u3", "C")
    u4 = User("u4", "D")

    service = ExpenseService()

    splits = [
        Split(u1),
        Split(u2),
        Split(u3),
        Split(u4)
    ]

    expense = Expense(
        paid_by=u1,
        amount=1000,
        splits=splits,
        split_type=SplitType.EQUAL
    )

    service.add_expense(expense)

    service.show_balances()