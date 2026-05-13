'''
Design a hit counter which counts the number of hits received in the past 5 minutes (i.e., the past 300 seconds).

Your system should accept a timestamp parameter (in seconds granularity), and you may assume that calls are being made to the system in chronological order 
(i.e., timestamp is monotonically increasing). Several hits may arrive roughly at the same time.

Implement the HitCounter class:

HitCounter() Initializes the object of the hit counter system.
void hit(int timestamp) Records a hit that happened at timestamp (in seconds). Several hits may happen at the same timestamp.
int getHits(int timestamp) Returns the number of hits in the past 5 minutes from timestamp (i.e., the past 300 seconds).
 

Example 1:

Input
["HitCounter", "hit", "hit", "hit", "getHits", "hit", "getHits", "getHits"]
[[], [1], [2], [3], [4], [300], [300], [301]]
Output
[null, null, null, null, 3, null, 4, 3]

Explanation
HitCounter hitCounter = new HitCounter();
hitCounter.hit(1);       // hit at timestamp 1.
hitCounter.hit(2);       // hit at timestamp 2.
hitCounter.hit(3);       // hit at timestamp 3.
hitCounter.getHits(4);   // get hits at timestamp 4, return 3.
hitCounter.hit(300);     // hit at timestamp 300.
hitCounter.getHits(300); // get hits at timestamp 300, return 4.
hitCounter.getHits(301); // get hits at timestamp 301, return 3.

Constraints:

1 <= timestamp <= 2 * 109
All the calls are being made to the system in chronological order (i.e., timestamp is monotonically increasing).
At most 300 calls will be made to hit and getHits.
 

Follow up: What if the number of hits per second could be huge? Does your design scale?

'''

# Binary search solution with O(log n) time complexity for getHits and O(1) for hit. Space complexity is O(n) where n is the number of hits recorded.

# TC: O(n log n)
# SC: O(n)
class HitCounter:

    def __init__(self):
        self.hits = []

    def hit(self, timestamp: int) -> None:
        if self.hits and self.hits[-1][0] == timestamp:
            self.hits[-1] = (timestamp, self.hits[-1][1] + 1)
        else:
            self.hits.append((timestamp, 1))

    def getHits(self, timestamp: int) -> int:

        lower_bound = timestamp - 299  # inclusive window

        # Binary search: first index with timestamp >= lower_bound
        left, right = 0, len(self.hits) - 1
        idx = len(self.hits)

        while left <= right:
            mid = (left + right) // 2
            if self.hits[mid][0] >= lower_bound:
                idx = mid
                right = mid - 1
            else:
                left = mid + 1

        # Sum from idx to end
        total_hits = 0
        for i in range(idx, len(self.hits)):
            total_hits += self.hits[i][1]

        return total_hits


hit_counter = HitCounter()
hit_counter.hit(1)
hit_counter.hit(2)
hit_counter.hit(3)
print(hit_counter.getHits(4))
hit_counter.hit(300)
print(hit_counter.getHits(300))
print(hit_counter.getHits(301))


# TC: O(1)
# SC: O(1)

# Bucketing
class HitCounter:
    def __init__(self):
        # 300 buckets for 300 seconds
        self.times = [0] * 300
        self.counts = [0] * 300

    def hit(self, timestamp: int) -> None:

        idx = timestamp % 300

        # If this bucket is from an old timestamp → overwrite
        if self.times[idx] != timestamp:
            self.times[idx] = timestamp
            self.counts[idx] = 1
        else:
            # Same timestamp → increment count
            self.counts[idx] += 1

    def getHits(self, timestamp: int) -> int:

        total_hits = 0

        for i in range(300):
            # Only count hits within last 300 seconds
            if timestamp - self.times[i] < 300:
                total_hits += self.counts[i]

        return total_hits


hit_counter = HitCounter()
hit_counter.hit(1)
hit_counter.hit(2)
hit_counter.hit(3)
print(hit_counter.getHits(4)) # Output: 3
hit_counter.hit(300)
print(hit_counter.getHits(300)) # Output: 4
print(hit_counter.getHits(301)) # Output: 3


# Variant: Given a class with methods like put_element(k), get_element_count(k) and get_total_elements(), 
# implement the above methods after initialising a custom counter class with expiry time of 't' seconds.

# TC: O(t)
# SC: O(t)

class ExpiringCounter:

    def __init__(self, t: int):
        self.t = t
        self.times = [0] * t
        # Each bucket is a dictionary to count occurrences of keys
        self.buckets = [{} for _ in range(t)]

    def put_element(self, key: str, timestamp: int) -> None:

        idx = timestamp % self.t

        # If bucket is stale → reset
        if self.times[idx] != timestamp:
            self.times[idx] = timestamp
            self.buckets[idx] = {}

        # Add/update key
        if key in self.buckets[idx]:
            self.buckets[idx][key] += 1
        else:
            self.buckets[idx][key] = 1

    def get_element_count(self, key: str, timestamp: int) -> int:

        total = 0
 
        for i in range(self.t):
            # Check if bucket is within valid window and specific key exists/count
            if timestamp - self.times[i] < self.t:
                total += self.buckets[i].get(key, 0)

        return total

    def get_total_elements(self, timestamp: int) -> int:

        total = 0

        for i in range(self.t):
            # Only count elements within valid window and all keys count
            if timestamp - self.times[i] < self.t:
                print(self.buckets[i].values())
                total += sum(self.buckets[i].values())

        return total


obj = ExpiringCounter(300)
obj.put_element("a", 1)
obj.put_element("a", 2)
obj.put_element("b", 2)
print(obj.get_element_count("a", 3))  # Output: 2
print(obj.get_element_count("b", 3))  # Output: 1
print(obj.get_total_elements(3))       # Output: 3