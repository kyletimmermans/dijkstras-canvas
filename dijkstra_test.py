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

dict = {}
x0, y0 = 100, 100
dict['1']=(x0,y0,x0+50,y0+51)
dict['2']=(x0,y0,x0+100,y0+101)

print(dict)
print("")
# Tuples store coords and act as a single value to a single key in the dictionary
# Tuples start at 0 and end at n-1

if (dict['1'][1] == dict['2'][1]) is True:
    print("This is working")

print("")

if (dict['1'][3] == dict['2'][3]) is False:
    print("Oh yeah, its definitely working")