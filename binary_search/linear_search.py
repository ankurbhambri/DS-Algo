from Extras.functionExeutionDeco import measure


# O(n) time complexity


def linear_search(arr, target):
    if target in arr:
        return arr.index(target)
    else:
        return "Not Found"


# Linear Search call
arr = [2, 5, 1, 6, 0, 9, 7, 10]
target = 7
print(linear_search(arr, target))
