parent = [-1, 0, 1, 2, 5, 6, 7, 0, 2]

def printPath(parent, j):
    # Base Case : If j is source
    if parent[j] == -1:
        print(j, end=' ')
        return
    printPath(parent, parent[j])
    print(j, end=' ')

printPath(parent, 8)