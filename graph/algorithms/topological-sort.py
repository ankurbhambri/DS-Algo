from collections import defaultdict, deque

############################### Kahn's Algorithm ###############################

# Cycle Detection in Directed Graph using BFS(Kahn's Algorithm) indegree method
# TC: O(V + E) where V is the number of vertices and E is the number of edges in the graph.
# SC: O(V) for the queue and the indegree dictionary.
def khan_algo(graph, n):

    adj = defaultdict(list)
    indegree = [0] * n

    for u, v in graph:
        adj[u].append(v)
        indegree[v] += 1

    # 2. Push all vertices with indegree 0 into the queue
    # (Nodes with 0 indegree have no dependencies/prerequisites)
    queue = deque([i for i in range(n) if indegree[i] == 0])

    res = []
    while queue:
        node = queue.popleft()
        res.append(node)

        for nei in adj[node]:
            # Decrease the indegree of all neighbors
            indegree[nei] -= 1

            # If indegree becomes 0, add it to the queue
            if indegree[nei] == 0:
                queue.append(nei)

    # If res doesn't include all vertices, there is a cycle!
    return res if len(res) == n else []


print(khan_algo([[0, 1], [1, 2], [2, 0]], n = 3))  # Output: [] (cycle detected) -> (0 -> 1 -> 2 -> 0)
print(khan_algo([[0, 1], [1, 2], [2, 3]], n = 4))  # Output: [0, 1, 2, 3] (valid topological order)


# https://leetcode.com/problems/course-schedule/
# https://leetcode.com/problems/course-schedule-ii/

class Solution:
    # def canFinish(numCourses, prerequisites): # part 1
    def findOrder(self, numCourses, prerequisites):

        indegree = [0] * numCourses
        adj = defaultdict(list)

        for crs, pre in prerequisites:
            adj[pre].append(crs)
            indegree[crs] += 1

        q = deque([i for i in range(numCourses) if indegree[i] == 0])

        res = []
        while q:
            node = q.popleft() # O(1) operation
            res.append(node)

            for nei in adj[node]:
                indegree[nei] -= 1

                if indegree[nei] == 0:
                    q.append(nei)

        # Course Schedule I: ke liye return len(res) == numCourses
        # Course Schedule II: ke liye return res if len(res) == numCourses else []
        return res if len(res) == numCourses else []


# https://leetcode.com/problems/find-all-possible-recipes-from-given-supplies/description/

# TC: O(R + I) where R is the number of recipes and I is the total number of ingredients across all recipes.
# SC: O(R + I) for the graph and the count dictionary.
class Solution:
    def findAllRecipes(self, recipes, ingredients, supplies):

        count = defaultdict(int)
        graph = defaultdict(list)

        for recipe, reqs in zip(recipes, ingredients):
            count[recipe] = len(reqs)
            for req in reqs:
                graph[req].append(recipe)

        q = deque(supplies)
        recipe_set = set(recipes)
        res = []

        while q:

            item = q.popleft()

            if item in recipe_set:  
                res.append(item)

            for r in graph[item]:
                count[r] -= 1
                if count[r] == 0:
                    q.append(r)

        return res


'''
You want to run two tests on a device. Each test has a series of setup tests that must be done in order.

For example,
you need to complete Step A, B, and C in that order to run test1.
Then there is test2, which needs steps X, B, and Z to be setup in that order to run.

You could setup the device by doing the steps like this A, B, C, X, B Z. But that would be inefficient because you are doing step B twice. 
How would you make the list of steps such that there are no duplicate steps but the order of the steps is maintained. 

For example, in this case, the optimized correct steps are A, X, B, C,Z.
'''

class Solution:
    def optimize_steps(self, tests):

        graph = defaultdict(set)
        indegree = defaultdict(int)

        # Build graph
        for test in tests:
            for i in range(len(test) - 1):

                u, v = test[i], test[i + 1]

                if v not in graph[u]:

                    graph[u].add(v)
                    indegree[v] += 1

        # Topological sort
        result = []
        queue = deque([s for s in indegree if indegree[s] == 0])

        while queue:
            step = queue.popleft()
            result.append(step)
            for nxt in graph[step]:
                indegree[nxt] -= 1
                if indegree[nxt] == 0:
                    queue.append(nxt)

        return result


print(Solution().optimize_steps([["A", "B", "C"], ["X", "B", "Z"]]))  # Output: ['A', 'X', 'B', 'C', 'Z']


# Must Problem: https://leetcode.com/problems/replace-all-s-to-avoid-consecutive-repeating-characters/

'''
You are given a replacements mapping and a text string that may contain
placeholders formatted as %var%, where each var corresponds to a key in the
replacements mapping. Each replacement value may itself contain one or more
such placeholders. Each placeholder is replaced by the value associated with
its corresponding replacement key. Return the fully substituted text string
which does not contain any placeholders.

Example 1:
    
    Input: replacements = [["A","abc"],["B","def"]], text = "%A%_%B%"

    Output: "abc_def"

    Explanation: The mapping associates "A" with "abc" and "B" with "def".
    Replace %A% with "abc" and %B% with "def" in the text.
    The final text becomes "abc_def".

Example 2:
    
    Input: replacements = [["A","bce"],["B","ace"],["C","abc%B%"]],
           text = "%A%_%B%_%C%"
    
    Output: "bce_ace_abcace"

    Explanation: The mapping associates "A" with "bce", "B" with "ace",
    and "C" with "abc%B%". Replace %A% with "bce" and %B% with "ace" in
    the text. Then, for %C%, substitute %B% in "abc%B%" with "ace" to
    obtain "abcace". The final text becomes "bce_ace_abcace".

Constraints:
    - 1 <= replacements.length <= 10
    - Each element of replacements is a two-element list [key, value]:
      * key is a single uppercase English letter
      * value is a non-empty string of at most 8 characters that may
        contain zero or more placeholders formatted as %<key>%
    - All replacement keys are unique
    - The text string is formed by concatenating all key placeholders
      (formatted as %<key>%) randomly from the replacements mapping,
      separated by underscores
    - text.length == 4 * replacements.length - 1
    - Every placeholder in the text or in any replacement value
      corresponds to a key in the replacements mapping
    - There are no cyclic dependencies between replacement keys
'''

import re
class Solution:
    def applySubstitutions(self, replacements: list[list[str]], text: str) -> str:

        mp = {k: v for k, v in replacements}

        adj = defaultdict(list)
        indegree = {k: 0 for k in mp}

        # Build DAG
        for key, val in replacements:

            deps = re.findall(r'%([A-Z])%', val)

            for dep in deps:
                adj[dep].append(key)
                indegree[key] += 1

        # Start with nodes having no dependencies
        q = deque([k for k in mp if indegree[k] == 0])

        resolved = {}

        while q:

            cur = q.popleft()

            # cur already has all placeholders resolved
            if cur not in resolved:
                resolved[cur] = mp[cur]

            for nxt in adj[cur]:

                # Replace all occurrences of %cur% in nxt
                resolved_val = resolved.get(nxt, mp[nxt]).replace(f"%{cur}%", resolved[cur])

                resolved[nxt] = resolved_val

                indegree[nxt] -= 1

                if indegree[nxt] == 0:
                    q.append(nxt)

        # Expand final text
        ans = text
        for k, v in resolved.items():
            ans = ans.replace(f"%{k}%", v)

        return ans


print(Solution().applySubstitutions([["A","abc"],["B","def"]], "%A%_%B%")) # "abc_def"
print(Solution().applySubstitutions([["A","bce"],["B","ace"],["C","abc%B%"]], "%A%_%B%_%C%")) # "bce_ace_abcace" 