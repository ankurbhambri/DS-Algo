'''
Design a search autoc   omplete system for a search engine. Users may input a sentence (at least one word and end with a special character '#').

You are given a string array sentences and an integer array times both of length n,
where sentences[i] is a previously typed sentence and times[i] is the corresponding number of times the sentence was typed. 
For each input character except '#', return the top 3 historical hot sentences that have the same prefix as the part of the sentence already typed.

Here are the specific rules:

The hot degree for a sentence is defined as the number of times a user typed the exactly same sentence before.
The returned top 3 hot sentences should be sorted by hot degree (The first is the hottest one).
If several sentences have the same hot degree, use ASCII-code order (smaller one appears first).

If less than 3 hot sentences exist, return as many as you can.
When the input is a special character, it means the sentence ends, and in this case, you need to return an empty list.
Implement the AutocompleteSystem class:

AutocompleteSystem(String[] sentences, int[] times) Initializes the object with the sentences and times arrays.
List<String> input(char c) This indicates that the user typed the character c.

Returns an empty array [] if c == '#' and stores the inputted sentence in the system.

Returns the top 3 historical hot sentences that have the same prefix as the part of the sentence already typed. 
If there are fewer than 3 matches, return them all.
 

Example 1:

Input
["AutocompleteSystem", "input", "input", "input", "input"]
[[["i love you", "island", "iroman", "i love leetcode"], [5, 3, 2, 2]], ["i"], [" "], ["a"], ["#"]]
Output
[null, ["i love you", "island", "i love leetcode"], ["i love you", "i love leetcode"], [], []]

Explanation
AutocompleteSystem obj = new AutocompleteSystem(["i love you", "island", "iroman", "i love leetcode"], [5, 3, 2, 2]);
obj.input("i"); // return ["i love you", "island", "i love leetcode"]. There are four sentences that have prefix "i". Among them, "ironman" and "i love leetcode" have same hot degree. Since ' ' has ASCII code 32 and 'r' has ASCII code 114, "i love leetcode" should be in front of "ironman". Also we only need to output top 3 hot sentences, so "ironman" will be ignored.
obj.input(" "); // return ["i love you", "i love leetcode"]. There are only two sentences that have prefix "i ".
obj.input("a"); // return []. There are no sentences that have prefix "i a".
obj.input("#"); // return []. The user finished the input, the sentence "i a" should be saved as a historical sentence in system. And the following input will be counted as a new search.
 

Constraints:

n == sentences.length
n == times.length
1 <= n <= 100
1 <= sentences[i].length <= 100
1 <= times[i] <= 50
c is a lowercase English letter, a hash '#', or space ' '.
Each tested sentence will be a sequence of characters c that end with the character '#'.
Each tested sentence will have a length in the range [1, 200].
The words in each input sentence are separated by single spaces.
At most 5000 calls will be made to input.

'''

import collections
import heapq

class Sentence:
    def __init__(self, sentence, count):

        self.count = count
        self.sentence = sentence

    def __lt__(self, other):
        # Min-Heap Logic: 
        # 1. If counts are different, the one with SMALLER count is "less" (gets popped)
        # 2. If counts are same, the one with LARGER ASCII (alphabetically later) is "less"
        if self.count == other.count:
            return self.sentence > other.sentence
        return self.count < other.count

class AutocompleteSystem:
    def __init__(self, sentences, times):

        self.root = {}
        self.current_sentence = ""
        self.counts = collections.defaultdict(int)
        for s, t in zip(sentences, times):
            self.counts[s] = t
            self._insert(s, t)

    def _insert(self, sentence, count):

        node = self.root
        for char in sentence:
            if char not in node:
                node[char] = {}
            node = node[char]
            if "data" not in node:
                node["data"] = collections.defaultdict(int)
            node["data"][sentence] = count

    def input(self, c: str):

        if c == "#":
            self.counts[self.current_sentence] += 1
            self._insert(self.current_sentence, self.counts[self.current_sentence])
            self.current_sentence = ""
            return []

        self.current_sentence += c
        node = self.root
        for char in self.current_sentence:
            if char not in node:
                return []
            node = node[char]

        # Use a Min-Heap to find top 3
        heap = []
        for sentence, count in node["data"].items():
            heapq.heappush(heap, Sentence(sentence, count))
            if len(heap) > 3:
                heapq.heappop(heap)

        # Pop from heap and reverse to get top 3 in order
        res = []
        while heap:
            res.append(heapq.heappop(heap).sentence)
        return res[::-1]

print(
    AutocompleteSystem(
        ["i love you", "island", "iroman", "i love leetcode"],
        [5, 3, 2, 2]
    ).input("i")
) # ["i love you", "island", "i love leetcode"]