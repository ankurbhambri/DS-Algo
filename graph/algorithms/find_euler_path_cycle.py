from collections import defaultdict


def find_euler_graph(graph, N):
    def dfs(node, visit):

        visit.add(node)

        for nei in graph[node]:

            if nei not in visit:

                dfs(nei, visit)

    def connect_component():

        visit = set()
        node = -1

        for i in range(N):
            if len(graph[i]) > 0:
                node = i
                break

        if node == -1:

            return True

        dfs(node, visit)

        for i in range(N):

            if not visit[i] and len(graph[i]) > 0:

                return False

        return True

    def find_euler(N):

        # if we having multi component graph there must be one component which having at-least one edge
        if not connect_component():
            return 0

        odd = 0

        for i in range(N):

            if len(graph[i]) & 1:
                odd += 1

        if odd > 2:
            return 0

        return 2 if odd == 0 else 1

    res = find_euler()

    if res == 0:
        print("Not Euler graph")

    elif res == 1:
        print("Semi Euler graph")

    else:
        print("Euler graph")


graph = defaultdict(list)

graph[1].append(0)
graph[0].append(2)
graph[2].append(1)
graph[0].append(3)
graph[3].append(4)
