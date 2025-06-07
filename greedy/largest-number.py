class Solution:
    def largestNumber(self, nums):
        # Convert all integers to strings for comparison
        nums = list(map(str, nums))

        # Custom comparator inside merge sort
        def compare(x, y):
            return x + y > y + x

        # Merge Sort implementation
        def merge_sort(arr):
            if len(arr) <= 1:
                return arr
            mid = len(arr) // 2
            left = merge_sort(arr[:mid])
            right = merge_sort(arr[mid:])
            return merge(left, right)

        def merge(left, right):
            result = []
            i = j = 0
            while i < len(left) and j < len(right):
                if compare(left[i], right[j]):
                    result.append(left[i])
                    i += 1
                else:
                    result.append(right[j])
                    j += 1
            result.extend(left[i:])
            result.extend(right[j:])
            return result

        # Apply merge sort
        sorted_nums = merge_sort(nums)

        # Edge case: all numbers are zero
        if sorted_nums[0] == '0':
            return '0'

        # Join and return
        return ''.join(sorted_nums)


print(Solution().largestNumber([10, 2]))  # Output: "210"
print(Solution().largestNumber([3, 30, 34, 5, 9]))  # Output: "9534330"
print(Solution().largestNumber([1, 20, 23, 4, 8]))  # Output: "8423201"
print(Solution().largestNumber([0, 0]))  # Output: "0"
