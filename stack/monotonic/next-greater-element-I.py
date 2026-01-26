# https://leetcode.com/problems/next-greater-element-i/description/

'''
                        Monotonic Stack Logic

Here, Brute force approach (nested loops) would take O(N^2) time, which is slow

Step 1: Problem Analysis
    - We use Monotonic Stack to optimize to O(N) time complexity

Step 2: Algorithm Strategy
    - Traverse the array from RIGHT to LEFT (reverse order)
    - Maintain a stack that keeps elements in decreasing order (monotonic stack)

Step 3: Stack Rule
    - Stack will only contain elements that have potential to be "Next Greater" for future elements

Step 4: Processing Logic
    - For each element, remove smaller elements from stack top
    - If stack has elements, the top element is our "Next Greater"
    - Push current element to stack for future processing

Step 5: Why Right to Left?
    - When we process element at index i, we already know the next greater 
    - elements for all positions to the right of i

'''

class Solution:
    def nextGreaterElement(self, nums1, nums2):

        # Step 1: nums2 ke har element ka next greater nikal kar map mein rakhein
        stack = []
        mapping = {}

        # Right to Left scan karein
        for num in reversed(nums2):

            # Jab tak stack mein chote elements hain, unhe hata do
            while stack and stack[-1] <= num:
                stack.pop()

            # Agar stack khali nahi hai, toh top element hi next greater hai
            if stack:
                mapping[num] = stack[-1]

            else:
                mapping[num] = -1

            # Current number ko stack mein daal dein
            stack.append(num)
    
        # Step 2: nums1 ke elements ke liye mapping se answer nikal lein
        return [mapping[n] for n in nums1]


print(Solution().nextGreaterElement([4,1,2], [1,3,4,2]))  # Output: [-1,3,-1]
print(Solution().nextGreaterElement([2,4], [1,2,3,4]))    # Output: [3,-1]


'''
Right Greater Element (RGE)
    Matlab: Apne se right side mein pehla bada number dhoondna.

    Logic (Simple Way): Hum array ko piche se (Right to Left) scan karenge. Stack mein hum un numbers ko rakhenge jo right side mein hain aur "bade" hain.

    Piche se shuru karo.

    Stack se wo saare numbers nikal do jo current number se chote ya barabar hain.

    Ab stack ke top par jo bacha hai, wahi aapka Right Greater hai.

    Current number ko stack mein daal do.
'''

def get_right_greater(nums):

    n = len(nums)
    rge = [-1] * n
    stack = []

    for i in range(n - 1, -1, -1):
        while stack and stack[-1] <= nums[i]:
            stack.pop()

        if stack:
            rge[i] = stack[-1]

        stack.append(nums[i])

    return rge

print(get_right_greater([4, 5, 2, 10, 8]))  # Output: [5, 10, 10, -1, -1]
print(get_right_greater([2, 7, 3, 5, 4, 6, 8]))  # Output: [7, 8, 5, 6, 6, 8, -1]


# Is baar hum array ko shuru se (Left to Right) scan karenge. Stack mein hum un numbers ko rakhenge jo left side mein guzar chuke hain aur "bade" hain.
def get_left_greater(nums):

    n = len(nums)
    lge = [-1] * n
    stack = []

    for i in range(n):

        while stack and stack[-1] <= nums[i]:
            stack.pop()

        if stack:
            lge[i] = stack[-1]

        stack.append(nums[i])

    return lge