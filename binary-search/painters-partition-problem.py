# https://www.geeksforgeeks.org/dsa/painters-partition-problem/


# Checks whether all boards can be painted within 'maxTime' by dividing the work among at most k painters
def isPossible(maxTime, arr, k):
    painters = 1
    currSum = 0

    for length in arr:
        
        # if a board is longer than maxTime,
        # it's impossible to assign
        if length > maxTime:
            return False

        # if assigning this board exceeds maxTime, 
        # give it to a new painter
        if currSum + length > maxTime:
            painters += 1
            currSum = length
        
        # otherwise, continue adding to the current 
        # painter's workload
        else:
            currSum += length

    # return true if total painters used is
    # within the allowed k
    return painters <= k

def minTime(arr, k):

    low = max(arr)
    high = sum(arr)
    result = high

    while low <= high:
        mid = (low + high) // 2

        # if this time allows us to paint
        # with k painters or fewer
        if isPossible(mid, arr, k):
            result = mid
            high = mid - 1
            
        # if not possible, we need to allow 
        # more time
        else:
            low = mid + 1

    return result


print(minTime([5, 10, 30, 20, 15], 3))
print(minTime([10, 20, 30, 40], 2))


# allocate-minimum-number-of-pages

# https://www.geeksforgeeks.org/problems/allocate-minimum-number-of-pages0937/1

def isPossible(maxPages, arr, k):
    students = 1
    currSum = 0

    for pages in arr:
        
        # if a book has more pages than maxPages,
        # it's impossible to assign
        if pages > maxPages:
            return False

        # if assigning this book exceeds maxPages, 
        # give it to a new student
        if currSum + pages > maxPages:
            students += 1
            currSum = pages
        
        # otherwise, continue adding to the current 
        # student's workload
        else:
            currSum += pages

    # return true if total students used is
    # within the allowed k
    return students <= k

def minPages(arr, k):

    if len(arr) < k:
        return -1

    low = max(arr)
    high = sum(arr)
    result = high

    while low <= high:

        mid = (low + high) // 2

        # if this page limit allows us to assign
        # with k students or fewer
        if isPossible(mid, arr, k):
            result = mid
            high = mid - 1

        # if not possible, we need to allow 
        # more pages
        else:
            low = mid + 1

    return result


print(minPages([15, 17, 20], 2))
print(minPages([12, 34, 67, 90], 2))