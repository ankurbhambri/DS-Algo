# https://leetcode.com/problems/random-pick-index/description/

# TC: O(n) for initialization, O(1) for pick
# SC: O(n)

import random
from collections import defaultdict

class Solution:

    def __init__(self, nums):
        self.d = defaultdict(list)

        for i, num in enumerate(nums):
            self.d[num].append(i)

    def pick(self, target: 'int') -> 'int':
        return random.choice(self.d[target])


print(Solution([1, 2, 3, 3, 3]).pick(3))
print(Solution([1, 2, 3, 3, 3]).pick(1))
print(Solution([1, 2, 3, 3, 3]).pick(3))


# Reservoir Sampling approach

# TC: O(n) for pick
# SC: O(1)

class Solution:

    def __init__(self, nums):
        self.nums = nums

    def pick(self, target: 'int') -> 'int':
        count = 0
        result = -1

        for i, num in enumerate(self.nums):
            if num == target:
                count += 1
                # 1/count probability se select karo, if selected, update result
                if random.randint(1, count) == count:
                    result = i

        return result

print(Solution([1, 2, 3, 3, 3]).pick(3))
print(Solution([1, 2, 3, 3, 3]).pick(1))
print(Solution([1, 2, 3, 3, 3]).pick(3))


# Variant:

# What if you had to sample K random numbers in an array?

import random

def getKRandom(nums, k):

    # 1. Pehle k elements ko reservoir mein bharo
    reservoir = nums[:k]

    # 2. Baaki elements ke liye loop chalao
    for i in range(k, len(nums)):
        j = random.randint(0, i) # 0 se current index tak random
        if j < k:
            reservoir[j] = nums[i] # Replace purana with naya

    return reservoir


# What if you had to sample one random index of the maximum value in an array?

import random

def pickRandomMaxIndex(nums):

    count = 0
    result_index = -1
    max_val = float('-inf')

    for i in range(len(nums)):

        if nums[i] > max_val:
            # Naya king mil gaya!
            max_val = nums[i]
            result_index = i
            count = 1

        elif nums[i] == max_val:
            # Ek aur barabar wala mila
            count += 1
            # 1/count probability ke saath naya index select karo
            if random.randint(1, count) == 1:
                result_index = i
                
    return result_index