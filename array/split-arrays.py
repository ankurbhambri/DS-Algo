"""
    Given an array of integers arr and an integer k, split the array into k contiguous subarrays. 
    The size of each subarray should be as equal as possible, meaning no two subarrays should differ in size by more than one element. 
    If there are not enough elements to fill all k subarrays, the remaining subarrays should be empty.

    Constraints:
    0 <= len(arr) <= 1000
    0 <= arr[i] <= 1000
    1 <= k <= 50
"""

def splitArray(arr, k):

    n = len(arr)
    result = []
    
    # Edge case: agar array empty hai ya k invalid hai
    if n == 0 or k <= 0:
        return [[] for _ in range(k)]
    
    # Base size aur extra elements calculate karo
    base_size = n // k
    extra = n % k
    
    start = 0
    for i in range(k):
        # Agar elements khatam ho gaye, toh empty subarray
        if start >= n:
            result.append([])
            continue
        
        # Size decide karo
        size = base_size + 1 if i < extra else base_size
        
        # Extra safety: ensure size doesn't overshoot
        if start + size > n:
            size = n - start  # Adjust size to remaining elements
            
        # Subarray banao
        result.append(arr[start: start + size])
        start += size
    
    return result


print(splitArray([1, 2, 3], 5))  # [[1], [2], [3], [], []]
print(splitArray([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3))  # [[1, 2, 3, 4], [5, 6, 7], [8, 9, 10]]
