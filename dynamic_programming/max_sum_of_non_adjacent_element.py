# https://www.codingninjas.com/codestudio/problems/maximum-sum-of-non-adjacent-elements_843261

def maximumNonAdjacentSum(nums):    
    n1, n2 = 0, 0
    for n in nums:
        n1, n2 = n2, max(n1 + n, n2)
    return n2

# similar to house robber problem leetcode
# https://leetcode.com/problems/house-robber/

def rob(self, nums: List[int]) -> int:

  rob1, rob2 = 0, 0

  for n in nums:
      rob1, rob2 = rob2, max(n + rob1, rob2)

  return rob2
