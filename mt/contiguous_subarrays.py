import sys
import os

# Add the parent directory to the sys.path
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))
sys.path.append(parent_dir)


from Extras.test_case_check import check

"""

Contiguous Subarrays

You are given an array arr of N integers. For each index i, you are required to determine the number of contiguous subarrays that fulfill the following conditions:
The value at index i must be the maximum element in the contiguous subarrays, and
These contiguous subarrays must either start from or end on index i.

Signature
int[] countSubarrays(int[] arr)

Input
Array arr is a non-empty list of unique integers that range between 1 to 1,000,000,000
Size N is between 1 and 1,000,000

Output
An array where each index i contains an integer denoting the maximum number of contiguous subarrays of arr[i]

Example:
arr = [3, 4, 1, 6, 2]
output = [1, 3, 1, 5, 1]

Explanation:
For index 0 - [3] is the only contiguous subarray that starts (or ends) at index 0 with the maximum value in the subarray being 3.
For index 1 - [4], [3, 4], [4, 1]
For index 2 - [1]
For index 3 - [6], [6, 2], [1, 6], [4, 1, 6], [3, 4, 1, 6]
For index 4 - [2]
So, the answer for the above input is [1, 3, 1, 5, 1]

"""


def countSubarrays(arr):
    n = len(arr)
    left = [0] * n
    right = [0] * n

    # Calculate left distances
    stack = []
    for i in range(n):
        while stack and arr[stack[-1]] < arr[i]:
            stack.pop()
        left[i] = i - stack[-1] if stack else i + 1
        stack.append(i)

    # Clear stack for right distances calculation
    stack = []

    # Calculate right distances
    for i in range(n - 1, -1, -1):
        while stack and arr[stack[-1]] < arr[i]:
            stack.pop()
        right[i] = stack[-1] - i if stack else n - i
        stack.append(i)

    # Calculate the result
    result = [left[i] + right[i] - 1 for i in range(n)]

    return result


expected_1 = [1, 3, 1, 5, 1]
output_1 = countSubarrays([3, 4, 1, 6, 2])
check(expected_1, output_1)

expected_2 = [1, 2, 6, 1, 3, 1]
output_2 = countSubarrays([2, 4, 7, 1, 5, 3])
check(expected_2, output_2)
