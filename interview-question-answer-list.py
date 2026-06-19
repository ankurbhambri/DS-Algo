"""
Interview Question -> Answer Notes (Clean Version)

This file is a compact Q/A sheet made from your mixed notes.
For each question, the answer includes either:
1) a direct repo file where the solution already exists, or
2) a clean implementation in this file if it was custom.
"""

from __future__ import annotations

import bisect
import heapq
from collections import defaultdict, deque
from math import inf


QA_LIST = [
    {
        "question": "Jump game with odd-left/even-right rule and +X updates. Detect infinite loop.",
        "answer": "Use value->sorted-indices map + bisect for next jump, update map after each +X, and visited state (index, direction) for cycle detection.",
        "source": "Implemented below: jump_update",
    },
    {
        "question": "Given words + prefix, return all words starting with prefix.",
        "answer": "Build Trie, walk prefix node, DFS from that node to collect words.",
        "source": "Repo: trie/query-prefix.py",
    },
    {
        "question": "Task Scheduler (LC 621) + follow-up: multiple CPUs.",
        "answer": "Single CPU: max-heap simulation or greedy formula. Multi CPU follow-up: balance rounds using max frequency and number of max-frequency tasks.",
        "source": "Repo: hash-map/task-scheduler.py",
    },
    {
        "question": "Maximum area rectangle from points, with no extra points inside.",
        "answer": "Check diagonals/corners and validate interior constraints. For advanced constraints, use sweep-line + Fenwick tree.",
        "source": "Repo: maths/maximum-area-rectangle-with-point-constraints-i.py and maths/maximum-area-rectangle-with-point-constraints-ii.py",
    },
    {
        "question": "Ad serving system: return highest score ad, decrease score, avoid consecutive repeats, cooldown/gap.",
        "answer": "Use max-heap for active ads + queue for cooldown release by turn.",
        "source": "Implemented below: AdSystem",
    },
    {
        "question": "Lakes / closed regions in grid (including follow-up where boundaries matter).",
        "answer": "Use DFS flood fill. For closed components, DFS returns False when reaching boundary.",
        "source": "Implemented below: count_closed_lakes; Related repo: graph/problems/grid problems/number-of-islands.py",
    },
    {
        "question": "Earliest arrival between airports with depart/arrive times.",
        "answer": "Build adjacency by flights and run Dijkstra-like min-heap on current arrival time, only taking flights with depart >= current time.",
        "source": "Implemented below: earliest_arrival",
    },
    {
        "question": "Hidden n x n board with n-1 rooks; API countRook(a,b,c,d). Find missing row/column with fewer API calls.",
        "answer": "Binary search row and column independently using prefix rectangle counts.",
        "source": "Implemented below: find_missing_rook_position",
    },
    {
        "question": "LFU-like cache variant: evict only even-score entries.",
        "answer": "Maintain score buckets + eviction scanning only valid even-score buckets.",
        "source": "Repo: caching/lru-cache.py (LFUEvenCache)",
    },
    {
        "question": "Minimum time to finish jobs / scheduling style backtracking.",
        "answer": "Sort jobs descending + DFS assignment with pruning by seen worker loads and current best bound.",
        "source": "Repo: backtracking/find-minimum-time-to-finish-all-jobs.py",
    },
    {
        "question": "Minimum removals to make mountain array.",
        "answer": "LIS from left + LIS from right; keep valid peaks and maximize mountain length.",
        "source": "Repo: dynamic-programming/LIS/minimum-number-of-removals-to-make-mountain-array.py",
    },
]


def print_qa_list() -> None:
    for i, item in enumerate(QA_LIST, start=1):
        print(f"Q{i}: {item['question']}")
        print(f"A{i}: {item['answer']}")
        print(f"Source: {item['source']}")
        print("-" * 80)


# -----------------------------------------------------------------------------
# Q1 Answer: Jump Update Game
# -----------------------------------------------------------------------------
def jump_update(arr: list[int], s: int, x: int) -> int:
    """
    Start from index s.
    Odd move: jump to nearest left index where value == arr[s] + 1.
    Even move: jump to nearest right index where value == arr[s] + 1.
    After every jump, update previous position by +x.
    Return final index when no jump possible, or -1 if infinite loop.
    """
    direction = 0  # 0 = left (odd), 1 = right (even)

    value_to_indices: dict[int, list[int]] = {}
    for i, val in enumerate(arr):
        value_to_indices.setdefault(val, []).append(i)

    visited = set()

    while True:
        state = (s, direction)
        if state in visited:
            return -1
        visited.add(state)

        target = arr[s] + 1
        if target not in value_to_indices or not value_to_indices[target]:
            return s

        positions = value_to_indices[target]
        next_s = -1

        if direction == 0:
            i = bisect.bisect_left(positions, s)
            if i > 0:
                next_s = positions[i - 1]
        else:
            i = bisect.bisect_right(positions, s)
            if i < len(positions):
                next_s = positions[i]

        if next_s == -1:
            return s

        old_s = s
        old_val = arr[old_s]
        value_to_indices[old_val].remove(old_s)
        if not value_to_indices[old_val]:
            del value_to_indices[old_val]

        arr[old_s] += x
        new_val = arr[old_s]
        value_to_indices.setdefault(new_val, [])
        bisect.insort(value_to_indices[new_val], old_s)

        s = next_s
        direction = 1 - direction


