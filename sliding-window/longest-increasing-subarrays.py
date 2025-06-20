'''
Given an array of integers, find the first longest continuously ascending subsequence.

Return a string containing:
1. The subsequence elements (comma-separated)
2. The starting index of the subsequence
3. The ending index of the subsequence

Examples:
- For array [1, 2, 3, 1, 2]:
  - Longest ascending: [1, 2, 3]
  - Output:
    subsequence: 1,2,3
    first: 0
    last: 2

- For array [5, 3, 4, 8, 6, 7]:
  - Longest ascending: [3, 4, 8]
  - Output:
    subsequence: 3,4,8
    first: 1
    last: 3

Return "Exception" for any invalid inputs.

'''


def longest_ascending_subsequence(nums):

    if not nums:
        return
    
    l = 0
    max_start, max_end, max_len = 0, 0, 1

    for r in range(1, len(nums)):

        if nums[r] <= nums[r - 1]:
            # reset the left pointer to the current right pointer
            l = r

        else:
            # check if current subsequence is longer
            current_len = r - l + 1

            if current_len > max_len:

                max_len = current_len

                max_start = l
                max_end = r
    
    result = [
        f"subsequence: {', '.join(map(str, nums[max_start: max_end + 1]))}",
        f"first: {max_start}",
        f"last: {max_end}"
    ]
    
    return "\n".join(result)


print(longest_ascending_subsequence([1, 2, 3, 1, 2]))  # Example 1
print(longest_ascending_subsequence([5, 3, 4, 8, 6, 7]))  # Example 2
