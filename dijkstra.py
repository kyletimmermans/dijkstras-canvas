'''
Function should look like: dijkstra(graph, start, end)
Should move from print path A->B->C and distance number
if end = end - 1
path.append()
'''

import sys

'''
# Function that implements Dijkstra's single source shortest path using a 2D array to represent an Adjacency Matrix
def dijkstra(graph, start): 
    vertexes = len(graph)  # -1 or +1, do we start at 0 in the graph?
    distance = [sys.maxsize+1] * vertexes  # Initialize distance super far, so unreachable (sys.maxsize+1)
    distance[start] = 0   # Initialize source to be 0
    visited = [False] * vertexes  # Visited array initialized to not visited

    for i in range(vertexes):
        minDistance = sys.maxsize + 1  # Impossible to be at, so its automatically the largest
        for length in range(vertexes):  # Return smallest distance of a row
            if distance[length] < minDistance and visited[length] is False:
                minDistance = distance[length]
                vertex = length  # vertex = the index of the smallest distance in a row(vertex)
        print("u = " + str(vertex) + " | minDinstance(vertexes=" + str(vertexes) + ", distance=" + str(distance) + ", visited=" + str(visited))

        visited[vertex] = True  # Mark vertex as visited

        for length in range(vertexes):  # For each distance in a row(vertex)
            if graph[vertex][length] > 0 and visited[length] is False and distance[length] > distance[vertex] + graph[vertex][length]:
                distance[length] = distance[vertex] + graph[vertex][length]  # Add smallest distances
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

#adjacentMatrix, vertex#, source vertex/row
dijkstra(example_graph, 0)
'''

# Function that implements Dijkstra's single source shortest path using a 2D array to represent an Adjacency Matrix
def dijkstra(graph, start, end):
    vertexes = len(graph)  # -1 or +1, do we start at 0 in the graph?
    distance = [sys.maxsize+1] * vertexes  # Initialize distance super far, so unreachable (sys.maxsize+1)
    distance[start] = 0   # Initialize source to be 0
    visited = [False] * vertexes  # Visited array initialized to not visited
    path = []  # Stores the smallest distance

    for nextVertex in range(vertexes):  # For all vertexes
        minDistance = sys.maxsize + 1  # Impossible to be at, so its automatically the largest
        for length in range(vertexes):  # Return smallest distance of a row  # Return
            if distance[length] < minDistance and visited[length] is False:
                minDistance = distance[length]
                vertex = length  # vertex = the index of the smallest distance in a row(vertex)
        # Every time, we see this point, vertex is increased because the last vertex is marked as visited, and we move to the next one

        visited[vertex] = True  # Mark vertex as visited

        for length in range(vertexes):  # For each distance in a row(vertex)
            if graph[vertex][length] > 0 and visited[length] is False and distance[length] > distance[vertex] + graph[vertex][length]:
                distance[length] = distance[vertex] + graph[vertex][length]  # Add smallest distances

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

#adjacentMatrix, vertex#, source vertex/row
dijkstra(example_graph, 0, 9)
