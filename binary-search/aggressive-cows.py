# https://www.naukri.com/code360/problems/aggressive-cows_1082559

'''

You are given an array 'arr' consisting of 'n' integers which denote the position of a stall.

You are also given an integer 'k' which denotes the number of aggressive cows.

You are given the task of assigning stalls to 'k' cows such that the minimum distance between any two of them is the maximum possible.

Print the maximum possible minimum distance.

Example:
    Input: 'n' = 3, 'k' = 2 and 'arr' = {1, 2, 3}

    Output: 2

    Explanation: The maximum possible minimum distance will be 2 when 2 cows are placed at positions {1, 3}. Here distance between cows is 2.

'''

# TC: O(n log n) -> O(n log(max(arr)))
# SC: O(1)

# Idea, we will use binary search to find the maximum possible minimum distance between cows. 
# First we will sort the stalls, then we will use binary search on the distance between the first and last stall. 
# For each mid value, we will check if it is possible to place k cows with that minimum distance using a helper function. 
# If it is possible, we will try for a larger distance; otherwise, we will try a smaller one.

def aggressiveCows(stalls, k):

    stalls.sort()

    n = len(stalls)

    l, r = 1, stalls[-1] - stalls[0]

    res = 0  # we store the best possible minimum distance

    def isPossible(mid):
        count = 1  # place the first cow at stalls[0]
        lastPos = stalls[0]

        for i in range(1, n):
            # distance between the current stall and the last placed cow must be at least mid, 
            # if it is, we can place another cow, otherwise we skip this stall and check the next one.
            if stalls[i] - lastPos >= mid:
                count += 1
                lastPos = stalls[i]

                # if we have placed k cows, we can return True
                # as we have found a valid configuration with at least mid distance.
                # We can try for a larger distance now.
                if count == k:
                    return True

        return False

    while l <= r:
        m = (l + r) // 2 # l + (r - l) // 2 to avoid overflow
        if isPossible(m):
            res = m     # m is a valid answer, then try for a larger one, this is asked in the question
            l = m + 1
        else:
            r = m - 1

    return res


print(aggressiveCows([1, 2, 4, 8, 9], 3))  # Output: 3
print(aggressiveCows([1, 2, 3, 4, 5], 2))  # Output: 4
print(aggressiveCows([1, 2, 3, 4, 5], 3))  # Output: 3
print(aggressiveCows([1, 2, 3, 4, 5], 4))  # Output: 2
