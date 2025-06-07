# https://leetcode.com/problems/time-based-key-value-store/

class TimeMap:
    def __init__(self):
        self.hashMap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hashMap:
            self.hashMap[key] = []
        self.hashMap[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:

        res = ""

        objs = self.hashMap.get(key, [])

        l, r = 0, len(objs) - 1

        # binary search
        while l <= r:

            mid = (r + l) // 2

            if objs[mid][1] <= timestamp:

                res = objs[mid][0]

                l = mid + 1

            else:
                r = mid - 1

        return res
