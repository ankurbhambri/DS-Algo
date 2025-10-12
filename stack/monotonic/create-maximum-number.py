# https://leetcode.com/problems/create-maximum-number/


class Solution:
    def maxNumber(self, nums1, nums2, k):

        def maxSubseq(nums, k):

            if k == 0:
                return []

            drop = len(nums) - k  # kitne elements drop kar sakte hain
            stack = []
            
            for num in nums:
                # Jab tak stack mein chhote elements hain aur hum drop kar sakte hain
                while drop > 0 and stack and stack[-1] < num:
                    stack.pop()
                    drop -= 1
                stack.append(num)

            return stack[:k]  # exactly k elements return karo
        
        def merge(nums1, nums2):
            """Merge two arrays to form maximum number"""
            result = []
            i, j = 0, 0
            
            while i < len(nums1) and j < len(nums2):
                # Compare remaining portions, not just single digits
                if nums1[i:] > nums2[j:]:
                    result.append(nums1[i])
                    i += 1
                else:
                    result.append(nums2[j])
                    j += 1
            
            # Remaining elements add karo
            result.extend(nums1[i:])
            result.extend(nums2[j:])
            
            return result
        
        def isGreater(nums1, nums2):
            """Check if nums1 > nums2 lexicographically"""
            for i in range(len(nums1)):
                if nums1[i] > nums2[i]:
                    return True
                elif nums1[i] < nums2[i]:
                    return False
            return False
        
        m, n = len(nums1), len(nums2)
        maxNum = []
        
        # Try all valid splits: i elements from nums1, k-i from nums2
        for i in range(max(0, k - n), min(k, m) + 1):
            # nums1 se i elements aur nums2 se k-i elements
            sub1 = maxSubseq(nums1, i)
            sub2 = maxSubseq(nums2, k - i)
            
            # Merge them optimally
            candidate = merge(sub1, sub2)
            
            # Update max if this is better
            if not maxNum or isGreater(candidate, maxNum):
                maxNum = candidate
        
        return maxNum


print(Solution().maxNumber([3,4,6,5], [9,1,2,5,8,3], 5))  # Output: [9,8,6,5,3]
print(Solution().maxNumber([6,7], [6,0,4], 5))        # Output: [6,7,6,0,4]
print(Solution().maxNumber([3,9], [8,9], 3))            # Output: [9,8,9]
print(Solution().maxNumber([2,5,6,4,4,0], [7,3,8,0,6,5,7,6,2], 15))  # Output: [7,3,8,2,5,6,4,4,0,6,5,7,6,2]
