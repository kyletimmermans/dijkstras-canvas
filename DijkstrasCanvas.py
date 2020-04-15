'''
Kyle Timmermans
Project Start Date: March 18th, 2020
v1.2 Release Date: April 15th, 2020
compiled in python v3.8.2

ToDo:
    1. Error Handling: Can't make vertex into the button area, give messagebox, can't draw up here, place in addVertex
    2. Fix:
            edges[alphabet1[letter]] = [vertexStart, vertexDestination]  # Labeling the dictionary of edges{} w/ letters
            UnboundLocalError: local variable 'vertexDestination' referenced before assignment
    3. Keep testing out bugs, try and break it
        -UnboundLocalError: local variable 'vertexStart' referenced before assignment
        -key error with non-existant edges
        -Hit buttons in different orders
'''

# Many global variables and long functions because many of these functions can't take parameters because of tkinter module #

from tkinter import *  # Import all widgets, canvas, etc
from tkinter import messagebox, font  # Messagebox warnings, custom font
from string import ascii_uppercase, ascii_lowercase  # Use to label edges
import re  # Splitting up and sanitizing input strings
import sys  # Used for sys.maxsize

#############
# Variables #
#############
alphabet1 = ascii_uppercase
alphabet2 = ascii_lowercase
letter = 0
vertexNumber = 13   # ID's start being assigned at 1, but we already have the widgets, they make up first 10 ID's
helperNumber = 1
clickNumber = 0     # Start click number at 0, i.e. start first of 2 clicks to make line
vertexes = {}       # Store vertex number and its location
edges = {}          # Store edge and its location
adjacencyMatrix = []  # Store all weights and vertexes to be traversed over, edited by addEdgeWeight()
path = []  # Store shortest path vertexes
start, end = 0, 0   # Init start and end to be used with the button
textCounterVertical = 25  # y-value to place shortest paths, incremented in dijkstra() so we can have a clean list
vertexReset = 0  # Used in resetButton
isReset = False  # Used in resetButton
vertexButtonisClicked = 0  # Used in resetButton
separationLineLimit = 1  # Max amount of short path results to be shown at once

#############
# Functions #
#############
def addVertex(event):
    global vertexNumber, helperNumber   # Grab vertexNumber from earlier, it is now global, no need to pass it through as a param now  # helperNumber: Need a dynamic number to add to vertex number
    global isReset, finalElementID, vertexButtonisClicked
    vertexButtonisClicked = 1  # At least something is done, used for resetButton
    x0 = event.x    # Current X-Coord for mouse click
    y0 = event.y    # Current Y-Coord for mouse click
    # Error Handling - If vertex is attempted to be placed above separation line
    if y0 < 200:  # Separation line begins at y=200, anything above is widgets space
        messagebox.showwarning(title="Warning", message="Can't place vertexes above the Canvas Separation Line!")
        return  # Exit, let user try again
    # -25s and +25s to ensure the tip of the mouse-pointer is the center of the created circle
    vertex = draw_space.create_oval(x0-25, y0-25, x0+25, y0+25, fill='Green', tags='vertex') # Create the vertex, give it a function soon to add to the dictionary
    vertex_text = draw_space.create_text(x0, y0, text=vertexNumber-12-vertexReset, tags='vertex')  # +25 to get to the center of a 50 circle
    draw_space.pack()
    if isReset == False:  # if not after a reset
        vertexes[vertexNumber-12-vertexReset] = draw_space.coords(vertexNumber+helperNumber)  # vertexNumber + helperNumber
        helperNumber += 1  # increment and add to vertex labels so we get just the vertex circle, place here because we want it to start adding after VN=1
        vertexNumber += 1
        finalElementID = vertex_text  # If stop here, this is the final element id
    else:   # if after a reset
        vertexes[vertexNumber - 12 - vertexReset] = draw_space.coords(finalElementID+1)  # +1 because vertex_text also cost an id when printed
        vertexNumber += 1
        finalElementID = vertex_text  # If stop here, this is the final element id


