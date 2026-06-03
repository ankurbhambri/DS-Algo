
'''
R1

We were given an array, a starting position, and a value x, and had to perform operations over multiple rounds.

In the i-th round, if i is odd, start from the current index and move to the left until you find the closest index whose value is exactly double the value at the current index.

Once such an index is found, add the given value x to the current index.

If i is even, perform the same process but search towards the right instead.

Continue performing these operations as long as they are possible.

'''

from collections import defaultdict
import bisect

from collections import defaultdict
from bisect import bisect_left, bisect_right, insort

def simulate(arr, pos, x):
    n = len(arr)

    # value -> sorted indices
    positions = defaultdict(list)

    for i, v in enumerate(arr):
        positions[v].append(i)

    round_no = 1

    while True:

        curr = arr[pos]
        target = 2 * curr

        idxs = positions.get(target, [])

        found = False

        if round_no % 2 == 1:  # search left

            k = bisect_left(idxs, pos)

            if k > 0:
                found = True

        else:  # search right

            k = bisect_right(idxs, pos)

            if k < len(idxs):
                found = True

        if not found:
            break

        # update arr[pos]
        old_val = arr[pos]
        new_val = old_val + x

        # remove pos from old value bucket
        old_idxs = positions[old_val]
        old_pos = bisect_left(old_idxs, pos)
        old_idxs.pop(old_pos)

        # insert into new value bucket
        insort(positions[new_val], pos)

        arr[pos] = new_val

        round_no += 1

    return arr


print(simulate([1, 3, 6, 12], 1, 2))  # Output: [1, 5, 8, 14]
print(simulate([1, 2, 4, 8], 0, 1))  # Output: [2, 3, 5, 9]


'''
R3
The question was:

Implement a function that, given a collection of words and a query prefix, returns all words that start with the given prefix.

Example:

words = ["abc", "abd", "abef", "xyz"]
prefix = "ab"

Output:

["abc", "abd", "abef"]

'''

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):

        node = self.root

        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()

            node = node.children[ch]

        node.is_word = True


def find_words_with_prefix(words, prefix):

    trie = Trie()

    for word in words:
        trie.insert(word)

    node = trie.root

    for ch in prefix:
        if ch not in node.children:
            return []
        node = node.children[ch]

    result = []
    def dfs(curr, path):

        if curr.is_word:
            result.append(path)

        for ch, nxt in curr.children.items():
            dfs(nxt, path + ch)

    dfs(node, prefix)

    return result


print(find_words_with_prefix(["abc", "abd", "xyz"], "ab"))  # Output: ["abc", "abd"]
print(find_words_with_prefix(["hello", "hi", "hey", "world"], "he"))  # Output: ["hello", "hey"]

'''
R4

The fourth round was based on LeetCode 2188:

https://leetcode.com/problems/minimum-time-to-finish-the-race/description/

The interviewer broke the problem into two parts. I solved the first part but could not solve the follow-up.

'''