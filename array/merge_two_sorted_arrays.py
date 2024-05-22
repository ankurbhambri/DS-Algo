# Logic is similar to the merge step in the merge sort algorithm


def solution(arr1, arr2):

    i, j = 0, 0

    res = []

    # Iterating both arrays and appending the smaller element of both elements in result
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            res.append(arr1[i])
            i += 1
        else:
            res.append(arr2[j])
            j += 1

    # if any remaining elements of arr1
    while i < len(arr1):
        res.append(arr1[i])
        i += 1

    # if any remaining elements of arr2
    while j < len(arr2):
        res.append(arr2[j])
        j += 1

    return res


# Example usage
arr1 = [1, 3, 4, 5, 12, 13]
arr2 = [2, 4, 6, 8, 9, 10]
print(solution(arr1, arr2))
