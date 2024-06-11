"""
https://www.geeksforgeeks.org/count-pairs-with-given-sum/

Given an array of N integers, and an integer K, the task is to find the number of pairs of integers in the array whose sum is equal to K.

Similar to https://leetcode.com/problems/subarray-sum-equals-k/
"""


# idea whenever asked to find pairs with sum equal to K, use hashmap and
def getPairsCount(arr, n, k):

    hm = {0: 1}
    res = 0
    sm = 0

    for i in range(n):

        sm += arr[i]

        res += hm.get(sm - k, 0)

        hm[sm] = 1 + hm.get(sm, 0)

    return res


arr = [1, 5, 7, -1]
n = len(arr)
sum = 6
print("Count of pairs is", getPairsCount(arr, n, sum))
