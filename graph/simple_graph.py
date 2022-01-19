from collections import defaultdict, deque


class DirectedGraph:

    adj = defaultdict(list)

    def addEdges(self, graph):

        for n1, n2 in graph:
            self.adj[n1].append(n2)

        return self.adj

    def checkCycle_DFS(self, node):

        visit = set()

        def dfs(node):

            if node in visit:
                return True

            visit.add(node)

            for i in self.adj[node]:
                if dfs(i):
                    return True
            return False

        return 'Cycle' if dfs(node) else 'No Cycle'

    def checkCycle_BFS(self, node):

        visit = set()
        q = deque()
        q.append(node)

        while q:

            cur = q.popleft()

            if cur in visit:
                return "cycle"

            for i in self.adj[cur]:
                q.append(i)
                visit.add(cur)

        return "No Cycle"

    # Size from a node to it's child


obj = DirectedGraph()

print(obj.addEdges([[0, 1], [0, 2], [1, 3], [0, 1]]))
# print(obj.checkCycle_DFS(0))
# print(obj.checkCycle_BFS(0))
print(obj.addEdges([[0, 1], [1, 0]]))
# print(obj.checkCycle_DFS(1))
# print(obj.checkCycle_BFS(1))
