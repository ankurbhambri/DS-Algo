'''
Design Hit Counter

Create a system that tracks the number of "clicks" received within the last 300 seconds (5 minutes).
Each method will receive a timestamp parameter (represented in seconds).

You can assume that for recordClick(), timestamps are always provided in increasing order.
However getRecentClicks() can be called for any timestamp. The earliest timestamp will always be 1.

Note that multiple clicks may be recorded at the same timestamp.

Examples:
ClickCounter tracker = new ClickCounter();

register a click at time 1
tracker.recordClick(1);

register a click at time 2
tracker.recordClick(2);

register a click at time 3
tracker.recordClick(3);

retrieve clicks at time 4, expect 3
tracker.getRecentClicks(4);

register a click at time 300
tracker.recordClick(300);

retrieve clicks at time 300, expect 4
tracker.getRecentClicks(300);

retrieve clicks at time 301, expect 3
tracker.getRecentClicks(301);

Constraints
- All timestamps are positive integers and start at 1.
- Timestamps are provided in a strictly increasing sequence.
- At most 10,000 operations will be performed.
- There may be multiple clicks at the same timestamp.

'''

# Approach 1: Circular Array — O(1) record, O(300) get — fixed memory
# Approach 2: Deque — O(1) amortized record, O(n) worst-case get

from collections import deque


# ======================== Approach 1: Circular Array (Optimal) ========================

class ClickCounter:
    """
    Uses two fixed-size arrays of length 300 (window_size).
    Each bucket stores the timestamp and hit count.
    Modulo maps timestamps to buckets; stale buckets are detected by comparing timestamps.
    
    Time:  record O(1), get O(window_size)
    Space: O(window_size) — constant
    """
    def __init__(self):
        self.window_size = 300
        self.times = [0] * self.window_size
        self.hits = [0] * self.window_size

    def record_click(self, timestamp: int) -> None:
        index = timestamp % self.window_size
        if self.times[index] != timestamp:
            # Bucket belongs to an older timestamp — reset it
            self.times[index] = timestamp
            self.hits[index] = 1
        else:
            self.hits[index] += 1

    def get_recent_clicks(self, timestamp: int) -> int:
        total = 0
        for i in range(self.window_size):
            if timestamp - self.times[i] < self.window_size:
                total += self.hits[i]
        return total


# ======================== Approach 2: Deque ========================

class ClickCounterDeque:
    """
    Stores each click as a timestamp in a deque.
    On get, pops expired entries from the front.
    
    Time:  record O(1), get O(n) worst case but amortized O(1) since each entry is popped at most once
    Space: O(n) — proportional to clicks in the window
    """
    def __init__(self):
        self.window_size = 300
        self.queue = deque()

    def record_click(self, timestamp: int) -> None:
        self.queue.append(timestamp)

    def get_recent_clicks(self, timestamp: int) -> int:
        while self.queue and timestamp - self.queue[0] >= self.window_size:
            self.queue.popleft()
        return len(self.queue)


# ======================== Tests ========================

if __name__ == "__main__":

    for name, cls in [("Circular Array", ClickCounter), ("Deque", ClickCounterDeque)]:
        t = cls()
        t.record_click(1)
        t.record_click(2)
        t.record_click(3)
        assert t.get_recent_clicks(4) == 3

        t.record_click(300)
        assert t.get_recent_clicks(300) == 4
        assert t.get_recent_clicks(301) == 3

        # Multiple clicks at same timestamp
        t2 = cls()
        t2.record_click(1)
        t2.record_click(1)
        t2.record_click(1)
        assert t2.get_recent_clicks(1) == 3
        assert t2.get_recent_clicks(300) == 3
        assert t2.get_recent_clicks(301) == 0

        print(f"{name}: All tests passed!")