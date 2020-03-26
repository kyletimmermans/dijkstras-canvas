'''
Kyle Timmermans
March 18th, 2020
python v3.8.2
'''

# dictionary use for numbered vertex's and their stored coordinates?

from tkinter import *

vertexNumber = 0    # To be made global later, just initialized here as 0
clickNumber = 0     # Start click number at 0, i.e. start first of 2 clicks to make line
vertexes = {}    # Key: The Vertex Number, Value: (x0, y0, x0+50, y0+50)
edges = {}       # Key: The Vertex Number, Value: (x1, y1, x2, y2)



def addVertex(event):
    global vertexNumber   # Grab vertexNumber from earlier, it is now global, no need to pass it through as a param now
    x0 = event.x    # Current X-Coord for mouse click
    y0 = event.y    # Current Y-Coord for mouse click
    vertex = draw_space.create_oval(x0, y0, x0+50, y0+50, fill="Green", tags="vertex")  # Create the vertex, give it a function soon to add to the dictionary
    vertex_text = draw_space.create_text((x0+25, y0+25), text=vertexNumber, tags="vertex")  # +25 to get to the center of a 50 circle
    draw_space.pack()
    #weights[vertexNumber] = -1  # Initialize as -1 - means no edge (for now, might be added in addEdge)
    vertexNumber += 1

def addEdge(event):  # Why does *args work for this?
    global clickNumber
    global x1, y1
    if clickNumber == 0:  # start pos before mouse is clicked
        x1 = event.x   # start x pos of mouse
        y1 = event.y   # start y pos of mouse
        clickNumber = 1   # On next click, define x2, y2
    else:                  # end coords when mouse is unlicked
        x2 = event.x    # end x pos of mouse
        y2 = event.y    # end y pos of mouse
        draw_space.create_line(x1, y1, x2, y2, fill='Black', width=10)   # Draw line with those coords
        #for all vertexes, are x1 and y1 overlapping any of them?
            #for all vertexes except for the one above are x2 and y2 overlapping them
                #if yes for both, then the edge is between those two vertexes
        clickNumber = 0   # We have a line drawn, go back and determine the x1, y1 start coords for the next line

root = Tk()
root.title("Dijkstra's Canvas by Kyle")
draw_space = Canvas(root, width=1000, height=1000, background='white')  # Canvas for drawing, make dynamic sizing in the future
draw_space.grid(row=0, column=0)  # Give the canvas coordinates
draw_space.bind('<Button-2>', addVertex)  # Bind addVertex to mouse2, binded func's can only have event as parameter
draw_space.tag_bind('vertex', '<Button-1>', addEdge)  # tags used for clicking function, the declared variables in addVertex need the 'vertex' tag
root.mainloop()


