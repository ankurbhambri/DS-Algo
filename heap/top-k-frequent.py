'''
There are two type on leetcode 

1) https://leetcode.com/problems/top-k-frequent-elements/
2) https://leetcode.com/problems/top-k-frequent-words/description/

- First one is the top k frequent elements problem, where we need to find the top k frequent elements in an array of integers, hete Tie-breaker: Does not matte.

- Second one is the top k frequent words problem, where we need to find the top k frequent words in a list of strings in lexicographical order and higher frequency.

'''

from collections import Counter
import heapq

# https://leetcode.com/problems/top-k-frequent-elements/

class Solution:
    def topKFrequent(self, nums, k: int):

        total_word_counts = Counter(nums) # O(N)

        heap = []
        for user, word_count in total_word_counts.items(): # O(k)
            heapq.heappush(heap, (word_count, user)) # O(log k)
            if len(heap) > k:
                heapq.heappop(heap)  # O(log k)
        
        # O(N log k)
        return [user for word_count, user in heap[:k]]

print(Solution().topKFrequent([1, 1, 1, 2, 2, 3], 2))  # [1, 2]
print(Solution().topKFrequent([1], 1))  # [1]
print(Solution().topKFrequent([1, 2], 2))  # [1, 2]
print(Solution().topKFrequent([1, 2, 3, 4, 5, 6, 7, 8, 9], 3))  # [7, 8, 9]


# https://leetcode.com/problems/top-k-frequent-words/description/

class Element:
    def __init__(self, count, word):
        self.count = count
        self.word = word
        
    def __lt__(self, other):
        if self.count == other.count:
            return self.word > other.word
        return self.count < other.count
    
    def __eq__(self, other):
        return self.count == other.count and self.word == other.word

class Solution(object):
    def topKFrequent(self, words, k):

        counts = Counter(words)
        
        hm = []
        heapq.heapify(hm)
        for word, count in counts.items():
            heapq.heappush(hm, (Element(count, word), word))
            if len(hm) > k:
                heapq.heappop(hm)
        
        res = []
        for _ in range(k):
            res.append(heapq.heappop(hm)[1])
        return res[::-1]

print(Solution().topKFrequent(["i", "love", "leetcode", "i", "love", "coding"], 2))  # ["i", "love"]
print(Solution().topKFrequent(["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], 4))  # ["the", "is", "sunny", "day"]
print(Solution().topKFrequent(["a", "b", "c", "a", "b", "c", "a"], 2))  # ["a", "b"]
print(Solution().topKFrequent(["a", "b", "c", "d", "e", "f", "g"], 3))  # ["e", "f", "g"]