def addEdge(event):  # Why does *args work for this?
    global clickNumber, letter, x1, y1
    global finalElementID
    if letter != 52:  # Error Handling - Edge Amount
        pass  # Keep going if condition met
    else:
        messagebox.showwarning(title="Warning", message="Number of edges limited to 52!")  # Handle for when we run out of vertex labels (Past lower case alphabet)
        edgeButtonSet()  # Go straight to giving edge weights
        return
    if clickNumber == 0:  # start pos before mouse is clicked
        x1 = event.x   # start x pos of mouse
        y1 = event.y   # start y pos of mouse
        clickNumber = 1   # On next click, define x2, y2
    else:                  # end coords when mouse is unclicked
        x2 = event.x    # end x pos of mouse
        y2 = event.y    # end y pos of mouse
        # Error Handling - When drawing edge to itself
        if (x1 <= x2 <= x1+25) and (y1 <= y2 <= y1+25):
            messagebox.showwarning(title="Warning", message="Can not draw an edge from a vertex to itself!")
            clickNumber = 0  # Allow a new line to be drawn again, from a new spot
            return  # Drop the rest of the function
        line = draw_space.create_line(x1, y1, x2, y2, fill='Black', width=5, tags='edge')   # Draw line with those coords, needs edge tag for reset
        finalElementID = line  # if stopping here before reset
        if letter <= 25:  # Go through uppercase letters
            if ((x1 == x2) and ((y1 > y2) or (y1 < y2))):
                lineLetter = line_text = draw_space.create_text(((x1 + x2) / 2) - 10, ((y1 + y2) / 2), text=alphabet1[letter], font=('Courier', 25), tags='edge')
            elif ((y1 == y2) and ((x1 > x2) or (x1 < x2))):
                lineLetter = line_text = draw_space.create_text(((x1 + x2) / 2), ((y1 + y2) / 2) + 12, text=alphabet1[letter], font=('Courier', 25), tags='edge')
            elif ((x1 < x2) and (y1 < y2)) or ((x1 > x2) and (y1 > y2)):  # Get Edge labeling correct, if same do one way, if different, do other way
                lineLetter = line_text = draw_space.create_text(((x1 + x2) / 2) - 10, ((y1 + y2) / 2) + 10, text=alphabet1[letter], font=('Courier', 25), tags='edge')
            elif ((x1 > x2) and (y1 < y2)) or ((x1 < x2) and (y1 > y2)):
                lineLetter = line_text = draw_space.create_text(((x1 + x2) / 2) + 10, ((y1 + y2) / 2) + 10, text=alphabet1[letter], font=('Courier', 25), tags='edge')
            else:
                lineLetter = line_text = draw_space.create_text(((x1 + x2) / 2), ((y1 + y2) / 2) + 10, text=alphabet1[letter], font=('Courier', 25), tags='edge')
        elif letter > 25:
            if ((x1 == x2) and ((y1 > y2) or (y1 < y2))):
                lineLetter = line_text = draw_space.create_text(((x1 + x2) / 2) - 10, ((y1 + y2) / 2), text=alphabet2[letter-26], font=('Courier', 25), tags='edge')
            elif ((y1 == y2) and ((x1 > x2) or (x1 < x2))):
                lineLetter = line_text = draw_space.create_text(((x1 + x2) / 2), ((y1 + y2) / 2) + 12, text=alphabet2[letter-26], font=('Courier', 25), tags='edge')
            elif ((x1 < x2) and (y1 < y2)) or ((x1 > x2) and (y1 > y2)):  # Get Edge labeling correct, if same do one way, if different, do other way
                lineLetter = line_text = draw_space.create_text(((x1 + x2) / 2) - 10, ((y1 + y2) / 2) + 10, text=alphabet2[letter-26], font=('Courier', 25), tags='edge')
            elif ((x1 > x2) and (y1 < y2)) or ((x1 < x2) and (y1 > y2)):
                lineLetter = line_text = draw_space.create_text(((x1 + x2) / 2) + 10, ((y1 + y2) / 2) + 10, text=alphabet2[letter-26], font=('Courier', 25), tags='edge')
            else:
                lineLetter = line_text = draw_space.create_text(((x1 + x2) / 2), ((y1 + y2) / 2) + 10, text=alphabet2[letter-26], font=('Courier', 25), tags='edge')
        finalElementID = lineLetter  # if stopping here before reset
        draw_space.pack()  # Pack into canvas and give unique ID
        # If start of edge is found in a vertex (x1, y1) and end of edge is found in a vertex (x2, y2), place them in edges {}
        for key in vertexes:
            if (vertexes[key][0] < x1 < vertexes[key][2]) == True and (vertexes[key][1] < y1 < vertexes[key][3]) == True:  # If at the same point, must include x and y axis, otherwise, not specific enough
                vertexStart = key
        for key in vertexes:
            if (vertexes[key][0] < x2 < vertexes[key][2]) == True and (vertexes[key][1] < y2 < vertexes[key][3]) == True:
                vertexDestination = key
        if letter <= 25:
            edges[alphabet1[letter]] = [vertexStart, vertexDestination]  # Labeling the dictionary of edges{} w/ letters
        elif letter > 25:
            edges[alphabet2[letter-26]] = [vertexStart, vertexDestination]  # Needs a -26 or will return index error
        clickNumber = 0   # We have a line drawn, go back and determine the x1, y1 start coords for the next line)
        letter += 1     # Next letter, eventually goes to lowercase

