'''
vertexText = Label(text='Input Vertexes by left clicking mouse: ', font=('Helvetica', 14), background='Floral White')  # Vertex Text
draw_space.create_window(165, 30, window=vertexText)  # Draw Vertex Text
vertexButton = Button(text='Done', command=vertexButtonSet, background='Floral White')  # Vertex Button
draw_space.create_window(355, 30, window=vertexButton)  # Draw Vertex Button
edgeText = Label(text='Input Edges by left clicking the start vertex and then the destination vertex: ', font=('Helvetica', 14), background='Floral White')  # Edge Text
draw_space.create_window(319, 75, window=edgeText)  # Draw Edge Text
edgeButton = Button(text='Done', command=edgeButtonSet, background='Floral White')  # Edge Button
draw_space.create_window(660, 75, window=edgeButton)    # Draw Edge Button
weightText = Label(text='Input the weights of edges between nodes e.g. A=7, B=8 (Case-Sensitive)', font=('Helvetica', 14), background='Floral White')  # Weight Text
draw_space.create_window(319, 120, window=weightText)   # Draw Weight Text
weightEntry = Entry(root)   # Weight Entry
draw_space.create_window(705, 120, window=weightEntry)  # Draw Weight Entry
weightInput = Button(text='Input', command=addEdgeWeight, background='Floral White')  # Weight Button
draw_space.create_window(800, 120, window=weightInput)   # Draw Weight Button
shortpathText = Label(text='Enter the two vertexes for the shortest path you want e.g. v2,v4', font=('Helvetica', 14), background='Floral White')  # Short Path Text
draw_space.create_window(270, 165, window=shortpathText)    # Draw Short Path Text
shortpathEntry = Entry(root)    # Short Path Entry
draw_space.create_window(605, 165, window=shortpathEntry)  # Draw Short Path Entry
shortpathButton = Button(text='Show Result', command=dijkstra, background='Floral White')    # Short Path Button
draw_space.create_window(715, 165, window=shortpathButton)  # Draw Short Path Button
resetButton = Button(text='Reset Canvas', command=resetGraph, background='Floral White')  # Reset Button
draw_space.create_window(539, 30, window=resetButton)  # Draw Reset Button
custFont = font.Font(family='Helvetica', size=15, weight='bold', underline=1)  # Custom Font
resultTitle = Label(text='Shortest Paths', font=custFont, background='Floral White')  # Result Title (Bold, Underlined)
draw_space.create_window(910, 20, window=resultTitle)  # Draw Result Title
separationLine = draw_space.create_line(0, 200, 1500, 200, fill='Black', width=1)  # Separation Line, needs .pack() b/c it's not a window
draw_space.pack()  # Pack in separationLine, ID#13, Final Static ID
'''

from tkinter import *
import aggdraw

draw = aggdraw.Dib("RGB", (1500, 1000), (255, 250, 240, 1))

def lineDraw():
    draw.line((500, 500, 900, 900), aggdraw.Pen("black", 5))
    draw.expose(hwnd=draw_space.winfo_id())
    draw_space.pack()

root = Tk()
root.title("Dijkstra's Canvas - @KyleTimmermans")
draw_space = Canvas(root, width=1500, height=1000, background="Floral White")  # Canvas for drawing, make dynamic sizing in the future
draw_space.pack()

vertexButton = Button(text='Done', command=lineDraw, background='Floral White')  # Vertex Button
draw_space.create_window(355, 30, window=vertexButton)  # Draw Vertex Button
separationLine = draw_space.create_line(0, 200, 1500, 200, fill='Black', width=1)  # Separation Line, needs .pack() b/c it's not a window
draw_space.pack()  # Pack in separationLine, ID#13, Final Static ID


root.mainloop()
