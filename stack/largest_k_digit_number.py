# https://leetcode.com/discuss/interview-question/5293722/Phone-Screen

"""
Find the largest k digit number , where number is to be choosen from the given array maintaing the order For example:

Arr=[4,9,0,2] k=2
Largest Number: 92

[4,0,2,9], K=2
Largest Number: 49

https://leetcode.com/discuss/interview-question/5293722/Phone-Screen

similar - https://leetcode.com/problems/remove-k-digits/description/

"""


def largest_k_digit_number(arr, k):
    n = len(arr)
    if k > n:
        return []

    stack = []
    to_remove = n - k

    for num in arr:
        while stack and k and stack[-1] < num:
            stack.pop()
            to_remove -= 1
        stack.append(num)

    return stack[:k]


print(largest_k_digit_number([4, 9, 0, 2], 2))  # Output: [9, 2]
print(largest_k_digit_number([4, 0, 2, 9], 2))  # Output [4, 9]
print(largest_k_digit_number([3, 5, 2, 6, 4, 8, 9], 4))  # Output: [6, 4, 8, 9]
