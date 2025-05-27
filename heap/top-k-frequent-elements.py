import heapq
from collections import Counter

class Solution:
    def topKFrequent(self, nums, k):

        total_word_counts = Counter(nums) # O(N)

        heap = []
        for user, word_count in total_word_counts.items(): # O(N)
            # [freq, word]
            heapq.heappush(heap, (word_count, user)) # O(log k)
            if len(heap) > k:
                # heap pop means remove the smallest element from the root of the heap and then heapify the remaining elements
                # This ensures that we keep only the top k frequent elements in the heap
                heapq.heappop(heap)  # O(log k)
        
        # O(N log k)
        return [user for _, user in heap[:k]]


print(Solution().topKFrequent([1, 1, 1, 2, 2, 3], 2))  # [1, 2]
print(Solution().topKFrequent([1], 1))  # [1]
print(Solution().topKFrequent([1, 2], 2))  # [1, 2]
print(Solution().topKFrequent([1, 2, 3, 4, 5, 6, 7, 8, 9], 3))  # [7, 8, 9]
