def max_heapify(arr, k):
    l = left(k)
    r = right(k)
    if l < len(arr) and arr[l] > arr[k]:
        largest = l
    else:
        largest = k
    if r < len(arr) and arr[r] > arr[largest]:
        largest = r
    if largest != k:
        arr[k], arr[largest] = arr[largest], arr[k]
        max_heapify(arr, largest)


def left(k):
    return 2 * k + 1


def right(k):
    return 2 * k + 2


def build_max_heap(arr):

    n = int((len(arr) // 2) - 1)
    print(n)
    for k in range(n, -1, -1):
        max_heapify(arr, k)


arr = [10, 20, 15, 30, 40]
build_max_heap(arr)
print(arr)


# Usage of heap

from heapq import heapify, heappush, heappop


def solution(arr):
    arr = [-i for i in arr]
    heapify(arr)  # max heap simulation
    res = []
    while arr:
        val = -heappop(arr)
        res.append(val)
    return res


print(solution([10, 20, 15, 30, 40]))
