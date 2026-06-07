# https://leetcode.com/problems/find-minimum-time-to-finish-all-jobs/


# TC: O(k^n), where n is the number of jobs and k is the number of workers.
# SC: O(k)
class Solution:
    def minimumTimeRequired(self, jobs: list[int], k: int) -> int:

        jobs.sort(reverse=True)
        workers = [0] * k

        self.ans = sum(jobs)

        def dfs(i):

            if i == len(jobs):
                self.ans = min(self.ans, max(workers))
                return

            seen = set()

            for w in range(k):

                # same load wale workers equivalent hain
                if workers[w] in seen:
                    continue

                # already answer se worse ho raha hai
                if workers[w] + jobs[i] >= self.ans:
                    continue

                seen.add(workers[w])

                workers[w] += jobs[i]
                dfs(i + 1)
                workers[w] -= jobs[i]

                # empty worker ko try karke wapas aa gaye
                # baaki empty workers bhi same hi honge
                if workers[w] == 0:
                    break

        dfs(0)

        return self.ans