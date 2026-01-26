'''
Given an array like [1,2,3,4] build the second largest number you can using these digits
for this example it is => [4, 3, 1, 2]
'''

from collections import Counter

# TC: O(N) where N is length of nums
# SC: O(N) we are using an extra array to store the answer


def second_largest(nums):

    counter = Counter(nums)

    # edge cases: no 2nd largest
    if len(counter) == 1:
        return None

    ans = []
    n = len(nums)

    for i in range(10, -1, -1):
        if i in counter:
            ans += [i] * counter[i]

    # build 2nd largest, while swapping the first decreasing pair from right
    for i in range(n - 1, -1, -1):
        if ans[i - 1] > ans[i]:
            ans[i], ans[i - 1] = ans[i - 1], ans[i]
            break

    return ans


print(second_largest([1])) # Output: None
print(second_largest([2, 2, 2, 2, 2, 2])) # Output: None 
print(second_largest([1, 2, 3, 4])) # Output: [4, 3, 1, 2]
print(second_largest([4, 3, 2, 1])) # Output: [4, 2, 3, 1]