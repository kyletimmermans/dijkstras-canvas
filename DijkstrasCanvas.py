'''
Kyle Timmermans
March 18th, 2020
python v3.8.2

Fix weight labeling when x and y are greater than point 1
For add edge weight, when entering non-real weight value, make sure to handle 'KeyError' error
'''

# Many global calls because many of these functions can't take parameters because of tkinter module

from tkinter import *
from tkinter import messagebox  # For error handling
from string import ascii_uppercase, ascii_lowercase  # Use to label edges
import re  # Splitting up and sanitizing input strings

#############
# Variables #
#############
alphabet1 = ascii_uppercase
alphabet2 = ascii_lowercase
letter = 0
vertexNumber = 10    # ID's start being assigned at 1, but we already have the widgets, they make up first 10 ID's
helperNumber = 1
edgeNumber = vertexNumber  # Continue numbering shapes after vertexes are placed
clickNumber = 0     # Start click number at 0, i.e. start first of 2 clicks to make line
vertexes = {}       # Store vertex number and its location
edges = {}          # Store edge and its location
adjacencyMatrix = []  # Store all weights and vertexes to be traversed over, edited by addEdgeWeight()

#############
# Functions #
#############
def addVertex(event):
    global vertexNumber   # Grab vertexNumber from earlier, it is now global, no need to pass it through as a param now
    global helperNumber   # # Need a dynamic number to add to vertex number
    x0 = event.x    # Current X-Coord for mouse click
    y0 = event.y    # Current Y-Coord for mouse click
    vertex = draw_space.create_oval(x0, y0, x0+50, y0+50, fill='Green', tags='vertex') # Create the vertex, give it a function soon to add to the dictionary
    vertex_text = draw_space.create_text((x0+25, y0+25), text=vertexNumber-9, tags='vertex')  # +25 to get to the center of a 50 circle
    draw_space.pack()
    if vertexNumber == 1:  # ID's go up by odd numbers b/c be are essentially creating two objects, the circle and its textbox label
        vertexes[vertexNumber-9] = draw_space.coords(vertexNumber)   # Coords just going with continuity of id's auto-assigning
        vertexNumber += 1  # increment vertex labels
    elif vertexNumber < 45:
        vertexes[vertexNumber-9] = draw_space.coords(vertexNumber+helperNumber)  ##### Maybe not use .coords but just ID??
        helperNumber += 1  # increment and add to vertex labels so we get just the vertex circle, place here because we want it to start adding after VN=1
        vertexNumber += 1
    else:
        messagebox.showwarning(title="Warning", message="Number of vertexes limited to 52! You can now add edges to your graph.") # Handle for when we run out of vertex labels (Past lower case alphabet)
        vertexButtonSet()  # Go straight to creating edges

def addEdge(event):  # Why does *args work for this?
    global clickNumber
    global edgeNumber
    global letter
    global x1, y1
    if clickNumber == 0:  # start pos before mouse is clicked
        x1 = event.x   # start x pos of mouse
        y1 = event.y   # start y pos of mouse
        clickNumber = 1   # On next click, define x2, y2
    else:                  # end coords when mouse is unclicked
        x2 = event.x    # end x pos of mouse
        y2 = event.y    # end y pos of mouse
        line = draw_space.create_line(x1, y1, x2, y2, fill='Black', width=5)   # Draw line with those coords
        if letter <= 25:  # Go through uppercase letters
            if ((x1 < x2) and (y1 < y2)) or ((x1 > x2) and (y1 > y2)):  # Get Edge labeling correct, if same do one way, if different, do other way
                line_text = draw_space.create_text(((x1 + x2) / 2) - 10, ((y1 + y2) / 2) + 10, text=alphabet1[letter], font=('Courier', 25))
            elif ((x1 > x2) and (y1 < y2)) or ((x1 < x2) and (y1 > y2)):
                line_text = draw_space.create_text(((x1 + x2) / 2) + 10, ((y1 + y2) / 2) + 10, text=alphabet1[letter], font=('Courier', 25))
            else:
                line_text = draw_space.create_text(((x1 + x2) / 2), ((y1 + y2) / 2) + 10, text=alphabet1[letter], font=('Courier', 25))
        elif letter > 25:
            if ((x1 < x2) and (y1 < y2)) or ((x1 > x2) and (y1 > y2)):  # Get Edge labeling correct, if same do one way, if different, do other way
                line_text = draw_space.create_text(((x1 + x2) / 2) - 10, ((y1 + y2) / 2) + 10, text=alphabet2[letter-26], font=('Courier', 25))
            elif ((x1 > x2) and (y1 < y2)) or ((x1 < x2) and (y1 > y2)):
                line_text = draw_space.create_text(((x1 + x2) / 2) + 10, ((y1 + y2) / 2) + 10, text=alphabet2[letter-26], font=('Courier', 25))
            else:
                line_text = draw_space.create_text(((x1 + x2) / 2), ((y1 + y2) / 2) + 10, text=alphabet1[letter], font=('Courier', 25))
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
            edges[alphabet2[letter]] = [vertexStart, vertexDestination]
        edgeNumber += 1
        clickNumber = 0   # We have a line drawn, go back and determine the x1, y1 start coords for the next line)
        letter += 1     # Next letter, eventually goes to lowercase


