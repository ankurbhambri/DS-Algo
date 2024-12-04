"""
You are given a log of website requests, where each log entry includes three pieces of information: the time of the request,
the customer ID, and the page visited. Each entry represents a page request made by a customer at a given time.
Your task is to write an algorithm to identify the most frequently visited sequence of three consecutive pages by any customer.
If there is a tie (multiple sequences with the same highest frequency), return the lexicographically smallest sequence.

Example:
Consider the following log entries:

mathematica
Copy code

T0,C1,A
T0,C2,E
T1,C1,B
T1,C2,B
T2,C1,C
T2,C2,C
T3,C1,D
T3,C2,D
T4,C1,E
T5,C2,A

From these entries, you can see there are two customers, C1 and C2. Customer C1 visited the pages in the order A -> B -> C -> D -> E, and customer C2 visited the pages in the order E -> B -> C -> D -> A.

Output:
Your algorithm should determine the most frequently visited three-page sequence across all customers. If there is more than one sequence with the highest frequency, return the lexicographically smallest sequence.
For the example above, the output should be the sequence (B, C, D), as it is visited by both customers.

Constraints:
The log file will have at least three entries.
Each customer will visit at least three different pages.
This problem requires parsing the data, analyzing patterns of page visits, and applying sorting and counting algorithms to identify the correct sequence.

link - https://leetcode.com/discuss/interview-question/5165222/Amazon-or-SDE-II-or-Help-me-solve-this-Amazon-Onsite-Interview-Question

"""

import heapq


def solution(arr):
    customer_seq = {j: [] for _, j, _ in arr}
    pattern_freq = {}

    for i, j, k in arr:
        customer_seq[j].append(k)

    win_size = 3
    for k, v in customer_seq.items():

        for i in range(len(v) - win_size):

            w = v[i : i + win_size]

            pattern_freq[tuple(w)] = 1 + pattern_freq.get(tuple(w), 0)

    # heap to get data based on "frequency" and "lexicographically smallest sequence"
    def get_top_sequence(sequences):
        heap = []

        for sequence, frequency in sequences.items():

            heapq.heappush(heap, (-frequency, sequence))

        return heapq.heappop(heap)[1]

    return get_top_sequence(pattern_freq)


arr = [
    ("T0", "C1", "A"),
    ("T0", "C2", "E"),
    ("T1", "C1", "B"),
    ("T1", "C2", "B"),
    ("T2", "C1", "C"),
    ("T2", "C2", "C"),
    ("T3", "C1", "D"),
    ("T3", "C2", "D"),
    ("T4", "C1", "E"),
    ("T5", "C2", "A"),
]

print(solution(arr))

# TC - O(N log N) - Because we are iterating sequence N time and using heap to sort in Log N time.
# Space - O(N^2 + N), Two dictionaries N ^ 2 and heap O(N).
