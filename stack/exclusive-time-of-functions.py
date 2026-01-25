# https://leetcode.com/problems/exclusive-time-of-functions/description/

from collections import deque

class Solution:
    def exclusiveTime(self, n: int, logs):

        res, st, prev = [0] * n, deque(), 0

        for log in logs:

            id, type, time = log.split(":")
            id, time = int(id), int(time)

            if type == "start":
                if st:
                    res[st[-1]] += time - prev
                st.append(id)
                prev = time

            else:
                res[st.pop()] += time - prev + 1
                prev = time + 1

        return res


print(Solution().exclusiveTime(2, ["0:start:0", "1:start:2", "1:end:5", "0:end:6"]))
print(Solution().exclusiveTime(1, ["0:start:0","0:start:2","0:end:5","0:start:6","0:end:6","0:end:7"]))