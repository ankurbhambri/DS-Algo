class TrieNode:
    def __init__(self):
        self.children = {}
        self.suggestions = []

class Solution:
    def suggestedProducts(self, products, searchWord):
        products.sort()  # Sort lexicographically

        # Build Trie
        head = TrieNode()
        for product in products:
            curr = head
            for char in product:
                if char not in curr.children:
                    curr.children[char] = TrieNode()
                curr = curr.children[char]
                if len(curr.suggestions) < 3:
                    curr.suggestions.append(product)

        # Search Suggestions
        result = []
        curr = head
        for char in searchWord:
            if curr and char in curr.children:
                curr = curr.children[char]
                result.append(curr.suggestions)
            else:
                curr = None
                result.append([])

        return result

print(
    Solution().suggestedProducts(
        ["mobile", "mouse", "moneypot", "monitor", "mousepad"],
        "mouse"
    )
) # [['mobile', 'moneypot', 'monitor'], ['mobile', 'moneypot', 'monitor'], ['mouse', 'mousepad'], ['mouse', 'mousepad'], ['mouse', 'mousepad']]
print(
    Solution().suggestedProducts(
        ["havana", "hat", "havana", "havana"],
        "havana"
    )
) # [['hat', 'havana', 'havana'], ['hat', 'havana', 'havana'], ['havana', 'havana', 'havana'], ['havana', 'havana', 'havana'], ['havana', 'havana', 'havana'], ['havana', 'havana', 'havana']]