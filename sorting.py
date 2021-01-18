class Sorting:

    def buuble_sort(self, arr):
        ''' It's a simple sorting algorithm. This sorting algorithm is comparison-based algorithm 
        in which each pair of adjacent elements is compared and the elements are swapped if they 
        are not in order. This algorithm is not suitable for large data sets as its average and 
        worst case complexity are of Ο(n^2) where n is the number of items.'''

        for i in range(len(arr)):
            for k in range(len(arr)-1):
                if arr[k] > arr[k+1]:
                    arr[k], arr[k+1] = arr[k+1], arr[k]
        return arr

    def insertion_sort(self, arr):
        ''' Insertion sort is a simple sorting algorithm that works the way we sort 
        playing cards in our hands.'''
        for i in range(1, len(arr)):
            key = arr[i]
            k = i-1
            while k >= 0 and key < arr[k]:
                arr[k+1] = arr[k]
                k -= 1
            arr[k+1] = key
        return arr

    def selection_sort(self, arr):
        ''' The selection sort algorithm sorts an array by repeatedly finding the minimum 
            element (considering ascending order) from unsorted part and putting it at 
            the beginning. The algorithm maintains two subarrays in a given array.

            1) The subarray which is already sorted.
            2) Remaining subarray which is unsorted.

            In every iteration of selection sort, the minimum element (considering ascending order) 
            from the unsorted subarray is picked and moved to the sorted subarray.'''

        for i in range(len(arr)):
            min_val = min(arr[i:len(arr)])
            pos = arr.index(min_val)
            if min_val < arr[i]:
                arr[pos], arr[i] = arr[i], min_val
        return arr

    # Quick Sort:
    def partition(self, arr, l, r):

        pivot = arr[r]
        i = l - 1
        for j in range(l, r-1):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i+1], arr[r] = arr[r], arr[i+1]
        return i+1

    def quickSort(self, arr, l, h):
        if len(arr) == 1:
            return arr
        if l < h:
            pi = self.partition(arr, l, h)
            self.quickSort(arr, l, pi-1)
            self.quickSort(arr, pi+1, h)

        return arr


if __name__ == "__main__":

    arr = [45, 3, 67, 56, 8, 0]
    obj = Sorting()

    # print('Bubble Sort', obj.buuble_sort(arr))

    # print('Insertion Sort', obj.insertion_sort(arr))

    # print('Selection Sort', obj.selection_sort(arr))

    # print("Quick Sort", obj.quickSort(arr, 0, len(arr)-1))
