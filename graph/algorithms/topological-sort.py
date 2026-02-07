""" 
- It sorts parents and child in correct ordering

- DAG - A directed graph with no cycle is called DAG.

- Topological sorting for Directed Acyclic Graph (DAG) is a linear ordering of 
  vertices such that for every directed edge u v, vertex u comes before v in the ordering.

- Topological Sorting for a graph is not possible if the graph is not a DAG(Direct Acyclic Graph).



"""

# TC: O(V + E) where V is the number of vertices and E is the number of edges in the graph.
# SC: O(V) for the recursion stack and the visited sets.
def topologicalSort(n, graph):
    adj = {c: [] for c in range(n)}

    for n1, n2 in graph:
        adj[n1].append(n2)

    res = []
    visit = cycle = set()

    def dfs(node):
        # if there is cycle means no possible to do topological sort
        if node in cycle:
            return True

        if node in visit:
            return False

        # First add in cycle then remove it.
        cycle.add(node)
        visit.add(node)

        for ch in adj[node]:
            if dfs(ch):
                return True

        cycle.remove(node)  # backtrack
        res.append(node)

        return False

    for cur in range(n):
        if dfs(cur):
            return []

    return res


print(topologicalSort(4, [[1, 0], [2, 0], [3, 1], [3, 2]]))


# Cycle Detection in Directed Graph using BFS(Kahn's Algorithm) indegree method
# TC: O(V + E) where V is the number of vertices and E is the number of edges in the graph.
# SC: O(V) for the queue and the indegree dictionary.
def khan_algo(graph):

    indegree = {i: 0 for i in graph}

    for i in range(len(graph)):  # need n here
        for node in graph[i]:
            indegree[node] += 1

    q = [i for i in range(len(graph)) if indegree[i] == 0]

    res = []
    while q:

        node = q.pop(0)
        res.append(node)

        for nei in adj[node]:
            indegree[nei] -= 1
            if indegree[nei] == 0:
                q.append(nei)

    return [] if len(res) != len(graph) else res # in case if result length is not equal to graph length, it means there is a cycle


adj = {0: [], 1: [], 2: [3], 3: [1], 4: [0, 1], 5: [0, 2]}
print(khan_algo(adj))

"""
Note:-
Topological sort is an algorithm that takes a directed acyclic graph (DAG) as 
input and produces a linear ordering of its vertices such that for every directed
edge uv from vertex u to vertex v, u comes before v in the ordering.

Kahn's algorithm, also known as the "topological sorting algorithm", is another
algorithm used to perform topological sorting of a DAG. It works by iteratively
removing nodes with no incoming edges and adding them to the sorted list until
all nodes have been processed.

In summary, Kahn's algorithm is one specific implementation of the topological
sort algorithm.
"""



# https://leetcode.com/problems/course-schedule/

def canFinish(n, prerequisites):

    indegree = {i: 0 for i in range(n)}
    adj = {i: [] for i in range(n)}

    for crs, pre in prerequisites:
        # [1, 0] 0 must be completed before 1 so this way we can make adj
        adj[pre].append(crs)
        indegree[crs] += 1  # no

    q = [i for i in range(n) if indegree[i] == 0]

    res = []
    while q:

        node = q.pop(0)
        res.append(node)

        for nei in adj[node]:
            indegree[nei] -= 1

            if indegree[nei] == 0:
                q.append(nei)

    return len(res) == n


# https://leetcode.com/problems/course-schedule-ii/

def findOrder(numCourses, prerequisites):

    indegree = {i: 0 for i in range(numCourses)}
    adj = {i: [] for i in range(numCourses)}

    for u, v in prerequisites:
        adj[u].append(v)
        indegree[v] += 1

    q = [i for i in range(numCourses) if indegree[i] == 0]

    res = []
    while q:

        node = q.pop(0)
        res.append(node)

        for nei in adj[node]:
            indegree[nei] -= 1

            if indegree[nei] == 0:
                q.append(nei)

    return res[::-1] if len(res) == numCourses else []  # reverse to get the last from first


# https://leetcode.com/problems/find-all-possible-recipes-from-given-supplies/description/

from collections import defaultdict, deque

class Solution:
    def findAllRecipes(recipes, ingredients, supplies):

        ingredient_count = defaultdict(int)
        dependency_graph = defaultdict(list)
        
        for recipe, required_ingredients in zip(recipes, ingredients):
            ingredient_count[recipe] = len(required_ingredients)
            for ingredient in required_ingredients:
                dependency_graph[ingredient].append(recipe)
        
        available_items = deque(supplies)
        available_recipes = set(recipes)
        prepared_recipes = []
        
        while available_items:
            item = available_items.popleft()
            
            if item in available_recipes:  
                prepared_recipes.append(item)
            
            for dependent_recipe in dependency_graph[item]:
                ingredient_count[dependent_recipe] -= 1
                if ingredient_count[dependent_recipe] == 0:
                    available_items.append(dependent_recipe)
        
        return prepared_recipes


'''
You want to run two tests on a device. Each test has a series of setup tests that must be done in order.

For example,
you need to complete Step A, B, and C in that order to run test1.
Then there is test2, which needs steps X, B, and Z to be setup in that order to run.

You could setup the device by doing the steps like this A, B, C, X, B Z. But that would be inefficient because you are doing step B twice. 
How would you make the list of steps such that there are no duplicate steps but the order of the steps is maintained. 

For example, in this case, the optimized correct steps are A, X, B, C,Z.
'''

def optimize_steps(tests):
    graph = defaultdict(set)
    indegree = defaultdict(int)

    # Build graph
    for test in tests:
        for i in range(len(test) - 1):
            u, v = test[i], test[i + 1]
            if v not in graph[u]:
                graph[u].add(v)
                indegree[v] += 1
            indegree[u] += 0

    # Topological sort
    queue = deque([s for s in indegree if indegree[s] == 0])
    result = []

    while queue:
        step = queue.popleft()
        result.append(step)
        for nxt in graph[step]:
            indegree[nxt] -= 1
            if indegree[nxt] == 0:
                queue.append(nxt)

    return result
tests = [
    ["A", "B", "C"],
    ["X", "B", "Z"]
]

print(optimize_steps(tests))