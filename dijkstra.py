'''
Function should look like: dijkstra(graph, start, end)
print From A to B: path = A->B->C and distance number
if end = end - 1
path.append()
'''

import sys
path = []
vertexes = 9
adjacencyMatrix = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
                 [4, 0, 8, 0, 0, 0, 0, 11, 0],
                 [0, 8, 0, 7, 0, 4, 0, 0, 2],
                 [0, 0, 7, 0, 9, 14, 0, 0, 0],
                 [0, 0, 0, 9, 0, 10, 0, 0, 0],
                 [0, 0, 4, 14, 10, 0, 2, 0, 0],
                 [0, 0, 0, 0, 0, 2, 0, 1, 6],
                 [8, 11, 0, 0, 0, 0, 1, 0, 7],
                 [0, 0, 2, 0, 0, 0, 6, 7, 0]]
start = 1
end = 9


# Function that implements Dijkstra's single source shortest path using a 2D array to represent an Adjacency Matrix
def dijkstra():
    global vertexes, start, end, adjacencyMatrix
    start = start - 1
    graph = adjacencyMatrix
    vertexes = len(graph)  # -1 or +1, do we start at 0 in the graph?
    distance = [sys.maxsize+1] * vertexes  # Initialize distance super far, so unreachable (sys.maxsize+1)
    distance[start] = 0   # Initialize source to be 0
    visited = [False] * vertexes  # Visited array initialized to not visited
    parent = [-1] * vertexes  # Parent array of previous vertexes to store shortest path tree, see:  path[dist] = vertex

    for nextVertex in range(vertexes):  # For all vertexes
        minDistance = sys.maxsize + 1  # Impossible to be at, so its automatically the largest
        for length in range(vertexes):  # Return smallest distance of a row  # Return
            if distance[length] < minDistance and visited[length] is False:
                minDistance = distance[length]
                vertex = length  # vertex = the index of the smallest distance in a row(vertex)
        # Every time, we see this point, vertex is increased because the last vertex is marked as visited, and we move to the next one

        visited[vertex] = True  # Mark vertex as visited

        ########################################## Why does this part work ##########################################################
        for dist in range(vertexes):  # For each distance in a row(vertex)
            if graph[vertex][dist] > 0 and visited[length] is False and distance[dist] > distance[vertex] + graph[vertex][dist]:
                distance[dist] = distance[vertex] + graph[vertex][dist]  # Add smallest distance
                parent[dist] = vertex  ####### Why does this line work #######
        #############################################################################################################################

    def getPath(parent, j):  # Recurse through parent array and append to path
        global path
        if parent[j] == -1:
            path.append(j)
            return
        getPath(parent, parent[j])
        path.append(j)

    getPath(parent, end-1)  # Execute getPath here, for start to end
    print(path)

    print("node="+str(start)+" distance="+str(distance[end-1]))


#adjacentMatrix, vertex#, source vertex/row
dijkstra()

# path for 0 to 9: 0->1->2->8