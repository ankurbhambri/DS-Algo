# https://pkg.go.dev/github.com/lee-hen/Algoexpert/very_hard/22_airport_connections#section-readme


def airportConnections(airports, routes, startingAirport):
    def createGraph():
        graph = {
            airport: {"connections": [], "reachable": True, "unreachable": []}
            for airport in airports
        }
        for route in routes:
            airport, connection = route
            graph[airport]["connections"].append(connection)
        return graph

    def getUnreachableNodes(graph, start):
        visited = set()

        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for conn in graph[node]["connections"]:
                dfs(conn)

        dfs(start)
        return [node for node in airports if node not in visited]

    def markUnreachable(graph, unreachableNodes):
        def dfs_unreachable(node):
            if graph[node]["reachable"]:
                return
            if node in visited:
                return
            visited.add(node)
            unreachable.append(node)
            for conn in graph[node]["connections"]:
                dfs_unreachable(conn)

        for node in unreachableNodes:
            unreachable = []
            visited = set()
            dfs_unreachable(node)
            graph[node]["unreachable"] = unreachable

    def minNewConnections(unreachableNodes):
        unreachableNodes.sort(
            key=lambda node: len(graph[node]["unreachable"]), reverse=True
        )
        newConnections = 0
        for node in unreachableNodes:
            if graph[node]["reachable"]:
                continue
            newConnections += 1
            for conn in graph[node]["unreachable"]:
                graph[conn]["reachable"] = True
        return newConnections

    graph = createGraph()
    unreachable = getUnreachableNodes(graph, startingAirport)
    markUnreachable(graph, unreachable)
    return minNewConnections(unreachable)