# Vertex Button
def vertexButtonSet():
    global adjacencyMatrix
    # Fill matrix with zeros
    adjacencyMatrix = [[0] * (vertexNumber - 13) for x in range(vertexNumber - 13)]  # Must use list comprehension, [[0] * n] * m is just a list of references to [0]*n and will change everything
    draw_space.unbind('<Button 1>')
    draw_space.tag_bind('vertex', '<Button-1>', addEdge)  # tags used for clicking function, the declared variables in addVertex need the 'vertex' tag

# Edge Finish Button
def edgeButtonSet():
    # Can't draw vertexes anymore
    draw_space.unbind('<Button 1>')

# Input button next to entry field for getting weights
def addEdgeWeight():
    global adjacencyMatrix
    global finalElementID
    inputValues = weightEntry.get()  # get user weight from entry using get()
    inputValues = re.sub('[^0-9a-zA-Z]+', ' ', inputValues).split()  # Space allows for correct split, instead of just no spaces
    inputValues = [inputValues[x:x + 2] for x in range(0, len(inputValues), 2)]  # For every 2 items put them in a new list, increase x, stop at 2, repeat
    # Input one value, or multiple values separated by commas
    if len(inputValues) > len(edges.keys()):    # Input sanitation
        messagebox.showwarning(title="Warning", message="One or more weight value(s) were attempted to be added to edges that do not exist, but were removed! All other values have been added.")  # User put too many edges in
    else:
        for lst in range(len(inputValues) - 1, -1, -1):  # Got to go backwards or its like sawing off a tree branch you're sitting on
            if sorted(inputValues)[lst][0] not in edges.keys():
                inputValues.pop(lst)  # Pop removes element from list by index, .remove() is by value
                messagebox.showwarning(title="Warning", message="One or more weight value(s) were attempted to be added to edges that do not exist, but were removed! All other values have been added.")
    for lst in inputValues: #  For list of lists of inputted weights separated by commas
        edgeName, weight = lst[0], int(lst[1])
        for key in edges:   # Place values into adjacencyMatrix, check with edges{} first to see if it exists
            if key == edgeName:     # Get values out of edges, e.g. edges{A: [1, 2]}
                adjacencyMatrix[edges[edgeName][0]-1][edges[edgeName][1]-1] = weight  # -1 because lists in reality, start from 0
                adjacencyMatrix[edges[edgeName][1]-1][edges[edgeName][0]-1] = weight  # Reversed here, can travel edges both ways b/c its an undirected graph
        point1 = vertexes[edges[edgeName][0]]  # Storing vertexes{} points from edges{} for x1,x2,y1,y2
        point2 = vertexes[edges[edgeName][1]]  # e.g. [359.0, 448.0, 530.0, 343.0]
        x1, y1, x2, y2 = point1[0], point1[1], point2[0], point2[1]  # e.g. 359.0y2 = point2[1]
        if (x2 - x1) > 0.0:
            slope = (y2 - y1) / (x2 - x1)  # Check Slope for extra cases
        else:  # Just in case we have zero in denominator
            slope = 0
        if ((x1 == x2) and ((y1 > y2) or (y1 < y2))):
            line_text = draw_space.create_text(((x1 + x2) / 2) - 10, ((y1 + y2) / 2), text=weight, font=('Courier', 15), tags='edge')
        elif ((y1 == y2) and ((x1 > x2) or (x1 < x2))):
            line_text = draw_space.create_text(((x1 + x2) / 2), ((y1 + y2) / 2) - 5, text=weight, font=('Courier', 15), tags='edge')
        elif ((x1 < x2) and (y1 < y2)) or ((x1 > x2) and (y1 > y2)):
            if slope < 0.20:
                line_text = draw_space.create_text(((x1 + x2) / 2) + 15, ((y1 + y2) / 2), text=weight, font=('Courier', 15), tags='edge')
            elif 1.50 > slope >= 0.20:
                line_text = draw_space.create_text(((x1 + x2) / 2) + 25, ((y1 + y2) / 2), text=weight, font=('Courier', 15), tags='edge')
            elif 2.00 > slope >= 1.50:
                line_text = draw_space.create_text(((x1 + x2) / 2) + 35, ((y1 + y2) / 2), text=weight, font=('Courier', 15), tags='edge')
            elif slope >= 2.00:
                line_text = draw_space.create_text(((x1 + x2) / 2) + 40, ((y1 + y2) / 2), text=weight, font=('Courier', 15), tags='edge')
        elif ((x1 > x2) and (y1 < y2)) or ((x1 < x2) and (y1 > y2)):
            if slope < 0.20:
                line_text = draw_space.create_text(((x1 + x2) / 2) - 5, ((y1 + y2) / 2), text=weight, font=('Courier', 15), tags='edge')
            elif 1.50 > slope >= 0.20:
                line_text = draw_space.create_text(((x1 + x2) / 2) - 10, ((y1 + y2) / 2), text=weight, font=('Courier', 15), tags='edge')
            elif 2.00 > slope >= 1.50:
                line_text = draw_space.create_text(((x1 + x2) / 2) - 15, ((y1 + y2) / 2), text=weight, font=('Courier', 15), tags='edge')
            elif slope >= 2.00:
                line_text = draw_space.create_text(((x1 + x2) / 2) - 20, ((y1 + y2) / 2), text=weight, font=('Courier', 15), tags='edge')
        finalElementID = line_text  # if stopping here before reset


