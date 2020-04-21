from tkinter import *
from math import sqrt

# This point lies on the edge of the circle so there's no line overhang on the green vertex (cuts off extra overlap)
class circleEdgePoint:
    def __init__(self, x1, y1, x2, y2, r):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.r = r
    def cx(self):
        return self.x1 + (self.r * (self.x2 - self.x1) / sqrt((self.x2 - self.x1) + (self.y2 - self.y1)))  # Needs the multiplication asterisk
    def cy(self):
        return self.y1 + (self.r * (self.y2 - self.y1) / sqrt((self.x2 - self.x1) + (self.y2 - self.y1)))
    def final(self):
        return [round(self.cx(), 1), round(self.cy(), 1)]  # Return x,y of C-coord as a list, round() to nearest tenths place, e.g. 7.1

points = circleEdgePoint(5, 10, 15, 20, 5)   # Example points
print(points.final())  # need to use member function .final() to get the points


root = Tk()
root.title("Dijkstra's Canvas - @KyleTimmermans")
draw_space = Canvas(root, width=1500, height=1000, background='Floral White')  # Canvas for drawing, make dynamic sizing in the future
draw_space.pack()
x0, y0 = 700, 700
x1, y1 = 400, 500
circle1 = draw_space.create_oval(x0 - 25, y0 - 25, x0 + 25, y0 + 25, fill='Green', tags='vertex')
circle2 = draw_space.create_oval(x1 - 25, y1 - 25, x1 + 25, y1 + 25, fill='Red', tags='vertex')

# The Math Magic is going to be here #

line = draw_space.create_line(x0-22, y0-10, x1+22, y1+10, fill='Black', width=5, tags='edge')  # Do the inverse of what you did to x0,y0 to x1,y1 (at least in this case)
draw_space.pack()

root.mainloop()
