# https://leetcode.com/problems/minimum-number-of-taps-to-open-to-water-a-garden/

def minTaps(n, ranges):

    max_reach = [0] * (n + 1)
    
    # Convert taps to intervals and store the farthest right point for each left point
    for i in range(n + 1):
        left = max(0, i - ranges[i])
        right = min(n, i + ranges[i])
        max_reach[left] = max(max_reach[left], right)

    taps = 0       # Number of taps opened
    curr_end = 0   # Current farthest point we can reach
    next_end = 0   # Next farthest point we can reach

    for i in range(n + 1):
        # If the current position is beyond what we could previously reach
        if i > next_end:
            return -1
        
        # If the current position is beyond current coverage, open another tap
        if i > curr_end:
            taps += 1
            curr_end = next_end

        next_end = max(next_end, max_reach[i])

    return taps

print(minTaps(5, [3,4,1,1,0,0]))  # Output: 1
print(minTaps(3, [0,0,0,0]))  # Output: -1
