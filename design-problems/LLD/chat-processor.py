


'''
Chat logs processor

implement two methods
registerEvent(sender, receiver, timestamp)
getMostActiveUser()

Activeness is defined as number of chats with other users (at any moment)

Follow up:
- what if we need to return Top K active users
- what would we need to change

follow up 2
- what if registerEvent is called millions times a day and getMostActiveUser only once a day, what would change
'''

import heapq

class ChatProcessor:
    def __init__(self):
        self.user_chats = {}       # user -> set of unique partners
        self.active_count = {}     # user -> count (mirrors len of set)
        self.current_max_user = None

    # O(N)
    def registerEvent(self, sender: str, receiver: str, timestamp: int):
        for user, partner in [(sender, receiver), (receiver, sender)]:
            if user not in self.user_chats:
                self.user_chats[user] = set()
                self.active_count[user] = 0

            prev_size = len(self.user_chats[user])
            self.user_chats[user].add(partner)

            if len(self.user_chats[user]) > prev_size:  # genuinely new partner
                self.active_count[user] += 1
                if (self.current_max_user is None or self.active_count[user] > self.active_count[self.current_max_user]):
                    self.current_max_user = user
    # O(1)
    def getMostActiveUser(self) -> str:
        return self.current_max_user or ""

    # O(N log k)
    def getTopKActiveUsers(self, k: int) -> list:
        if not self.user_chats or k <= 0:
            return []

        min_heap = []
        for user, partners in self.user_chats.items():
            heapq.heappush(min_heap, (len(partners), user))
            if len(min_heap) > k:
                heapq.heappop(min_heap)

        # top_k = [heapq.heappop(min_heap)[1] for _ in range(len(min_heap))]
        top_k = [user for _, user in sorted(min_heap, reverse=True)]
        return top_k

processor = ChatProcessor()
processor.registerEvent("Abby", "Ben", 10)
processor.registerEvent("Abby", "Carla", 20)
processor.registerEvent("Ben", "Bob", 30)

print("Most Active User:", processor.getMostActiveUser())  # Output: Abby (2 unique partners)
print("Top 2 Active Users:", processor.getTopKActiveUsers(2))  # Output: ['Abby', 'Ben']