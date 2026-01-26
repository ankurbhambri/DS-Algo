# https://leetcode.com/problems/two-sum-iii-data-structure-design/description/

'''

Design a data structure that accepts a stream of integers and checks if it has a pair of integers that sum up to a particular value.

Implement the TwoSum class:

    TwoSum() Initializes the TwoSum object, with an empty array initially.

    void add(int number) Adds number to the data structure.

    boolean find(int value) Returns true if there exists any pair of numbers whose sum is equal to value, otherwise, it returns false.

'''

class TwoNumberSum:
    def __init__(self):

        self.hm = {}

    def add(self, num: int) -> None:

        self.hm[num] = 1 + self.hm.get(num, 0)

    def find(self, target: int) -> bool:

        for num in self.hm:

            val = target - num

            if val == num and self.hm[num] > 1:
                return True

            elif val in self.hm:
                return True

        return False

ts = TwoNumberSum()
ts.add(1)
ts.add(3)
ts.add(5)
print(ts.find(4))  # True (1 + 3)
print(ts.find(7))  # False (no two numbers sum to 7)
print(ts.find(6))  # True (1 + 5)
