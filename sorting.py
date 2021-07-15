'''It's a simple sorting algorithm. This sorting algorithm is comparison-based algorithm
in which each pair of adjacent elements is compared and the elements are swapped if they
are not in order.'''


def recursive_bubble_sort(arr):  # O(n)
    count = 0
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
            count += 1
    if count == 0:
        return arr
    else:
        return recursive_bubble_sort(arr)


def bubble_sort(arr):  # Ο(n^2)

    for i in range(len(arr)):
        for k in range(len(arr) - 1):
            if arr[k] > arr[k + 1]:
                arr[k], arr[k + 1] = arr[k + 1], arr[k]
    return arr


def insertion_sort(arr):
    '''Insertion sort is a simple sorting algorithm that works the way we sort
    playing cards in our hands.'''
    for j in range(1, len(arr)):
        value = arr[j]
        i = j - 1
        while i >= 0 and arr[i] > value:
            arr[j] = arr[i]
            i -= 1
        arr[j] = value
    return arr


def selection_sort(arr):
    '''The selection sort algorithm sorts an array by repeatedly finding the minimum
    element (considering ascending order) from unsorted part and putting it at
    the beginning. The algorithm maintains two subarrays in a given array.

    1) The subarray which is already sorted.
    2) Remaining subarray which is unsorted.

    In every iteration of selection sort, the minimum element (considering ascending order)
    from the unsorted subarray is picked and moved to the sorted subarray.'''

    for i in range(len(arr)):
        min_val = min(arr[i : len(arr)])
        pos = arr.index(min_val)
        if min_val < arr[i]:
            arr[pos], arr[i] = arr[i], min_val
    return arr


def quickSort(arr):
    n = len(arr)

    if n < 2:
        return arr

    # Position of the partitioning element
    current_position = 0

    # Partitioning loop
    for i in range(1, n):
        if arr[i] <= arr[0]:
            current_position += 1
            arr[i], arr[current_position] = arr[current_position], arr[i]

    # Brings pivot to it's appropriate position
    arr[0], arr[current_position] = arr[current_position], arr[0]

    # Sorts the elements to the left of pivot
    left = quickSort(arr[0:current_position])
    # sorts the elements to the right of pivot
    right = quickSort(arr[current_position + 1 : n])

    # Merging everything together
    arr = left + [arr[current_position]] + right

    return arr


def swapSort(arr):

    '''swap sorting on the basis of index position values
    like 1 index 2 is needed if values is present in
    its indes then no swap'''
    for i in range(len(arr)):
        if arr[i] != arr[arr[i] - 1]:
            arr[arr[i] - 1], arr[i] = arr[i], arr[arr[i] - 1]
    # position where wrong nos is present
    for i in range(len(arr)):
        if i + 1 != arr[i]:
            print('swap sort duplicate', arr[i], 'swap sort missing', i + 1)


if __name__ == "__main__":

    arr = [45, 3, 67, 56, 8, 0]

    print('Recursive Bubble Sort', recursive_bubble_sort(arr))

    # print('Bubble Sort', buuble_sort(arr))

    print('Insertion Sort', insertion_sort(arr))

    print('Selection Sort', selection_sort(arr))

    print("Quick Sort", quickSort(arr))

    arr2 = [2, 3, 1, 8, 2, 3, 5, 1]

    swapSort(arr2)
