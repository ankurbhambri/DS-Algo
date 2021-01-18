class Searching():

    def linear_search(self, arr, srch_val):
        ''' This is the simplest technique 
        to find out an element in an unsorted list
        with O(n) time complexity
        '''
        # linear serach pytonic way
        if srch_val in arr:
            return arr.index(srch_val)
        else:
            return 'Not Found'

    # Returns index of x in arr if present, else -1

    def binarySearch(self, arr, l, r, x):
        ''' This technique works on 
        sorted list and it  repeatedly 
        dividing the search interval in half.
        If the value of the search key is less 
        than the item in the middle of the interval, 
        narrow the interval to the lower half. 
        Otherwise narrow it to the upper half. 
        Repeatedly check until the value is found 
        or the interval is empty.
        It's time complexity is O(log n)
        mid = (low+hig)/2
        '''
        # Check base case
        if r >= l:

            mid = l + (r - l) // 2

            # If element is present at the middle itself
            if arr[mid] == x:
                return mid

            # If element is smaller than mid, then it
            # can only be present in left subarray
            elif arr[mid] > x:
                return self.binarySearch(arr, l, mid-1, x)

            # Else the element can only be present
            # in right subarray
            else:
                return self.binarySearch(arr, mid + 1, r, x)

        else:
            # Element is not present in the array
            return -1

# Driver Code
if __name__ == "__main__":
    cls_obj = Searching()

    # Linear Search call
    arr = [2, 5, 1, 6, 0, 9, 7, 10]
    srch = 7
    print('Linear Search Element is present at index', cls_obj.linear_search(arr, srch))

    # Binary Search call
    arr = [2, 3, 4, 10, 40]
    x = 10
    result = cls_obj.binarySearch(arr, 0, len(arr)-1, x)

    if result != -1:
        print("Binary Search Element is present at index", result)
    else:
        print("Binary Search Element is not present in array")
