def sumSubarrayMins(arr):
    
    M = 10 ** 9 + 7
    sums = 0
    n = len(arr)

    st = []
    
    for r in range(n + 1):
        
        while st and (r == n or arr[st[-1]] >= arr[r]):

            m = st.pop()
            l = st[-1] if st else -1
            sums += arr[m] * (m - l) * (r - m)

        st.append(r)
        
    return sums % M

print(sumSubarrayMins([3, 1, 2, 4]))  # Output: 17
print(sumSubarrayMins([5, 4, 3, 2, 1]))  # Output: 35
print(sumSubarrayMins([1, 3, 3]))  # Output: 12



from collections import deque

def sumSubarrayMins1(nums):
    MOD = 10**9 + 7
    n = len(nums)
    
    # Initialize arrays
    next_smaller = [n] * n
    prev_smaller = [-1] * n
    
    # Monotonic stack
    q = deque()
    
    # Fill next_smaller and prev_smaller
    for i in range(n):
        while q and nums[q[-1]] > nums[i]:
            t = q.pop()
            next_smaller[t] = i
        if q:
            prev_smaller[i] = q[-1]
        q.append(i)
    
    # Calculate contribution of each element
    total = 0
    for i in range(n):
        left = i - prev_smaller[i]  # Subarrays on the left
        right = next_smaller[i] - i  # Subarrays on the right
        total = (total + nums[i] * left * right) % MOD
        
    return total
    

print(sumSubarrayMins1([3, 1, 2, 4]))  # Output: 17
print(sumSubarrayMins1([5, 4, 3, 2, 1]))  # Output: 35
print(sumSubarrayMins1([1, 3, 3]))  # Output: 12