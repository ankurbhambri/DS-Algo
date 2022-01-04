"""It's a simple sorting algorithm. This sorting algorithm is comparison-based algorithm
in which each pair of adjacent elements is compared and the elements are swapped if they
are not in order."""


def recursive_bubble_sort(arr, n):  # O(n)

    if n == 1:
        return arr
    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]

    return recursive_bubble_sort(arr, n - 1)


def bubble_sort(arr):  # Ο(n^2)

    for i in range(len(arr)):
        for k in range(len(arr) - 1):
            if arr[k] > arr[k + 1]:
                arr[k], arr[k + 1] = arr[k + 1], arr[k]
    return arr


def insertion_sort(arr):
    """Insertion sort is a simple sorting algorithm that works the way we sort
    playing cards in our hands."""
    for j in range(1, len(arr)):
        value = arr[j]
        i = j - 1
        while i >= 0 and arr[i] > value:
            arr[j] = arr[i]
            i -= 1
        arr[j] = value
    return arr


def selection_sort(arr):
    """The selection sort algorithm sorts an array by repeatedly finding the minimum
    element (considering ascending order) from unsorted part and putting it at
    the beginning. The algorithm maintains two subarrays in a given array.

    1) The subarray which is already sorted.
    2) Remaining subarray which is unsorted.

    In every iteration of selection sort, the minimum element (considering ascending order)
    from the unsorted subarray is picked and moved to the sorted subarray."""

    for i in range(len(arr)):
        min_val = min(arr[i : len(arr)])
        pos = arr.index(min_val)
        if min_val < arr[i]:
            arr[pos], arr[i] = arr[i], min_val
    return arr


def partitioning(arr, l, h):

    pivot = arr[l]

    i, j = l, h

    while i < j:

        while arr[i] <= pivot:
            i += 1

        while arr[j] > pivot:
            j -= 1

        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    arr[l], arr[j] = arr[j], arr[l]

    return j


def quickSort(arr, l, h):

    if l < h:

        j = partitioning(arr, l, h)

        quickSort(arr, l, j)
        quickSort(arr, j + 1, h)

    return arr


def swapSort(arr):

    """swap sorting on the basis of index position values
    like 1 index 2 is needed if values is present in
    its indes then no swap"""
    # O(n^2)
    for i in range(len(arr)):
        if arr[i] != arr[arr[i] - 1]:
            arr[arr[i] - 1], arr[i] = arr[i], arr[arr[i] - 1]
    # position where wrong nos is present
    for i in range(len(arr)):
        if i + 1 != arr[i]:
            print("swap sort duplicate", arr[i], "swap sort missing", i + 1)
    # O(n)
    for i in range(len(arr) - 1):
        if arr[i] != arr[arr[i] - 1]:
            arr[arr[i] - 1], arr[i] = arr[i], arr[arr[i] - 1]

        if i + 1 != arr[i]:
            print(i + 1)

    print(arr)


def mergeSort(arr):

    if len(arr) > 1:

        mid = len(arr) // 2

        L = arr[:mid]

        R = arr[mid:]

        mergeSort(L)

        mergeSort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

    return arr


if __name__ == "__main__":

    arr = [45, 3, 67, 56, 8, 0]

    print("Recursive Bubble Sort", recursive_bubble_sort(arr, len(arr)))

    # print('Bubble Sort', buuble_sort(arr))

    print("Insertion Sort", insertion_sort(arr))

    print("Selection Sort", selection_sort(arr))

    print("Quick Sort", quickSort(arr, 0, len(arr) - 1))

    arr2 = [2, 3, 1, 8, 2, 3, 5, 1]

    swapSort(arr2)

    arr = [54, 26, 93, 17, 77, 31, 44, 55, 20]

    print("Merge Sort", mergeSort(arr))
