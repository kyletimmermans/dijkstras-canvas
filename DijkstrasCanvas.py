'''
Kyle Timmermans
March 18th, 2020
python v3.8.2
'''

# Vertex's must be created first, then edges, 'Done' buttons

# Adjacency matrix (2D Array) to store adjacency
# Do I make it so that the user input length changes the weigth or just the distance of edge is automatic?

from tkinter import *

vertexNumber = 1    # To be made global later, just initialized here as ??? because we have buttons and text boxes already init, id's for shapes start to assign at 1
#### ^^ this value will change when we add some buttons, text boxes, and a title
helperNumber = 1
edgeNumber = vertexNumber  # Continue numbering shapes after vertexes are placed
clickNumber = 0     # Start click number at 0, i.e. start first of 2 clicks to make line
vertexes = {}       # Store vertex number and its location
edges = {}          # Store edge and its location
adjacencyMatrix = []  # 2D Array to hold weights of edges between vertexes, if they exist

def addVertex(event):
    global vertexNumber   # Grab vertexNumber from earlier, it is now global, no need to pass it through as a param now
    global helperNumber   # # Need a dynamic number to add to vertex number
    x0 = event.x    # Current X-Coord for mouse click
    y0 = event.y    # Current Y-Coord for mouse click
    vertex = draw_space.create_oval(x0, y0, x0+50, y0+50, fill="Green", tags="vertex")  # Create the vertex, give it a function soon to add to the dictionary
    vertex_text = draw_space.create_text((x0+25, y0+25), text=vertexNumber, tags="vertex")  # +25 to get to the center of a 50 circle
    draw_space.pack()
    if vertexNumber == 1:  # ID's go up by odd numbers b/c be are essentially creating two objects, the circle and its textbox label
        vertexes[vertexNumber] = draw_space.coords(vertexNumber)   # Coords just going with continuity of id's auto-assigning
    else:
        vertexes[vertexNumber] = draw_space.coords(vertexNumber+helperNumber)  ##### Maybe not use .coords but just ID??
        helperNumber += 1  # increment and add to vertex labels so we get just the vertex circle, place here because we want it to start adding after VN=1
    vertexNumber += 1  # increment vertex labels

def addEdge(event):  # Why does *args work for this?
    global clickNumber
    global edgeNumber
    global x1, y1
    if clickNumber == 0:  # start pos before mouse is clicked
        x1 = event.x   # start x pos of mouse
        y1 = event.y   # start y pos of mouse
        clickNumber = 1   # On next click, define x2, y2
    else:                  # end coords when mouse is unlicked
        x2 = event.x    # end x pos of mouse
        y2 = event.y    # end y pos of mouse
        line = draw_space.create_line(x1, y1, x2, y2, fill='Black', width=5)   # Draw line with those coords
        if ((x1 < x2) and (y1 < y2)) or ((x1 > x2) and (y1 > y2)):  # Get Edge labeling correct, if same do one way, if different, do other way
            line_text = draw_space.create_text(((x1 + x2) / 2) - 10, ((y1 + y2) / 2) + 10, text='A', font=("Courier", 25))
        elif ((x1 > x2) and (y1 < y2)) or ((x1 < x2) and (y1 > y2)):
            line_text = draw_space.create_text(((x1+x2)/2)+10, ((y1+y2)/2)+10, text='A', font=("Courier", 25))
        draw_space.pack()  # Pack into canvas and give unique ID
        # for
        edgeNumber += 1
        clickNumber = 0   # We have a line drawn, go back and determine the x1, y1 start coords for the next line)

root = Tk()
root.title("Dijkstra's Canvas - @KyleTimmermans")
draw_space = Canvas(root, width=1000, height=1000, background='white')  # Canvas for drawing, make dynamic sizing in the future
draw_space.grid(row=0, column=0)  # Give the canvas coordinates

# Do while not, not next step
# draw_space.create_text(top left corner, "Input Vertexes by left clicking mouse")
#create_button(top left corner next to this msg^^, "Done"), onclick we can now add edges
draw_space.bind('<Button-2>', addVertex)  # Bind addVertex to mouse2, binded func's can only have event as parameter

# draw_space.create_text(top right corner, "Input Edges by left clicking the start vertex and then the destination vertex")
# Do while not, next step, reassign button 1 to new function
# create_button(top left corner next to this msg^^, "Done"), onclick, we can now input the shortest path we want
draw_space.tag_bind('vertex', '<Button-1>', addEdge)  # tags used for clicking function, the declared variables in addVertex need the 'vertex' tag

# Unbind all buttons
# Input weight to edges and insert textbox weights next to edges on graph

# Input two numbers of Nodes
# Output chosen nodes' shortest path to each other
root.mainloop()


print(vertexes)  # Testing purposes, storing vertex locations
print(edges)     # Testing purposes, storing edges and where they start/end
