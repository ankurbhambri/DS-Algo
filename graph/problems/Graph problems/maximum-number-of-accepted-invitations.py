# https://leetcode.com/problems/maximum-number-of-accepted-invitations

# Explanation - https://algo.monster/liteproblems/1820

# Here we will use Hungarian algorithm to find the maximum matching in a bipartite graph.


class Solution:
    def maximumInvitations(self, grid: list[list[int]]) -> int:

        m, n = len(grid), len(grid[0])

        # girl_match[j] = which boy currently owns girl j
        girl_match = [-1] * n

        def dfs(boy):

            for girl in range(n):

                if grid[boy][girl] == 0:
                    continue

                if girl in visited:
                    continue

                visited.add(girl)

                # girl free
                if girl_match[girl] == -1:
                    girl_match[girl] = boy
                    return True

                # try to relocate current owner
                if dfs(girl_match[girl]):
                    girl_match[girl] = boy
                    return True

            return False

        ans = 0

        for boy in range(m):

            # this will reset in every iteration as we want to find a new match for each boy.
            visited = set()

            if dfs(boy):
                ans += 1

        return ans


print(Solution().maximumInvitations([[1, 1, 0], [1, 0, 1], [0, 0, 1]]))  # Output: 3
print(Solution().maximumInvitations([[1, 0, 0], [1, 0, 0], [0, 1, 1]]))  # Output: 2


# Variant
'''
questions: [
    {id: 1, tags: ["MAC", "VSCODE"]},
    {id: 2, tags: ["PY", "AI"]},
    {id: 3, tags: ["JAVA", "OS"]},
    {id: 4, tags: ["PY", "NW"]}
]

Volunteer: [
    {id: 1, tags: ["PY","NW"], name: "A"},
    {id: 2, tags: ["AI"], name: "B"},
    {id: 3, tags: ["JAVA","NW"], name: "C"},
    {id: 4, tags: ["JAVA","NW"], name: "D"}
]

Assign question to volunteers such that each question is assigned to at most one volunteer based on tags match.
One volunteer can take at most one question and maximise the question assigned to volunteer.

for this example
    A can take question 4(PY match)
    B can take question 2(AI match)
    C can take question 3(Java match)

Question one no one can take as not match.
'''

def max_assignment(questions, volunteers):

    m = len(questions)
    n = len(volunteers)

    graph = [[] for _ in range(m)]

    # Build bipartite graph
    for i, q in enumerate(questions):

        for j, v in enumerate(volunteers):
            
            # agar intersection of tages mein kuch bhi common hai to edge banao
            if set(q["tags"]) & set(v["tags"]):

                graph[i].append(j)

    volunteer_match = [-1] * n

    def dfs(question):

        for volunteer in graph[question]:

            # If volunteer is already visited in this iteration, skip to avoid cycles
            if volunteer in visited:
                continue

            # Mark volunteer as visited for this iteration
            visited.add(volunteer)

            # volunteer is free
            if volunteer_match[volunteer] == -1:
                volunteer_match[volunteer] = question
                return True

            # try to relocate current owner
            if dfs(volunteer_match[volunteer]):
                volunteer_match[volunteer] = question
                return True

        return False

    ans = 0

    for question in range(m):

        visited = set()

        if dfs(question):
            ans += 1

    return ans


print(max_assignment(
    # questions
    [{"id": 1, "tags": ["MAC", "VSCODE"]},
     {"id": 2, "tags": ["PY", "AI"]},
     {"id": 3, "tags": ["JAVA", "OS"]},
     {"id": 4, "tags": ["PY", "NW"]}],
    # volunteers
    [{"id": 1, "tags": ["PY", "NW"], "name": "A"},
     {"id": 2, "tags": ["AI"], "name": "B"},
     {"id": 3, "tags": ["JAVA", "NW"], "name": "C"},
     {"id": 4, "tags": ["JAVA", "NW"], "name": "D"}]
))  # Output: 3