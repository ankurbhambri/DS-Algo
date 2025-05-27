def productExceptSelf(nums):

    n = len(nums)
    
    # Create prefix and suffix product arrays
    l = [1] * n  # Left product
    r = [1] * n  # Right product
    res = [1] * n  # Result array
    
    # Compute prefix products
    for i in range(1, n):
        l[i] = l[i - 1] * nums[i - 1]

    # Compute suffix products
    for i in range(n - 2, -1, -1):
        r[i] = r[i + 1] * nums[i + 1]

    # Compute result array
    for i in range(n):
        res[i] = l[i] * r[i]
    
    return res

print(productExceptSelf([1, 2, 3, 4]))  # Output: [24, 12, 8, 6]
print(productExceptSelf([1, 2, 3, 4, 5]))  # Output: [120, 60, 40, 30, 24]