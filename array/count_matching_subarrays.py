"""

Given an array of integers numbers and an array pattern representing a comparison pattern,
find how many subarrays of numbers match the given pattern.

The pattern can only contain the following integers:
• 1: the next number must be greater than the previous one.
• 0: the next number must be equal to the previous one.
• -1: the next number must be less than the previous one.

It is guaranteed that numbers.length > pattern.length. Note: You are not expected to provide the most optimal solution,
but a solution with time complexity not worse than O(numbers.length * pattern.length) will fit within the execution time limit.

"""


def count_matching_subarrays(numbers, pattern):

    n, m = len(numbers), len(pattern)

    # Precompute comparison between consecutive elements
    def cmp(a, b):
        return (a < b) - (a > b)  # 1 if a<b, -1 if a>b, 0 if equal

    comp = [cmp(numbers[i], numbers[i + 1]) for i in range(n - 1)]

    count = 0
    for i in range(n - m):
        if comp[i : i + m] == pattern:
            count += 1

    return count


print(count_matching_subarrays([1, 1, 1, 1], [0, 0]))  # 2
print(count_matching_subarrays([1, 2, 3, 4, 5, 6], [1, 1]))  # 4
print(count_matching_subarrays([1, 4, 4, 1, 3, 5, 5, 3], [1, 0, -1]))  # 2