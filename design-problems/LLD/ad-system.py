'''

Given APIs:

- insertAd(string content, int score)

- getAd()

Requirements:

    getAd() should always return the highest scored ad

    After returning an ad, decrease its score

    Consecutive same ads should not appear

    Follow-up: Introduce a cooldown/gap before the same ad can appear again while keeping operations close to O(1).

'''

import heapq
from collections import deque

# TC: O(log n) for insert_ad, O(log n) for get_ad
# SC: O(n) for storing ads in heap and cooldown queue
class AdSystem:
    def __init__(self, gap: int):

        self.hp = []
        # Cooldown queue store karega: (available_at_turn, score, content)
        self.q = deque()
        self.turn = 0
        self.gap = gap

    def insert_ad(self, content: str, score: int):
        # Max-heap behave karne ke liye score ko negative kiya
        heapq.heappush(self.hp, (-score, content))

    def get_ad(self) -> str:

        self.turn += 1

        # Step A: Cooldown queue check karo. Agar kisi ad ka rest time poora ho gaya hai,
        # toh use wapas main_heap mein daal do.
        while self.q and self.turn >= self.q[0][0]:
            _, score, content = self.q.popleft()
            heapq.heappush(self.hp, (-score, content))

        # Step B: Agar koi ad available nahi hai
        if not self.hp:
            return "No Ad Available"

        # Step C: Highest score wala ad nikaalo
        score, content = heapq.heappop(self.hp)
        current_score = -score  # score ko wapas positive kiya

        # Step D: Score ko decrease karo
        current_score -= 1

        # Step E: Agar score abhi bhi 0 se bada hai, toh cooldown queue mein daalo
        if current_score > 0:
            available_at_turn = self.turn + self.gap + 1
            self.q.append((available_at_turn, current_score, content))

        return content
