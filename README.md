![Version 3.0](https://img.shields.io/badge/version-v3.0-orange.svg)
![Python 3.9](https://img.shields.io/badge/python-3.9-blue.svg)
![Last Updated](https://img.shields.io/github/last-commit/kyletimmermans/dijkstras-canvas?color=success)
[![kyletimmermans Twitter](http://img.shields.io/twitter/url/http/shields.io.svg?style=social&label=Follow)](https://twitter.com/kyletimmermans)


# <div align="center">Dijkstra's Canvas</div>

Dijkstra's Canvas is an application written in Python3 and Tkinter that allows users to draw a visual undirected weighted graph in the program's window. Using only the mouse, users can click where they want to place different vertex points. They can then draw edges from one vertex to another by first clicking on the source vertex, and then on the destination vertex, creating the connections. At this point, the user can now enter weights for the edges they drew to simulate distance between the vertex points. Finally, they can specify two vertex points, and have the program use Dijkstra's algorithm to find the shortest path between the specified points. The visual aspect of this program is solely created with Tkinter and does not use visual-graphing libraries such as networkx or matplotlib.

<p align="center">
  <img src="https://github.com/kyletimmermans/dijkstras-canvas/blob/master/media/final_screenshot3.png?raw=true" alt="Dijkstra's Canvas"/>
</p>


</br>


### Updated v3.0 look with dark mode
<p align="center">
  <img src="https://github.com/kyletimmermans/dijkstras-canvas/blob/master/media/newlook2.png?raw=true" alt="v3.0 Dark Mode Look"/>
</p>


<br/>

Table of Contents
=================

<!--ts-->
   * [Installation](#installation)
   * [Changelog](#changelog)
   * [Usage](#usage)
      * [Features](#features)
      * [Example](#example)
      * [Adjacency Matrix](#adjacency-matrix)
      * [Algorithm Implementation](#algorithm-implementation)
      * [Error Handling](#error-handling)
   * [Who is Dijkstra?](#who-is-dijkstra)
      * [Dijkstra's Algorithm](#dijkstras-algorithm)
      * [Pseudocode](#pseudocode)
   * [Fun](#fun)
      * [???](#fun)
<!--te-->

<div>&ensp;</div>

### Installation
Download DijkstrasCanvas.zip which contains the .app file [here](https://github.com/kyletimmermans/dijkstras-canvas/files/6977352/Dijkstra.s.Canvas.zip)
  -Packaged with Platypus


Running Dijkstra's Canvas through command line:
1. If you don't already have Python 3 on your system, download the installer [here](https://www.python.org/downloads/ "Python Installer").
2. Run `wget https://raw.githubusercontent.com/kyletimmermans/dijkstras-canvas/master/DijkstrasCanvas.py`
3. Run `python3 DijsktrasCanvas.py`

<div>&ensp;</div>

### Changelog
<div>v1.0: Initial-Relase</div>
<div>v1.1:</div>
<div>&ensp;&ensp;-Fixed lots of user-input related bugs</div>
<div>&ensp;&ensp;-Fixed edge weight number printing, no longer prints edge weight numbers inside of or on top of lines</div>
<div>&ensp;&ensp;-Added 'Reset Canvas' Button</div>
<div>v1.2:</div>
<div>&ensp;&ensp;-Added Canvas-Buttons separation line</div>
<div>&ensp;&ensp;-Can only have so many shortest path results (8 results) before it reaches the separation line</div>
<div>&ensp;&ensp;-Added more Error Handling</div>
<div>&ensp;&ensp;-Minor bug fixes</div>
<div>v1.3:</div>
<div>&ensp;&ensp;-Added automatic geometry fix for creating edges, no more edges overlapping vertexes</div>
<div>&ensp;&ensp;-Bug fixes</div>
<div>v1.4:</div>
<div>&ensp;&ensp;-Optimization fixes</div>
<div>&ensp;&ensp;-Minor bug fixes</div>
<div>v2.0:</div>
<div>&ensp;&ensp;-Added Windows compatibility</div>
<div>&ensp;&ensp;-Fixed edge weight placement being too far away in some cases</div>
<div>&ensp;&ensp;-Fixed UnboundLocalError: local variable 'vertexDestination' referenced before assignment</div>
<div>&ensp;&ensp;-Fixed ZeroDivisonError in class circleEdgePoint</div>
<div>&ensp;&ensp;-Fixed key error with non-existant edges</div>
<div>&ensp;&ensp;-Fixed addEdgeWeight() input sanitation</div>
<div>&ensp;&ensp;-Fixed dijkstra() input sanitation</div>
<div>&ensp;&ensp;-Fixed NSAlert runModal error on MacOSX when trying to re-size window on x-axis</div>
<div>v2.1:</div>
<div>&ensp;&ensp;-Code cleanup, wrapped lots of math into classes. Deprecated Windows version b/c no anti-aliasing</div>
<div>&ensp;&ensp;-Fixed resize window issue</div>
<div>&ensp;&ensp;-Windows Binary still available</div>
<div>v2.2:</div>
<div>&ensp;&ensp;-Fixed 'sys' module not being recognized</div>
<div>&ensp;&ensp;-Removed binaries from relases, better to compile per machine basis</div>
<div>v3.0</div>
<div>&ensp;&ensp;-Update tkinter code to follow Python3.9</div>
<div>&ensp;&ensp;-Using tkmacosx library to have widgets look more native</div>
<div>&ensp;&ensp;-MacOSX 'Dark Mode' compliant</div>
<div>&ensp;&ensp;-Added app version to window header</div>
<div>&ensp;&ensp;-Added root window geometry for proper window placement</div>



</br>

### Usage
1. Right-click to enter Vertex points at any point in the window, and hit the 'Done' Button next to the input field
2. Now you can click from any vertex point to any other vertex point to create edges, then hit the second 'Done' Button
3. Input weights separated by commas and hit 'Input', e.g. A=7, B=8, C=9
4. Input two vertexes (source and destination. Then click 'Show Results' to see the Shortest Path between the two e.g. v1,v2
5. Hit the 'Reset Canvas' Button at any point, to remove the graph and all its elements to start over again

<br/>

Video of Dijkstra's Canvas in action! [https://youtu.be/_1Sd_68PKYE](https://youtu.be/_1Sd_68PKYE)

<br/>

### Features

|Features:|
|-------|
|Reset Canvas Button: Reset the entire graph and start from scratch|
|Forward and Reverse Path Finding: Go from v1,v2 or from v2,v1 and get its traversal path in reverse!|
|Automatic Edge Fix: Click on one vertex and then another, the resulting line will always be drawn from the outer-circumference of both vertexes, and it will never overlap the vertex. It is only drawn from the circumference of the vertex, making edges a breeze!|
|Available for MacOSX (.app): A GUI has been specifically crafted for MacOSX through testing and developing around the OS's rendering system, making Dijkstra's Canvas look like a native app!|

</br>

### Example
Geeksforgeeks.org has a well-made undirected weighted graph image that I will use as an example and re-create it in Dijsktra's Canvas. 
If we are given a graph such as this one:

<p align="center">
  <img src="https://github.com/kyletimmermans/dijkstras-canvas/blob/master/media/UndirectedWeightedGraph.png?raw=true" alt="Sample Graph"/>
</p>

We can draw the same graph in the program and give it the same edge weights.

<p align="center">
  <img src="https://github.com/kyletimmermans/dijkstras-canvas/blob/master/media/GraphTranslation2.png?raw=true" alt="Graph Translation"/>
</p>

### Adjacency Matrix
Once the graph is initialized with all its vertexes, edges, and edge weights, the program will take all the data and create an "Adjacency Matrix." A data structure that the path finding algorithm can read and work with. The Adjacency Matrix for the example graph would look something like this:

<p align="center">
  <img src="https://github.com/kyletimmermans/dijkstras-canvas/blob/master/media/adjacencyMatrix.png?raw=true" alt="Adjacency Matrix"/>
</p>

For instance, to get from node 0 to node 1, the distance is 4. We can see this in the first row of the 2D Array "adjancencyMatrix." Each row acts as a vertex, and each value in the row represents a distance to another vertex. The index of each value within each row represents the other vertexes. So adjacencyMatrix[0][1] is 4, from node 0 to node 1 has a distance of 4. Using that same logic, adjacencyMatrix[1][0] is also 4. Going backwards from point 1 to point 0 is still 4. This is how the entire matrix is built up, it is the way in which the program can interpret the visual data and find the shortest path of our sketched out graph. If adjacencyMatrix[x][y] = 0, then it indicates that there is no immediate edge/connection between the two points.

<br/>

### Algorithm Implementation

From the start vertex (row), we look for the smallest value in that row. We move to the next vertex which is the index of the smallest value. From there, we find the next smallest value in that row, if the smallest value in this row points to the last vertex (row) or any previously visted vertex (row), we can't use that one and we look for the next smallest value. Rinse and repeat until the smallest path is found.

<br/>

### Error Handling
1. Can't place vertexes beyond the allowed canvas space, only below separation line
2. Can't place an edge from a vertex to itself
3. Can't have more than 52 edges, edge labeling system uses A-Z and when that runs out, a-z (26+26)
4. Can't give edge weights for non-existant edges
5. When trying to get the shortest path of two vertexes, will check to see if the two entered vertexes exist
6. Shortest path of two vertexes and they are the same, e.g. v1,v1. Will return "Path = None | Distance = 0"
7. Shortest path of two vertexes that are not connected at some point on the graph, will return "No Connection Found"
8. If the "Shortest Paths" results bank gets too close to the Canvas Separation Line, it will remove the prior short path results and print the current short path result at the top, clearing the bank
9. Can't draw an edge if its source and destination vertex are the same
10. Edge weights can't be greater than 999, can't be 0, a negative number, or a float value

<br/>

### Who is Dijkstra?
Edsgar W. Dijkstra was a famous Dutch physicist, mathematician, and computer science pioneer who spent most of his life in a small Netherlands town known as Nuenen. Dijkstra was a professor at two prestigious universities, was a fellow for research boards, and held several awards such as the ACM A.M. Turing Award. He is the reason why this program was possible.

<br/>

### Dijkstra's Algorithm
An algorithm created by Dijkstra, that is used to find the shortest paths from a given source node, to all other nodes in a graph. 

<br/>

### Pseudocode
This is the backbone behind his algorithm
![alt text](https://github.com/kyletimmermans/dijkstras-canvas/blob/master/media/pseudocode.png "Pseudocode")

<br/>

### Fun

<p align="center">
  <img src="https://github.com/kyletimmermans/dijkstras-canvas/blob/master/media/fun1.png?raw=true" alt="Dijkstra's Canvas"/>
</p>

<div>&ensp;</div>

<p align="center">
  <img src="https://github.com/kyletimmermans/dijkstras-canvas/blob/master/media/fun2.png?raw=true" alt="Dijkstra's Canvas"/>
</p>

<div>&ensp;</div>

<p align="center">
  <img src="https://github.com/kyletimmermans/dijkstras-canvas/blob/master/media/fun3.png?raw=true" alt="Dijkstra's Canvas"/>
</p>
