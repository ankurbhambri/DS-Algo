# Subarray
# A subarray is a contiguous slice of an array that maintains the order of elements.
# For example, the subarrays of array [1, 2, 3] are:
# [1], [1, 2], [1, 2, 3], [2], [2, 3], and [3].

# Function to print all subarrays of the specified array
def print_all_subarrays(nums):
    # Iterate over all possible starting points
    for i in range(len(nums)):
        # Iterate over all possible ending points
        for j in range(i, len(nums)):
            # Print the subarray from index i to j
            print(nums[i: j + 1])

if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5]
    print("Subarrays:")
    print_all_subarrays(nums)

# Substring
# A substring is a contiguous slice of a string.
# For example, the substrings of the string 'apple' are:
# 'apple', 'appl', 'pple', 'app', 'ppl', 'ple', 'ap', 'pp', 'pl', 'le', 'a', 'p', 'l', 'e', ''.

# Function to print all non-empty substrings of the specified string
def print_all_substrings(s):
    # Iterate over all possible starting points
    for i in range(len(s)):
        # Iterate over all possible ending points
        for j in range(i, len(s)):
            # Print the substring from index i to j
            print(s[i: j + 1], end=' ')

if __name__ == '__main__':
    s = 'techie'
    print("\nSubstrings:")
    print_all_substrings(s)

# Subsequence
# A subsequence is a sequence derived from another sequence by deleting some elements
# without changing the order of the remaining elements.
# For example, 'ace' is a subsequence of 'abcde', but not a substring.

# Function to generate all subsequences (power set) of the specified sequence
def find_power_set(seq):
    # Total number of subsets is 2^n
    N = int(pow(2, len(seq)))
    result = []

    # Generate each subset
    for i in range(N):
        subset = ''
        for j in range(len(seq)):
            # Check if the j-th bit in i is set
            if (i & (1 << j)) != 0:
                subset += seq[j]
        result.append(subset)
    print(result)

if __name__ == '__main__':
    seq = 'apple'
    print("\nSubsequences (Power Set):")
    find_power_set(seq)

# Subset
# A subset is any possible combination of elements from the original set.
# Unlike subsequences, subsets do not need to maintain the relative order of elements.
# For example, {3, 1} is a valid subset of {1, 2, 3, 4, 5}, but it is neither a subsequence nor a subarray.

# Note: Subsets are already covered by the power set function above.
