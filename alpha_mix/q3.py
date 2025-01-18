'''
You are given a list of tuples where each tuple represents a chat message in the form (username, word_count). Each tuple indicates the number of words spoken by a user in a single message. Your task is to identify the top N most talkative users based on their total word counts.

Write a function TalkTalkativeUsers that takes:

A list of tuples user_word_counts where each tuple is (username, word_count).
An integer N, the number of most talkative users to return.
The function should return a list of N tuples sorted in descending order of word counts. Each tuple in the result should be (username, total_word_count).

Constraints:
The input list user_word_counts may contain millions of messages.
The number of unique users 
𝑘
k could be very large.
The function should be optimized to avoid sorting the entire dataset if only the top N users are needed.
The result should be sorted by total word count in descending order.

'''

# TC: O(m + klogn) - where m is the length of user_word_counts, k unique users and n is the size of the heap.


from collections import defaultdict
import heapq

def TalkTalkativeUsers(user_word_counts, n):
    """
    Identifies the top N most talkative users based on their total word counts.

    Args:
    user_word_counts (list of tuples): A list of (username, word_count) tuples.
    n (int): The number of top users to return.

    Returns:
    list of tuples: A list of the top N users and their word counts, sorted in descending order.
    """
    # Step 1: Aggregate word counts for each user
    total_word_counts = defaultdict(int)
    for user, word_count in user_word_counts:
        total_word_counts[user] += word_count  # O(len(user_word_counts))

    # Step 2: Use a min-heap to track the top N users
    heap = []  # Min-heap to store top N users
    for user, word_count in total_word_counts.items():  # O(k), where k is the number of unique users
        heapq.heappush(heap, (word_count, user))  # Push the current user into the heap
        if len(heap) > n:  # If the heap exceeds size n, remove the smallest element
            heapq.heappop(heap)  # O(log n)

    # Step 3: Sort the heap in descending order to prepare the result
    top_users = sorted(heap, key=lambda x: x[0], reverse=True)  # O(n log n), where n is the heap size

    # Step 4: Convert (word_count, user) back to (user, word_count) for readability
    return [(user, word_count) for word_count, user in top_users]


user_word_counts = [
    ('Joan', 1), ('Maria', 1), ('Joan', 5), ('Maria', 2), 
    ('Alex', 10), ('Joan', 2), ('Alex', 4), ('Bob', 12),
    ('Charlie', 8), ('Daisy', 3), ('Eva', 15), ('Frank', 2)
]
n = 3

top_users = TalkTalkativeUsers(user_word_counts, n)
print(top_users)
