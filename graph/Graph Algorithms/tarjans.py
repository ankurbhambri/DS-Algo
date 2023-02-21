# Python program to find strongly connected components in a given
# directed graph using Tarjan's algorithm (single DFS)
# Complexity : O(V+E)

from collections import defaultdict

# This class represents an directed graph
# using adjacency list representation


class Solution:
    def __init__(self, vertices):
        # No. of vertices
        self.V = vertices

        # default dictionary to store graph
        self.graph = defaultdict(list)

        self.Time = 0

    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)

    '''A recursive function that find finds and prints strongly connected
	components using DFS traversal
	u --> The vertex to be visited next
	disc[] --> Stores discovery times of visited vertices
	low[] -- >> earliest visited vertex (the vertex with minimum
				discovery time) that can be reached from subtree
				rooted with current vertex
	st -- >> To store all the connected ancestors (could be part
		of SCC)
	visited[] --> bit/index array for faster check whether
				a node is in stack
	'''

    def dfs(self, u, low, disc, visited, st):

        disc[u] = self.Time
        low[u] = self.Time
        self.Time += 1
        visited.add(u)
        st.append(u)

        for v in self.graph[u]:

            # If v is not visited yet, then recur for it
            if disc[v] == -1:
                self.dfs(v, low, disc, visited, st)

                # Check if the subtree rooted with v has a connection to
                # one of the ancestors of u
                # Case 1 (per above discussion on Disc and Low value)
                low[u] = min(low[u], low[v])

            elif v in visited:

                '''Update low value of 'u' only if 'v' is still in stack
                (i.e. it's a back edge, not cross edge).
                Case 2 (per above discussion on Disc and Low value)'''
                low[u] = min(low[u], disc[v])

        # head node found, pop the stack and print an SCC
        w = -1  # To store stack extracted vertices
        if low[u] == disc[u]:
            while w != u:
                w = st.pop()
                print(w, end=" ")
                visited.remove(w)

            print()

    # The function to do DFS traversal.
    # It uses recursive dfs()

    def SCC(self):

        # Mark all the vertices as not visited
        # and Initialize parent and visited,
        # and ap(articulation point) arrays
        disc = [-1] * (self.V)
        low = [-1] * (self.V)
        visited = set()
        st = []

        # Call the recursive helper function
        # to find articulation points
        # in DFS tree rooted with vertex 'i'
        for i in range(self.V):
            if disc[i] == -1:
                self.dfs(i, low, disc, visited, st)


obj = Solution(7)
obj.addEdge(0, 1)
obj.addEdge(1, 2)
obj.addEdge(1, 3)
obj.addEdge(3, 4)
obj.addEdge(4, 0)
obj.addEdge(4, 5)
obj.addEdge(4, 6)
obj.addEdge(5, 6)
obj.addEdge(6, 5)
print("SSC in second graph :")
obj.SCC()
