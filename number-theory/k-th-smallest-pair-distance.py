# https://leetcode.com/problems/find-k-th-smallest-pair-distance/

def smallestDistancePair(nums, K):

    def total_cost_to_make_all_x(x):
        return sum(abs(a - x) for a in nums)
    
    low, high = min(nums), max(nums)
    min_cost = float('inf')

    while low <= high:
        mid = (low + high) // 2
        cost_mid = total_cost_to_make_all_x(mid)
        cost_next = total_cost_to_make_all_x(mid + 1)

        min_cost = min(min_cost, cost_mid, cost_next)

        if cost_mid < cost_next:
            high = mid - 1
        else:
            low = mid + 1

    return min_cost <= K