# Function that implements Dijkstra's single source shortest path using a 2D array to represent an Adjacency Matrix
# Everytime we call, we can change the start position and get all the distances
# Only want the distance from start to end, and its path
def dijkstra():
    global vertexes, start, end, adjacencyMatrix, path, textCounterVertical, finalElementID
    graph = adjacencyMatrix
    inputValues = shortpathEntry.get()
    inputValues = re.sub('[^0-9]+', ' ', inputValues).split()
    # Error Handling - Chop off extra values if present
    if (int(inputValues[0]) and int(inputValues[1])) in vertexes.keys():
        if int(inputValues[1]) > int(inputValues[0]):
            start, end = int(inputValues[0]) - 1, int(inputValues[1])
        elif int(inputValues[0]) > int(inputValues[1]):   # if start > end, Allows for v2,v1 instead of v1,v2. Allows us to go backwards
            start, end = int(inputValues[1]) - 1, int(inputValues[0])
    else:
        messagebox.showwarning(title="Warning", message="One or neither of the vertexes entered, do not exist!")  # Error Handling - If vertex(es) not found
        return  # Show warning and backout of function
    vertexesLocal = len(graph)  # -1 or +1, do we start at 0 in the graph?
    distance = [sys.maxsize+1] * vertexesLocal  # Initialize distance super far, so unreachable (sys.maxsize+1)
    distance[start] = 0   # Initialize source to be 0
    visited = [False] * vertexesLocal  # Visited array initialized to not visited
    parent = [-1] * vertexesLocal  # Parent array of previous vertexes to store shortest path tree, see:  path[dist] = vertex
    for nextVertex in range(vertexesLocal):  # For all vertexes
        minDistance = sys.maxsize + 1  # Impossible to be at, so its automatically the largest
        for length in range(vertexesLocal):  # Return smallest distance of a row  # Return
            if distance[length] < minDistance and visited[length] is False:
                minDistance = distance[length]
                vertex = length  # vertex = the index of the smallest distance in a row(vertex)
        # Every time, we see this point, vertex is increased because the last vertex is marked as visited, and we move to the next one
        visited[vertex] = True  # Mark vertex as visited
        # Why does this part work
        for dist in range(vertexesLocal):  # For each distance in a row(vertex)
            if graph[vertex][dist] > 0 and visited[length] is False and distance[dist] > distance[vertex] + graph[vertex][dist]:
                distance[dist] = distance[vertex] + graph[vertex][dist]  # Add smallest distance
                parent[dist] = vertex  # Why does this line work
    path = []  # Reset path so it doesn't add the last pass's data, bc path is global
    # How does this work
    def getPath(parent, j):  # Recurse through parent array and append vertexes to path
        global path
        if parent[j] == -1:
            path.append(j)
            return
        getPath(parent, parent[j])
        path.append(j)
    getPath(parent, end-1)  # Execute getPath here, for start to end
    if int(inputValues[0]) > int(inputValues[1]):  # Allows us to check original input values and do v2,v1 instead of v1,v2
        path = [elem for elem in reversed(path)]  # One liner to reverse list, if it can be found going forwards, it can be found going backwards
    final_string = ""  # Initialize final string
    path_string = ""  # Initialize path with arrows string
    for i in range(len(path)):  # Create arrow path, if last value, don't place in so no hanging arrows
        if i != len(path) - 1:
            path_string += str(path[i]+1) + "-->"  # Needs a +1 for some reason
        else:
            path_string += str(path[i]+1)
    textCounterVertical += 20  # Move down the list
    # Error Handling - When results get to separationLine, 8 mount of results, or when it reaches (8*20) + 25 pixels high
    if textCounterVertical > 185:
        messagebox.showwarning(title="Warning", message="'Shortest Paths' results bank is full, clearing past results")
        textCounterVertical = 45  # Reset to normal
        draw_space.delete('shortPath')  # Remove prior shortest path results
    # Short path spacing, starting with normal cases
    if distance[end-1] < sys.maxsize and (inputValues[0] != inputValues[1]):  # Normal and backwards cases, has a connection, and not going to itself
        final_string = "v"+str(inputValues[0])+" to v"+str(inputValues[1])+": Path = "+path_string+" | Distance = "+str(distance[end-1])  # Final string to output, start always needs +1
        stringSize = 0  # Used to dynamically update the x-value for the text depending on the size of final string
        for length in range(len(final_string)):
            if length > 37:   # 37 is smallest possible string length, - needs only 3 pixels
                if final_string[length] == '-':
                    stringSize += 3.5
                else:
                    stringSize += 4
        finalLabel = draw_space.create_text(885+stringSize, textCounterVertical, text=final_string, font=('Times', 14), tags='shortPath')  # 884 is for when the string is smallest
    elif distance[end-1] > sys.maxsize and (inputValues[0] != inputValues[1]):  # If no connection found
        final_string = "v"+str(inputValues[0])+" to v"+str(inputValues[1])+": No Connection Found"
        stringSize = 0  # init stringSize locally
        for length in range(len(final_string)):
            if length > 29:  # 28 is the smallest length for no path found
                stringSize += 4  # Add 4 more spaces to adjust for a new character, every time we are over the smallest point
                if length == len(final_string) - 1:
                    stringSize += 1  # Needs an extra at the end to look uniform with others
        finalLabel = draw_space.create_text(869+stringSize, textCounterVertical, text=final_string, font=('Times', 14), tags='shortPath')
    elif inputValues[0] == inputValues[1]:
        final_string = "v" + str(inputValues[0]) + " to v" + str(inputValues[1]) + ": Path = None | Distance = 0"
        stringSize = 0  # init stringSize locally
        for length in range(len(final_string)):
            if length > 28:  # 28 is the smallest length for no path found
                stringSize += 4  # Add 4 more spaces to adjust for a new character, every time we are over the smallest point
                if length == len(final_string) - 1:
                    stringSize += 1  # Needs an extra at the end to look uniform with others
        finalLabel = draw_space.create_text(855+stringSize, textCounterVertical, text=final_string, font=('Times', 14), tags='shortPath')
    draw_space.pack()
    finalElementID = finalLabel  # Used for reset


