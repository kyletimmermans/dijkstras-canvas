'''
from tkinter import *

def addEdge(event):
    global click_number
    global x1, y1
    if click_number == 0:  # start pos before mouse is clicked
        x1 = event.x   # start x pos of mouse
        y1 = event.y   # start y pos of mouse
        click_number = 1   # On next click, define x2, y2
    else:                  # end coords when mouse is unlicked
        x2 = event.x    # end x pos of mouse
        y2 = event.y    # end y pos of mouse
        draw_space.create_line(x1, y1, x2, y2, fill='black', width=10)   # Draw line with those coords
        click_number = 0   # We have a line drawn, go back and determine the x1, y1 start coords for the next line

root = Tk()
root.title("Dijkstra's Canvas by Kyle")
draw_space = Canvas(root, width=1000, height=1000, background='white')  # Canvas for drawing, make dynamic sizing in the future
draw_space.grid(row=0, column=0)  # Give the canvas coordinates
draw_space.bind('<Button-1>', addEdge)  # Bind addEdge to mouse1
click_number = 0
root.mainloop()
'''

'''
from tkinter import Tk, Canvas

window = Tk()

c = Canvas(window, width=300, height=300)

def clear():
    canvas.delete(ALL)

def clicked(*args):
    print("You clicked play!")

playbutton = c.create_rectangle(75, 25, 225, 75, fill="red",tags="playbutton")
playtext = c.create_text(150, 50, text="Play", font=("Papyrus", 26), fill='blue',tags="playbutton")

c.tag_bind("playbutton", "<Button-1>", clicked)

c.pack()

window.mainloop()
'''

'''
example_graph = {
    'U': {'V': 2, 'W': 5, 'X': 1},
    'V': {'U': 2, 'X': 2, 'W': 3},
    'W': {'V': 3, 'U': 5, 'X': 3, 'Y': 1, 'Z': 5},
    'X': {'U': 1, 'V': 2, 'W': 3, 'Y': 1},
    'Y': {'X': 1, 'W': 1, 'Z': 1},
    'Z': {'W': 5, 'Y': 1},
}

print(example_graph)


from tkinter import *

root = Tk()
draw_space = Canvas(root, width=1000, height=1000, background='white')  # Canvas for drawing, make dynamic sizing in the future


draw_space.create_oval(50, 50, 500, 500, fill="green", tags='lel')
draw_space.create_line(50, 200, 900, 700, fill='black', width=10)
draw_space.create_line(50, 300, 900, 700, fill='black', width=10)

draw_space.pack()

result = draw_space.find_overlapping(50, 50, 500, 500)
print(result)

draw_space.grid(row=0, column=0)  # Give the canvas coordinates
root.mainloop()
'''

'''
dict = {}
x0, y0 = 100, 100
vertexNumber = 0
dict[vertexNumber]=(x0,y0,x0+50,y0+51)
dict['2']=(x0,y0,x0+100,y0+101)

print(dict)
print("")
# Tuples store coords and act as a single value to a single key in the dictionary
# Tuples start at 0 and end at n-1

if (dict[vertexNumber][1] == dict['2'][1]) is True:
    print("This is working")

print("")

if (dict[vertexNumber][3] == dict['2'][3]) is False:
    print("Oh yeah, its definitely working")
'''

'''
vertexes = {1: [400.0, 400.0, 450.0, 450.0]}

for key in vertexes:
    print(vertexes[key][0])
'''

'''
from tkinter import *

root = Tk()
root.title("Dijkstra's Canvas - @KyleTimmermans")
draw_space = Canvas(root, width=1000, height=1000, background='white')  # Canvas for drawing, make dynamic sizing in the future
draw_space.grid(row=0, column=0)  # Give the canvas coordinates

circle = draw_space.create_oval(280, 280, 330, 330, fill="Green")
circle2 = draw_space.create_oval(480, 480, 530, 530, fill="Green")
line = draw_space.create_line(300, 300, 500, 500, width=5, fill="Black")
draw_space.pack()
vertexes = {1: (280, 280, 330, 330), 2: (480, 480, 530, 530)}
edgeNumber = 1
edges = {}

print("Coords of Circle: ", end='')
print(draw_space.coords(circle))
print("Coords of Circle2: ", end='')
print(draw_space.coords(circle2))
print("Coords of Line: ", end='')
print(draw_space.coords(line))
print("ID of Circle: ", end='')
print(circle)
print("ID of Circle2: ", end='')
print(circle2)
print("ID of Line: ", end='')
print(line)
print("")

x1, y1 = 300, 300
x2, y2 = 500, 500


# Checking if first part of line is in a vertex
for key in vertexes:
    if (vertexes[key][0] < x1 < vertexes[key][2]) == True:
        vertexStart = key

for key in vertexes:
    if (vertexes[key][0] < x2 < vertexes[key][2]) == True:
        vertexDestination = key

edges[edgeNumber] = (vertexStart, vertexDestination)
root.mainloop()
print(edges)
'''

from tkinter import *
import re

vertexNumber = 2
adjacencyMatrix = [[0]*2 for _ in range(vertexNumber)]


def func():
    global adjacencyMatrix
    x = weightEntry.get()
    x = re.sub('[^0-9]+', ' ', x).split()
    vertex1, vertex2, weight = int(x[0]), int(x[1]), int(x[2])
    adjacencyMatrix[vertex1 - 1][vertex2 - 1] = weight


root = Tk()
root.title("Dijkstra's Canvas - @KyleTimmermans")
draw_space = Canvas(root, width=1500, height=1000, background='white')  # Canvas for drawing, make dynamic sizing in the future
draw_space.pack()

weightEntry = Entry(root)   # Weight Entry
draw_space.create_window(462, 120, window=weightEntry)  # Draw Weight Entry
weightInput = Button(text="Input", command=func)  # Weight Button
draw_space.create_window(592, 120, window=weightInput)   # Draw Weight Button

root.mainloop()  # Keep window open and loop all its functions

print(adjacencyMatrix)