# Vertex Button
def vertexButtonSet():
    draw_space.unbind('<Button 1>')
    draw_space.tag_bind('vertex', '<Button-1>', addEdge)  # tags used for clicking function, the declared variables in addVertex need the 'vertex' tag

# Edge Finish Button
def edgeButtonSet():
    global adjacencyMatrix
    adjacencyMatrix = [[0] * (vertexNumber-10) for x in range(vertexNumber-10)]  # Must use list comprehension, [[0] * n] * m is just a list of references to [0]*n and will change everything
    # Fill adjacency matrix with zeros
    draw_space.unbind('<Button 1>')

# Input button next to entry field for getting weights
def addEdgeWeight():
    global adjacencyMatrix
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
                adjacencyMatrix[edges[edgeName][0] - 1][edges[edgeName][1] - 1] = weight  # -1 because lists in reality, start from 0
                adjacencyMatrix[edges[edgeName][1] - 1][edges[edgeName][0] - 1] = weight  # Reversed here, can travel edges both ways b/c its an undirected graph
        point1 = vertexes[edges[edgeName][0]]  # Storing vertexes{} points from edges{} for x1,x2,y1,y2
        point2 = vertexes[edges[edgeName][1]]  # e.g. [359.0, 448.0, 530.0, 343.0]
        x1, y1, x2, y2 = point1[0], point1[1], point2[0], point2[1]  # e.g. 359.0y2 = point2[1]
        if ((x1 < x2) and (y1 < y2)) or ((x1 > x2) and (y1 > y2)):   # Get Edge labeling correct, if same do one way, if different, do other way
            draw_space.create_text((((x1 + x2) / 2) + 20), (((y1 + y2) / 2) - 20), text=weight, font=('Courier', 15))
        elif ((x1 > x2) and (y1 < y2)) or ((x1 < x2) and (y1 > y2)):
            draw_space.create_text(((x1 + x2) / 2) + 10, ((y1 + y2) / 2) + 10, text=weight, font=('Courier', 15))
        else:
            draw_space.create_text(((x1 + x2) / 2) + 10, ((y1 + y2) / 2) + 10, text=weight, font=('Courier', 15))

#def dijkstra(graph, start, end):   # Takes adjacencyMatrix, start vertex(as a number), end vertex(as a number)
    #Catch error handling
    #inputValues = re.sub('[^0-9a-zA-Z]+', ' ', inputValues).split()
    #global adjacencyMatrix
    #get two vertexes user wants
    #dijkstra on adjacency matrix
    #Throw error for non-existant vertex, or no-connection possible between the two vertexes, or allow user to addEdgeWeight() to fix it
    #Print a label with shortest path under last widget, keep appending and placing under the last path, see format below
    # show "Shortest path value: Distance: x  Path: A->B->C->D"

####################
# Window / Widgets #
####################
root = Tk()
root.title("Dijkstra's Canvas - @KyleTimmermans")
draw_space = Canvas(root, width=1500, height=1000, background='Floral White')  # Canvas for drawing, make dynamic sizing in the future
draw_space.pack()

draw_space.bind('<Button-1>', addVertex)  # Bind addVertex to mouse1 to Begin Program

# Widgets
### We have 10 widgets, they take up first ten ID Numbers, so start vertexNumber at 10
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
shortpathButton = Button(text='Show Result', background='Floral White')    # Short Path Button
draw_space.create_window(671, 165, window=shortpathButton)  # Draw Short Path Button

root.mainloop()  # Keep window open and loop all its functions

###########
# Testing #
###########
print(vertexes)  # Testing purposes, storing vertex locations
print(edges)     # Testing purposes, storing edges and where they start/end
print(adjacencyMatrix)