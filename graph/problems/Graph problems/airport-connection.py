# https://pkg.go.dev/github.com/lee-hen/Algoexpert/very_hard/22_airport_connections#section-readme


# AIRPORT CONNECTIONS

# A - airports
# R - routes
# O(A * (A + R) + A + R + Alog(A)) - time
# O(A + R) - space

"""
Steps : 
1. Adjacency List
2. Unreachable nodes
3. Build a connected component or cluster of Unreachable nodes.
4. Representative node of each Unreachable graph.
5. Count them
"""


class AirportNode:
    def __init__(self, airport):
        self.airport = airport
        self.connections = []
        self.isReachable = True
        self.unreachableConnections = []


def createGraph(airports, routes):
    airportGraph = {}
    for airport in airports:
        airportGraph[airport] = AirportNode(airport)
    for airport, connection in routes:
        airportGraph[airport].connections.append(connection)
    return airportGraph


def dfs(airportGraph, airport, visitedAirports):
    if airport in visitedAirports:
        return
    visitedAirports[airport] = True
    for connection in airportGraph[airport].connections:
        dfs(airportGraph, connection, visitedAirports)


def getUnreachableAirportNodes(airportGraph, airports, startingAirport):
    visitedAirports = {}
    dfs(airportGraph, startingAirport, visitedAirports)

    unreachableAirportNodes = []
    for airport in airports:
        if airport in visitedAirports:
            continue
        airportNode = airportGraph[airport]
        airportNode.isReachable = False
        unreachableAirportNodes.append(airportNode)
    return unreachableAirportNodes


def depthFirstAddUnreachableConnections(
    airportGraph, airport, unreachableConnections, visitedAirports
):
    if airportGraph[airport].isReachable:
        return
    if airport in visitedAirports:
        return
    visitedAirports[airport] = True
    unreachableConnections.append(airport)
    connections = airportGraph[airport].connections
    for connection in connections:
        depthFirstAddUnreachableConnections(
            airportGraph, connection, unreachableConnections, visitedAirports
        )


def markUnreachableConnections(airportGraph, unreachableAirportNodes):
    for airportNode in unreachableAirportNodes:
        airport = airportNode.airport
        unreachableConnections = []
        depthFirstAddUnreachableConnections(
            airportGraph, airport, unreachableConnections, {}
        )
        airportNode.unreachableConnections = unreachableConnections


def getMinNumberOfNewConnections(airportGraph, unreachableAirportNodes):
    unreachableAirportNodes.sort(
        key=lambda airport: len(airport.unreachableConnections), reverse=True
    )

    numberOfNewConnections = 0
    for airportNode in unreachableAirportNodes:
        if airportNode.isReachable:
            continue
        numberOfNewConnections += 1
        for connection in airportNode.unreachableConnections:
            airportGraph[connection].isReachable = True
    return numberOfNewConnections


def airportConnections(airports, routes, startingAirport):
    airportGraph = createGraph(airports, routes)
    unreachableAirportNodes = getUnreachableAirportNodes(
        airportGraph, airports, startingAirport
    )
    markUnreachableConnections(airportGraph, unreachableAirportNodes)
    return getMinNumberOfNewConnections(airportGraph, unreachableAirportNodes)


airports = [
    "BGI",
    "CDG",
    "DEL",
    "DOH",
    "DSM",
    "EWR",
    "EYW",
    "HND",
    "ICN",
    "JFK",
    "LGA",
    "LHR",
    "ORD",
    "SAN",
    "SFO",
    "SIN",
    "TLV",
    "BUD",
]

routes = [
    ["DSM", "ORD"],
    ["ORD", "BGI"],
    ["BGI", "LGA"],
    ["SIN", "CDG"],
    ["CDG", "SIN"],
    ["CDG", "BUD"],
    ["DEL", "DOH"],
    ["DEL", "CDG"],
    ["TLV", "DEL"],
    ["EWR", "HND"],
    ["HND", "ICN"],
    ["HND", "JFK"],
    ["ICN", "JFK"],
    ["JFK", "LGA"],
    ["EYW", "LHR"],
    ["LHR", "SFO"],
    ["SFO", "SAN"],
    ["SFO", "DSM"],
    ["SAN", "EYW"],
]

startingAirport = "LGA"
# print(airportConnections(airports, routes, startingAirport))


airports1 = ["A", "B", "C", "D", "E", "F", "G", "H"]
routes1 = [["A", "B"], ["C", "D"], ["D", "E"], ["H", "F"], ["F", "G"]]

print(airportConnections(airports1, routes1, "B"))
