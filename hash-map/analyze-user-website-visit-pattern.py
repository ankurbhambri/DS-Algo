"""
# https://leetcode.com/problems/analyze-user-website-visit-pattern/

You are given two string arrays, username and website, and an integer array, timestamp.
All the given arrays are of the same length, and the tuple [username[i], website[i], timestamp[i]] 
indicates that the user username[i] visited the website website[i] at time timestamp[i].

A pattern is a list of three websites (not necessarily distinct).
    - For example: ["home", "away", "love"], ["leetcode", "love", "leetcode"], and ["luffy", "luffy", "luffy"] are all patterns.

The score of a pattern is the number of users that visited all the websites in the pattern in the same order they appeared in the pattern.
    - For example, if the pattern is ["home", "away", "love"], the score is the number of users x such that x visited "home", then "away", then "love" in order.
    - Similarly, if the pattern is ["leetcode", "love", "leetcode"], the score is the number of users x such that x visited "leetcode", then "love", then "leetcode" again in order.
    - Also, if the pattern is ["luffy", "luffy", "luffy"], the score is the number of users x such that x visited "luffy" three different times at different timestamps.

Return the pattern with the largest score. If there is more than one pattern with the same largest score, return the lexicographically smallest such pattern.

Example 1:

Input: 
    
    username  = ["joe", "joe", "joe", "james", "james", "james", "james", "mary", "mary", "mary"]
    timestamp = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    website   = ["home", "about", "career", "home", "cart", "maps", "home", "home", "about", "career"]

Output: ["home", "about", "career"]

Explanation:
    The tuples in this example are: 

        ["joe", "home", 1], ["joe", "about", 2], ["joe", "career", 3],

        ["james", "home", 4], ["james", "cart", 5], ["james", "maps", 6], ["james", "home", 7],

        ["mary", "home", 8], ["mary", "about", 9], ["mary", "career", 10]

    The pattern ("home", "about", "career") has score 2 (joe and mary).
    The pattern ("home", "cart", "maps") has score 1 (james).
    The pattern ("home", "cart", "home") has score 1 (james).
    The pattern ("home", "maps", "home") has score 1 (james).
    The pattern ("cart", "maps", "home") has score 1 (james).
    The pattern ("home", "home", "home") has score 0 (no user visited home 3 times).

Example 2:

    Input: 

        username  = ["ua", "ua", "ua", "ub", "ub", "ub"]
        timestamp = [1, 2, 3, 4, 5, 6]
        website   = ["a", "b", "a", "a", "b", "c"]

    Output: ["a", "b", "a"]

Constraints:
    - 3 < username.length <= 50
    - 1 <= username[i].length <= 10
    - timestamp.length = username.length

"""

from collections import defaultdict

'''
Time Complexity Analysis:

    O(n log n) — sorting

    O(n) — user-to-site mapping

    O(u * m³) — generating 3-sequences and counting users per pattern

    → Final Time Complexity: O(n log n + u * m³)

Space Complexity Analysis:

    data → O(n)

    user_webs → O(n) (at most one site per timestamp per user)

    pattern_users → O(u * m³) in worst case (all unique patterns)

    res in combinations → O(m³)

    → Final Space Complexity: O(n + u * m³)

'''

# TC: O(n log n + u * m³)
# SC: O(n + u * m³)

class Solution:
    def mostVisitedPattern(self, username, timestamp, website):

        # Step 1: Combine and sort the visit records by timestamp
        data = sorted(zip(timestamp, username, website))

        # Step 2: Build user -> list of websites visited in time order
        user_webs = defaultdict(list)
        for _, user, site in data:
            user_webs[user].append(site)

        # Step 3: Build a counter for all 3-sequence patterns with unique users
        pattern_users = defaultdict(set)  # pattern -> set of users

        # Instead of using itertools.combinations or nested loops, we can define a recursive helper function to generate combinations.
        # And this can be extended for any k-sequence pattern generation.
        '''
        Input: sites = ["a", "b", "c", "d"] and k = 2

        dfs(0, []) # start = 0
        ├─ dfs(1, ["a"])      
        │  ├─ dfs(2, ["a", "b"]) → add ('a', 'b')
        │  ├─ dfs(3, ["a", "c"]) → add ('a', 'c')
        │  └─ dfs(4, ["a", "d"]) → add ('a', 'd')
        ├─ dfs(2, ["b"])
        │  ├─ dfs(3, ["b", "c"]) → add ('b', 'c')
        │  └─ dfs(4, ["b", "d"]) → add ('b', 'd')
        ├─ dfs(3, ["c"])
        │  └─ dfs(4, ["c", "d"]) → add ('c', 'd')

        O/P: [('a', 'b'), ('a', 'c'), ('a', 'd'), ('b', 'c'), ('b', 'd'), ('c', 'd')]

        '''
        def generate_combinations(sites, k):

            res = []

            def dfs(start, path):

                if len(path) == k:
                    res.append(tuple(path))
                    return

                for i in range(start, len(sites)):
                    path.append(sites[i])
                    dfs(i + 1, path)
                    path.pop() # backtrack to try next site

            dfs(0, [])
            return res

        for user, sites in user_webs.items():

            # Get all 3-sequence combinations from user's site history
            if len(sites) < 3:
                continue

            # Use set to avoid duplicate patterns for same user
            patterns = generate_combinations(sites, 3)

            for pattern in patterns:
                pattern_users[pattern].add(user)

        # Step 4: Find the 3-sequence visited by most users, tie -> lex smallest
        max_count = 0
        result = tuple()

        for pattern, users in pattern_users.items():

            if len(users) > max_count or (len(users) == max_count and pattern < result):

                max_count = len(users)
                result = pattern

        return list(result)


