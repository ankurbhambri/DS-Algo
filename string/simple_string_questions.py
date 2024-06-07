# Write a function to count the number of times each character appears in a string and rewrite the string in that format. Eg. "I am back." should become "i1 2a2m1b1c1k1.1"


def solution(s):
    freq = {}
    for i in s:
        freq[i] = 1 + freq.get(i, 0)
    res = ""
    for j in s:
        if j in freq:
            res += j + str(freq[j])
            del freq[j]
    return res


print(solution("I am back."))


# Count Words in a Sentence
def count_words(sentence):
    words = sentence.split()
    return len(words)


print(count_words("This is a sample sentence with several words"))


def validate_ip(s):
    a = s.split(".")
    if len(a) != 4:
        return False
    for x in a:
        if not x.isdigit():
            return False
        i = int(x)
        if i < 0 or i > 255:
            return False
    return True


print(validate_ip("127.0.0.1"))
print(validate_ip("192.0.1.255"))
print(validate_ip("192.1.0.256"))


def average_word_length(sentence):

    words = sentence.split()

    num_words = len(words)

    total_length = sum(len(word) for word in words)

    if num_words > 0:
        return total_length / num_words

    return 0


print(average_word_length("Calculate the average length of words in a sentence"))


def find_alphabet_with_most_neighbors(edges):

    graph = {}

    for edge in edges:
        u, v = edge[0], edge[1]
        if u not in graph:
            graph[u] = []
        if v not in graph:
            graph[v] = []
        graph[u].append(v)
        graph[v].append(u)  # Assuming the graph is undirected

    max_neighbors = -1
    alphabet_with_most_neighbors = None

    for alphabet, neighbors in graph.items():
        num_neighbors = len(neighbors)
        if num_neighbors > max_neighbors:
            max_neighbors = num_neighbors
            alphabet_with_most_neighbors = alphabet

    return alphabet_with_most_neighbors, max_neighbors


edges = [("A", "B"), ("A", "C"), ("B", "C"), ("B", "D"), ("C", "E")]
alphabet, num_neighbors = find_alphabet_with_most_neighbors(edges)
print(f"Alphabet '{alphabet}' has the most neighbors with {num_neighbors} neighbors.")
