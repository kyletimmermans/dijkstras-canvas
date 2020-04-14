![Version 1.2](http://img.shields.io/badge/version-v1.2-orange.svg)
![Python 3.8](http://img.shields.io/badge/python-3.8-blue.svg)
[![kyletimmermans Twitter](http://img.shields.io/twitter/url/http/shields.io.svg?style=social&label=Follow)](https://twitter.com/kyletimmermans)


# <div align="center">Dijkstra's Canvas</div>

Dijsktra's Canvas is an application written in Python3 and Tkinter that allows users to draw a visual undirected weighted graph in the program's window. Using only the mouse, users can click where they want to place different vertex points. They can then draw edges from one vertex to another by first clicking on the source vertex, and then on the destination vertex, creating the connections. At this point, the user can now enter weights for the edges they drew to simulate distance between the vertex points. Finally, they can specify two vertex points, and have the program use Dijsktra's algorithm to find the shortest path between the specified points. The visual aspect of this program is solely created with Tkinter and does not use visual-graphing libraries such as networkx or matplotlib.

<p align="center">
  <img src="https://github.com/kyletimmermans/dijkstras-canvas/blob/master/media/finalGraph.png?raw=true" alt="Dijkstra's Canvas"/>
</p>


<br/>

Table of Contents
=================

<!--ts-->
   * [Installation](#installation)
   * [Usage](#usage)
      * [Example](#example)
      * [Adjacency Matrix](#adjacency-matrix)
      * [Error Handling](#error-handling)
   * [Changelog](#changelog)
   * [Who is Dijkstra?](#who-is-dijkstra)
      * [Dijkstra's Algorithm](#dijkstras-algorithm)
      * [Pseudocode](#pseudocode)
<!--te-->

<br/>

### Installation
1. If you don't already have Python 3 on your system, download the installer [here](https://www.python.org/downloads/ "Python Installer").
2. Run `git clone https://github.com/kyletimmermans/dijkstras-canvas/DijsktrasCanvas.py`
3. Run `python3 DijsktrasCanvas.py`

<br/>

### Usage
1. Right-click to enter Vertex points at any point in the window, and hit the 'Done' Button next to the input field
2. Now you can click from any vertex point to any other vertex point to create edges, then hit the second 'Done' Button
3. Input weights separated by commas and hit 'Input', e.g. A=7, B=8, C=9
4. Input two vertexes, a source and destination vertex. Then click 'Show Results' to see the Shortest Path between the two 
e.g. v1,v2
5. Finally, hit the 'Reset Canvas' Button to start over again and create a new graph

<br/>

### Example
Geeksforgeeks.org has a well-made undirected weighted graph image that I will use as an example and re-create it in Dijsktra's Canvas. 
If we are given a graph such as this one:

<p align="center">
  <img src="https://github.com/kyletimmermans/dijkstras-canvas/blob/master/media/UndirectedWeightedGraph.png?raw=true" alt="Sample Graph"/>
</p>

We can draw the same graph in the program and give it the same edge weights.

<p align="center">
  <img src="https://github.com/kyletimmermans/dijkstras-canvas/blob/master/media/exampleGraph.png?raw=true" alt="Example Graph"/>
</p>

### Adjacency Matrix
Once the graph is initialized with all its vertexes, edges, and edge weights, the program will take all the data and create an "Adjacency Matrix" that the path finding algorithm can read and work with. The Adjacency Matrix for the example graph would look something like this:

<p align="center">
  <img src="https://github.com/kyletimmermans/dijkstras-canvas/blob/master/media/adjacencyMatrix.png?raw=true" alt="Adjacency Matrix"/>
</p>

For instance, to get from point 0 to point 1, the distance is 4. We can see this in the first row of the 2D Array "adjancencyMatrix." Each row acts as a vertex, and each value in the row represents a distance to another vertex. The index of each value within each row represents the other vertexes. So adjacencyMatrix[0][1] is 4, from point 0 to point 1 has a distance of 4. Using that same logic, adjacencyMatrix[1][0] is also 4. Going backwards from point 1 to point 0 is still 4. This is how the entire matrix is built up, it is the way in which the program can interpret the visual data and find the shortest path of our sketched out graph. If adjacencyMatrix[x][y] = 0, then it indicates that there is no immediate edge/connection between the two points.

<br/>

### Error Handling

<br/>

### Changelog
<div>v1.0: Initial-Relase: One graph allowed, lots of possible user-input related bugs</div>
<div>v1.1:</div>
<div>&#9;-Fixed lots of user-input related bugs</div>
<div>&#9;-Fixed edge weight number printing, no longer prints edge weight numbers inside of or on top of lines</div>
<div>&#9;-Added 'Reset Canvas' Button</div>
<div>v1.2:</div>
<div>&#9;-Added Canvas-Buttons separation line</div>
<div>&#9;-Can only have so many results before it reaches the separation line</div>
<div>&#9;-Minor bug fixes</div>

</br>


### Who is Dijkstra?
Edsgar W. Dijkstra was a famous Dutch physicist, mathematician, and computer science pioneer who spent most of his life in a small Netherlands town known as Nuenen. Dijkstra was a professor at two prestigious universities, was a fellow for research boards, and held several awards such as the ACM A.M. Turing Award. He is the reason why this program was possible.

<br/>

### Dijkstra's Algorithm
An algorithm created by Dijkstra that is used to find the shortest paths from a given source node, to all other nodes in a graph. 

<br/>

### Pseudocode
This is the backbone behind his algorithm
![alt text](https://github.com/kyletimmermans/dijkstras-canvas/blob/master/media/pseudocode.png "Pseudocode")
