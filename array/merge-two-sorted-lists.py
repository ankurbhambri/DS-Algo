# https://leetcode.com/problems/merge-two-sorted-lists/

'''
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

Logic is similar to the merge step in the merge sort algorithm
'''



def solution(arr1, arr2):

    i, j = 0, 0
    n, m = len(arr1), len(arr2)
    res = []

    # Iterating both arrays and appending the smaller element of both elements in result
    while i < n and j < m:

        if arr1[i] < arr2[j]:
            res.append(arr1[i])
            i += 1

        else:
            res.append(arr2[j])
            j += 1

    # if any remaining elements of arr1
    while i < n:
        res.append(arr1[i])
        i += 1

    # if any remaining elements of arr2
    while j < m:
        res.append(arr2[j])
        j += 1

    return res


# Example usage
arr1 = [1, 3, 4, 5, 12, 13]
arr2 = [2, 4, 6, 8, 9, 10]
print(solution(arr1, arr2))
