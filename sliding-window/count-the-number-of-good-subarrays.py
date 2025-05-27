from collections import defaultdict

def countGood(nums, k):    

    freq = defaultdict(int)
    left = 0
    pair_count = 0
    result = 0

    for right in range(len(nums)):
        # Add nums[right] to the window
        pair_count += freq[nums[right]]
        freq[nums[right]] += 1

        # Shrink window from the left if we have enough pairs
        while pair_count >= k:
            # At this point, we have at least k pairs in the window, and if we add more value in the window it will increase the number of subarray counts
            result += len(nums) - right  # So, thats why we are considering the remaining elements as subarray, including the current subarry
            freq[nums[left]] -= 1
            pair_count -= freq[nums[left]]
            left += 1

    return result

print(countGood([1,1,1,1,1], 10)) # Output: 1
print(countGood([3,1,4,3,2,2,4], 2)) # Output: 4