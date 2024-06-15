# Q1 - https://leetcode.com/problems/subsets/submissions/
# Q2 - https://leetcode.com/problems/subsets-ii/


def power_set(elements):
    n = len(elements)
    power_set_size = 2**n
    power_set_result = []

    # seen = set()

    for i in range(power_set_size):
        subset = []
        for j in range(n):
            # This is a bitwise operation to check if the jth bit is set in i
            if i & (1 << j):
                subset.append(elements[j])

        # For Q2 need to add these commented line as well
        # subset.sort()
        # if tuple(subset) not in seen:
        #     power_set_result.append(subset)
        #     seen.add(tuple(subset))

        power_set_result.append(subset)

    return power_set_result


# TC - O(2^N * N) - 2^n is the number of subsets in the power set, and for each subset, the function iterates over all elements (length n) bitmasking operation (i & (1 << j)).
# SC - O(2^N * N) - 2^n subsets and each subset can have at most n elements.


elements = [1, 2, 3]
print(power_set(elements))


# Tricky way to solve both questions but TC and SC is same as above.


# Q1
def subsets(nums):
    res = [[]]
    for num in nums:
        res += [i + [num] for i in res]
    return res


# Q2
def subsetsWithDup(nums):
    res = [[]]
    for num in nums:
        res += [i + [num] for i in res]

    present = set()
    ans = []
    for i in res:
        i.sort()
        if tuple(i) not in present:
            ans.append(i)
            present.add(tuple(i))

    return ans
