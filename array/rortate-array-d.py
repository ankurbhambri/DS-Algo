# Program for array left rotation by d positions.
# https://www.geeksforgeeks.org/array-rotation/


def solution(arr, d):

    def rotate(arr, i, j):
        while i < j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1

    n = len(arr)
    rotate(arr, 0, d - 1)
    rotate(arr, d, n - 1)
    rotate(arr, 0, n - 1)

    return arr


print(solution([1, 2, 3, 4, 5, 6, 7], 2))
