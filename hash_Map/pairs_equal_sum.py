# https://www.geeksforgeeks.org/count-pairs-with-given-sum/

"""
Given an array of N integers, and an integer K, the task is to find the number of pairs of integers in the array whose sum is equal to K.
"""


def getPairsCount(arr, n, sum):

    hm = {}
    count = 0

    for i in range(n):

        diff = sum - arr[i]

        if diff in hm:

            count += hm[diff]

        hm[arr[i]] = 1 + hm.get(arr[i], 0)

    return count


# Driver code
arr = [1, 5, 7, -1]
n = len(arr)
sum = 6
print("Count of pairs is", getPairsCount(arr, n, sum))
