# Given an array of integers, our task is to write a program that efficiently finds the second-largest element present in the array.

# TC: O(N) where N is length of array
# SC: O(1) we are not using any extra space
def solution(arr):

    a, b = 0, 0

    for i in arr:

        if i > a:
            b = a
            a = i

        elif i > b and i != a:
            b = i

    return b

print(solution([2, 2, 2])) # Output: 0
print(solution([10, 5, 10])) # Output: 5
print(solution([12, 35, 1, 10, 34, 1])) # Output: 34