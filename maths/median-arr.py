# Given an array arr[], the task is to find the median of this array. 
# The median of an array of size n is defined as the middle element when n is odd and the average of the middle two elements when n is even.

def findMedian(arr):
    n = len(arr)
    
    arr.sort()

    if n % 2 != 0:
        return arr[n // 2]

    return (arr[(n - 1) // 2] + arr[n // 2]) // 2

arr = [1, 3, 4, 2, 7, 5, 8, 6]
ans = findMedian(arr)
print(ans)
