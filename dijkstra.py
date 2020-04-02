'''
def dijkstra(adjacentMatrix, start, end):
    vertexes = []
    shortestDFS = []  # Shortest distance from start
    previous_vertex = []


# Driver program
example_graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
                 [4, 0, 8, 0, 0, 0, 0, 11, 0],
                 [0, 8, 0, 7, 0, 4, 0, 0, 2],
                 [0, 0, 7, 0, 9, 14, 0, 0, 0],
                 [0, 0, 0, 9, 0, 10, 0, 0, 0],
                 [0, 0, 4, 14, 10, 0, 2, 0, 0],
                 [0, 0, 0, 0, 0, 2, 0, 1, 6],
                 [8, 11, 0, 0, 0, 0, 1, 0, 7],
                 [0, 0, 2, 0, 0, 0, 6, 7, 0]]
'''

import sys

# Can we place mindistance inside of dijstkra() ?
def minDistance(vertexes, distance, shortestPathTree):
    # Initilaize minimum distance for next node
    min = sys.maxsize

    # Search not nearest vertex not in the
    # shortest path tree
    for v in range(vertexes):
        if distance[v] < min and shortestPathTree[v] is False:
            min = distance[v]
            min_index = v

    return min_index


# Funtion that implements Dijkstra's single source
# shortest path algorithm for a graph represented
# using adjacency matrix representation
def dijkstra(graph, vertexes, source):
    distance = [sys.maxsize] * vertexes
    distance[source] = 0   # Distance from source
    shortestPathTree = [False] * vertexes

    for output in range(vertexes):

        # Pick the minimum distance vertex from
        # the set of vertices not yet processed.
        # u is always equal to src in first iteration
        u = minDistance(vertexes, distance, shortestPathTree)

        # Put the minimum distance vertex in the
        # Shortest path tree
        shortestPathTree[u] = True

        # Update dist value of the adjacent vertices
        # of the picked vertex only if the current
        # distance is greater than new distance and
        # the vertex in not in the Shortest path tree
        for v in range(vertexes):
            if graph[u][v] > 0 and shortestPathTree[v] == False and \
                    distance[v] > distance[u] + graph[u][v]:
                distance[v] = distance[u] + graph[u][v]
    for node in range(vertexes):
        print(node, distance[node])

example_graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
                 [4, 0, 8, 0, 0, 0, 0, 11, 0],
                 [0, 8, 0, 7, 0, 4, 0, 0, 2],
                 [0, 0, 7, 0, 9, 14, 0, 0, 0],
                 [0, 0, 0, 9, 0, 10, 0, 0, 0],
                 [0, 0, 4, 14, 10, 0, 2, 0, 0],
                 [0, 0, 0, 0, 0, 2, 0, 1, 6],
                 [8, 11, 0, 0, 0, 0, 1, 0, 7],
                 [0, 0, 2, 0, 0, 0, 6, 7, 0]]

vertexes = 9

# adjacentMatrix, vertex#, source vertex/row
dijkstra(example_graph, vertexes, 0)