# -----------------------------------------------------------------------------
# Q5 Answer: Ad System with cooldown gap
# -----------------------------------------------------------------------------
class AdSystem:
    """
    insert_ad(content, score): add ad.
    get_ad():
      - returns highest score ad currently available,
      - decreases score by 1,
      - re-enables it only after cooldown gap turns.
    """

    def __init__(self, gap: int):
        self.hp: list[tuple[int, str]] = []
        self.cooldown = deque()  # (available_turn, score, content)
        self.turn = 0
        self.gap = gap

    def insert_ad(self, content: str, score: int) -> None:
        heapq.heappush(self.hp, (-score, content))

    def get_ad(self) -> str:
        self.turn += 1

        while self.cooldown and self.turn >= self.cooldown[0][0]:
            _, score, content = self.cooldown.popleft()
            heapq.heappush(self.hp, (-score, content))

        if not self.hp:
            return "No Ad Available"

        neg_score, content = heapq.heappop(self.hp)
        score = -neg_score - 1

        if score > 0:
            available_turn = self.turn + self.gap + 1
            self.cooldown.append((available_turn, score, content))

        return content


# -----------------------------------------------------------------------------
# Q6 Answer: Closed lakes count (0=water, 1=land)
# -----------------------------------------------------------------------------
def count_closed_lakes(grid: list[list[int]]) -> int:
    rows, cols = len(grid), len(grid[0])

    def dfs(r: int, c: int) -> bool:
        if r < 0 or r >= rows or c < 0 or c >= cols:
            return False
        if grid[r][c] != 0:
            return True

        grid[r][c] = 2

        left = dfs(r, c - 1)
        right = dfs(r, c + 1)
        up = dfs(r - 1, c)
        down = dfs(r + 1, c)

        return left and right and up and down

    count = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 0 and dfs(r, c):
                count += 1

    return count


# -----------------------------------------------------------------------------
# Q7 Answer: Earliest arrival in timed flights
# -----------------------------------------------------------------------------
def earliest_arrival(flights: list[tuple[str, str, int, int]], src: str, dst: str) -> int:
    graph = defaultdict(list)
    for u, v, depart, arrive in flights:
        graph[u].append((v, depart, arrive))

    pq = [(0, src)]  # (arrival_time, airport)
    best = defaultdict(lambda: inf)
    best[src] = 0

    while pq:
        cur_time, airport = heapq.heappop(pq)

        if airport == dst:
            return cur_time

        if cur_time > best[airport]:
            continue

        for nxt, depart, arrive in graph[airport]:
            if depart >= cur_time and arrive < best[nxt]:
                best[nxt] = arrive
                heapq.heappush(pq, (arrive, nxt))

    return -1


# -----------------------------------------------------------------------------
# Q8 Answer: Missing rook row/column via API countRook
# -----------------------------------------------------------------------------
def find_missing_rook_position(n: int, countRook) -> list[int]:
    """
    countRook(a, b, c, d) returns count of rooks inside rectangle:
      rows [a..c], cols [b..d], 1-indexed.
    There are n-1 rooks with unique rows/cols. Return [missing_row, missing_col].
    """

    l, r = 1, n
    while l < r:
        mid = (l + r) // 2
        if countRook(1, 1, mid, n) == mid:
            l = mid + 1
        else:
            r = mid
    missing_row = l

    l, r = 1, n
    while l < r:
        mid = (l + r) // 2
        if countRook(1, 1, n, mid) == mid:
            l = mid + 1
        else:
            r = mid
    missing_col = l

    return [missing_row, missing_col]


if __name__ == "__main__":
    print_qa_list()

    print("Jump Game Demo:", jump_update([3, 4, 2, 2, 7], 2, 4))
    print("Jump Game Demo:", jump_update([2, 1], 1, 2))

    ads = AdSystem(gap=1)
    ads.insert_ad("A", 3)
    ads.insert_ad("B", 2)
    print("Ad Demo:", ads.get_ad())
    print("Ad Demo:", ads.get_ad())
    print("Ad Demo:", ads.get_ad())