print(Solution().mostVisitedPattern(
    ["joe", "joe", "joe", "james", "james", "james", "james", "mary", "mary", "mary"],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    ["home", "about", "career", "home", "cart", "maps", "home", "home", "about", "career"]
))  # Output: ["home", "about", "career"]

print(Solution().mostVisitedPattern(
    ["ua", "ua", "ua", "ub", "ub", "ub"],
    [1, 2, 3, 4, 5, 6],
    ["a", "b", "a", "a", "b", "c"]
))  # Output: ["a", "b", "a"]


'''
Follow-up Questions You Might Get:

    What if instead of 3-sequence, we want the most frequent k-sequence?

        Generalize the logic using combinations(sites, k).

    What if websites can repeat, and we need consecutive 3 visits?

        Use a sliding window instead of combinations.
'''

'''
Similar 

You are given a log of website requests, where each log entry includes three pieces of information: the time of the request,
the customer ID, and the page visited. Each entry represents a page request made by a customer at a given time.
Your task is to write an algorithm to identify the most frequently visited sequence of three consecutive pages by any customer.
If there is a tie (multiple sequences with the same highest frequency), return the lexicographically smallest sequence.

Example:
Consider the following log entries:

T0,C1,A
T0,C2,E
T1,C1,B
T1,C2,B
T2,C1,C
T2,C2,C
T3,C1,D
T3,C2,D
T4,C1,E
T5,C2,A

From these entries, you can see there are two customers, C1 and C2. Customer C1 visited the pages in the order A -> B -> C -> D -> E, and customer C2 visited the pages in the order E -> B -> C -> D -> A.

Output:
Your algorithm should determine the most frequently visited three-page sequence across all customers. If there is more than one sequence with the highest frequency, return the lexicographically smallest sequence.
For the example above, the output should be the sequence (B, C, D), as it is visited by both customers.

Constraints:
The log file will have at least three entries.
Each customer will visit at least three different pages.
This problem requires parsing the data, analyzing patterns of page visits, and applying sorting and counting algorithms to identify the correct sequence.

link - https://leetcode.com/discuss/interview-question/5165222/Amazon-or-SDE-II-or-Help-me-solve-this-Amazon-Onsite-Interview-Question

'''

from collections import defaultdict, Counter

class Solution2:
    def mostVisitedPattern(self, data: str, k: int):
        timestamp, username, website = [], [], []

        for line in data.strip().split('\n'):
            t, u, w = line.strip().split(',')
            timestamp.append(int(t[1:]))  # convert "T0" → 0
            username.append(u.strip())
            website.append(w.strip())

        # Step 1: Combine and sort the visit records by timestamp
        records = sorted(zip(timestamp, username, website))

        # Step 2: Group website visits per user in timestamp order
        user_webs = defaultdict(list)
        for _, user, site in records:
            user_webs[user].append(site)

        # Step 3: Count all k-length consecutive patterns per user
        pattern_counter = Counter()

        for user, sites in user_webs.items():
            if len(sites) < k:
                continue
            seen = set()
            for i in range(len(sites) - k + 1):
                pattern = tuple(sites[i: i + k])
                if pattern not in seen:  # avoid duplicate patterns for same user
                    pattern_counter[pattern] += 1
                    seen.add(pattern)

        # Step 4: Get the most frequent pattern (lex smallest on tie)
        max_count = 0
        result = tuple()
        for pattern, count in pattern_counter.items():
            if count > max_count or (count == max_count and pattern < result):
                max_count = count
                result = pattern

        return list(result)

# Test
input_data = '''
    T0,C1,A
    T0,C2,E
    T1,C1,B
    T1,C2,B
    T2,C1,C
    T2,C2,C
    T3,C1,D
    T3,C2,D
    T4,C1,E
    T5,C2,A
'''

print(Solution2().mostVisitedPattern(input_data, 3))  # Expected: ['B', 'C', 'D']


# Note: Difference in above code is that it asks for combinations and in second one it uses consecutive k-length patterns.
