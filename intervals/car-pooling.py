# https://leetcode.com/problems/car-pooling/

class Solution:
    def carPooling(self, trips, capacity: int) -> bool:

        delta = []

        for p, u, v in trips:
            delta.append((u, p))
            delta.append((v, -p))

        for _, p in sorted(delta):
            capacity -= p
            if capacity < 0:
                return False
        return True

print(Solution().carPooling([[2, 1, 5], [3, 3, 7]], 4))  # False
print(Solution().carPooling([[2, 1, 5], [3, 3, 7]], 5))  # True

# Similar problem statement

'''
    Given a set of jobs array and max number of cpus, where each job object contains 3 props {starttime,duration,numberofCpusNeeded},
    Write a function which returns true if the jobs can be executed with the given max cpus else return false even if one job can't be executed?
'''

def canExecuteJobs(jobs, maxCpus):

    events = []

    for job in jobs:

        start = job['starttime']
        end = job['starttime'] + job['duration']
        cpus = job['numberofCpusNeeded']

        events.append((start, cpus))
        events.append((end, -cpus))

    events.sort()

    current_cpu_usage = 0
    for _, cpu_change in events:
        current_cpu_usage += cpu_change

        if current_cpu_usage > maxCpus:
            return False
        
    return True

print(canExecuteJobs(
    [
        {'starttime': 1, 'duration': 4, 'numberofCpusNeeded': 2},
        {'starttime': 2, 'duration': 3, 'numberofCpusNeeded': 1},
        {'starttime': 5, 'duration': 2, 'numberofCpusNeeded': 2}
    ],
    3
))  # True