def resetGraph():
    global letter, clickNumber, start, end, textCounterVertical, vertexes, edges, adjacencyMatrix, path
    global vertexReset, isReset, finalElementID, vertexButtonisClicked
    if vertexButtonisClicked == 0:  # If nothing is done at all and reset is hit, last element created is id #12
        finalElementID = 13
    isReset = True
    vertexReset = vertexNumber-13
    # Delete all user created shapes
    draw_space.delete('vertex')
    draw_space.delete('edge')
    draw_space.delete('shortPath')
    letter, clickNumber, start, end, textCounterVertical = 0, 0, 0, 0, 25  # Init vars back to default, DO revert vertexNumber and helperNumber, id number's do not reset with .delete()
    vertexes, edges, adjacencyMatrix, path = {}, {}, [], []  # Init dicts and lists to empty
    draw_space.bind('<Button-1>', addVertex)  #Start back to placing vertexes

# Start Main #

####################
# Window / Widgets #
####################
root = Tk()
root.title("Dijkstra's Canvas - @KyleTimmermans")
draw_space = Canvas(root, width=1500, height=1000, background='Floral White')  # Canvas for drawing, make dynamic sizing in the future
draw_space.pack()

draw_space.bind('<Button-1>', addVertex)  # Bind addVertex to mouse1 to Begin Program

