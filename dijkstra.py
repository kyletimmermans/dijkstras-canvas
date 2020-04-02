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
def minDistance(vertexes, dist, sptSet):
    # Initilaize minimum distance for next node
    min = sys.maxsize

    # Search not nearest vertex not in the
    # shortest path tree
    for v in range(vertexes):
        if dist[v] < min and sptSet[v] == False:
            min = dist[v]
            min_index = v

    return min_index


# Funtion that implements Dijkstra's single source
# shortest path algorithm for a graph represented
# using adjacency matrix representation
def dijkstra(graph, vertexes, src):
    dist = [sys.maxsize] * vertexes
    dist[src] = 0
    sptSet = [False] * vertexes

    for cout in range(vertexes):

        # Pick the minimum distance vertex from
        # the set of vertices not yet processed.
        # u is always equal to src in first iteration
        u = minDistance(vertexes, dist, sptSet)

        # Put the minimum distance vertex in the
        # shotest path tree
        sptSet[u] = True

        # Update dist value of the adjacent vertices
        # of the picked vertex only if the current
        # distance is greater than new distance and
        # the vertex in not in the shotest path tree
        for v in range(vertexes):
            if graph[u][v] > 0 and sptSet[v] == False and \
                    dist[v] > dist[u] + graph[u][v]:
                dist[v] = dist[u] + graph[u][v]
    for node in range(vertexes):
        print(node, dist[node])

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