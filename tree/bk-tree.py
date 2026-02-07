# https://www.kaggle.com/code/lennarthaupts/bk-tree-fuzzy-string-matches


import tqdm


def levenshtein(s1, s2):

    if len(s1) < len(s2):
        return levenshtein(s2, s1)

    if len(s2) == 0:
        return len(s1)

    previous_row = list(range(len(s2) + 1))

    for i, c1 in enumerate(s1):

        current_row = [i + 1]

        for j, c2 in enumerate(s2):
            insert = previous_row[j + 1] + 1
            delete = current_row[j] + 1
            replace = previous_row[j] + (1 if c1 != c2 else 0)
            current_row.append(min(insert, delete, replace))

        previous_row = current_row

    return previous_row[-1]

print(levenshtein("cat", "catt"))  # Output: 3
print(levenshtein("kitten", "sitting"))  # Output: 3
print(levenshtein("flaw", "lawn"))  # Output:

class Node:
    
    def __init__(self, word):
        self.word = word
        self.distances = []
        self.children = []
    
    
class BKTree:
    
    def __init__(self):
        self.root = None
        
    # builds tree from list of strings    
    def build_tree(self, word_list):
        self.root = Node(word_list.pop(0))
        for word in tqdm(word_list):
            self.add(word)
    
    # rfunction to add a word to the tree
    def add(self, word):
        
        def add_child(node, word):
            distance = levenshtein(node.word, word)
            if distance in node.distances:
                return add_child(node.children[node.distances.index(distance)], word)
            node.distances.append(distance)
            node.children.append(Node(word))
              
        add_child(self.root, word)

    # finds close matches to a word where the distance is <= threshold
    # returns a list of tuples (levenshtein-distance, word)
    def find(self, word, threshold):
        output_list = []

        candidates = [self.root]

        while len(candidates) > 0:
            curr_candidate = candidates.pop(0)
            curr_dist = levenshtein(curr_candidate.word, word)
            if threshold >= curr_dist:
                output_list.append((curr_dist, curr_candidate.word))
            candidates.extend(child for distance, child in zip(curr_candidate.distances, curr_candidate.children) 
                              if curr_dist - threshold <= distance <= curr_dist + threshold)
            
        return output_list


word_list = [Node("hello"), Node("hell"), Node("helloo"), Node("hellooa"), Node("hella"), Node("hallo"), Node("hellooab")]
bk_tree = BKTree()
# bk_tree.build_tree([node.word for node in word_list])
# print(bk_tree.find("hello", 1))