# Widgets
### We have 13 widgets, they take up first eleven ID Numbers, so start vertexNumber at 13
### Anytime a widget is added, the vertexNumber must be changed and addVertex values must be changed
### Search for "-13" or -"whatever number of widgets there are"
### Look for "-12" too
### Fix everything in addVertex() and addEdgeWeight() when adding another widget
vertexText = Label(text='Input Vertexes by left clicking mouse: ', font=('Helvetica', 14), background='Floral White')  # Vertex Text
draw_space.create_window(126, 30, window=vertexText)  # Draw Vertex Text
vertexButton = Button(text='Done', command=vertexButtonSet, background='Floral White')  # Vertex Button
draw_space.create_window(276, 30, window=vertexButton)  # Draw Vertex Button
edgeText = Label(text='Input Edges by left clicking the start vertex and then the destination vertex: ', font=('Helvetica', 14), background='Floral White')  # Edge Text
draw_space.create_window(245, 75, window=edgeText)  # Draw Edge Text
edgeButton = Button(text='Done', command=edgeButtonSet, background='Floral White')  # Edge Button
draw_space.create_window(510, 75, window=edgeButton)    # Draw Edge Button
weightText = Label(text='Input the weights of edges between nodes e.g. A=7, B=8 (Case-Sensitive)', font=('Helvetica', 14), background='Floral White')  # Weight Text
draw_space.create_window(241, 120, window=weightText)   # Draw Weight Text
weightEntry = Entry(root)   # Weight Entry
draw_space.create_window(589, 120, window=weightEntry)  # Draw Weight Entry
weightInput = Button(text='Input', command=addEdgeWeight, background='Floral White')  # Weight Button
draw_space.create_window(715, 120, window=weightInput)   # Draw Weight Button
shortpathText = Label(text='Enter the two vertexes for the shortest path you want e.g. v2,v4', font=('Helvetica', 14), background='Floral White')  # Short Path Text
draw_space.create_window(209, 165, window=shortpathText)    # Draw Short Path Text
shortpathEntry = Entry(root)    # Short Path Entry
draw_space.create_window(521, 165, window=shortpathEntry)  # Draw Short Path Entry
shortpathButton = Button(text='Show Result', command=dijkstra, background='Floral White')    # Short Path Button
draw_space.create_window(671, 165, window=shortpathButton)  # Draw Short Path Button
resetButton = Button(text='Reset Canvas', command=resetGraph, background='Floral White')  # Reset Button
draw_space.create_window(500, 30, window=resetButton)  # Draw Reset Button
custFont = font.Font(family='Helvetica', size=15, weight='bold', underline=1)  # Custom Font
resultTitle = Label(text='Shortest Paths', font=custFont, background='Floral White')  # Result Title (Bold, Underlined)
draw_space.create_window(825, 25, window=resultTitle)  # Draw Result Title
separationLine = draw_space.create_line(0, 200, 1500, 200, fill='Black', width=1)  # Separation Line, needs .pack() b/c it's not a window
draw_space.pack()  # Pack in separationLine, ID#13

root.mainloop()  # Keep window open and loop all its functions

# End of Main #