# <div align="center">Dijkstra's Canvas</div>

Dijsktra's Canvas is an application written in Python3 and Tkinter that allows users to draw a visual undirected weighted graph in the program's window. Using only the mouse, users can click where they want to place different vertex points. They can then draw edges from one vertex to another by first clicking on the source vertex, and then on the destination vertex, creating the connections. At this point, the user can now enter weights for the edges they drew to simulate distance between the vertex points. Finally, they can specify two vertex points, and have the program use Dijsktra's algorithm to find the shortest path between the specified points. The visual aspect of this program is solely created with Tkinter and does not use visual-graphing libraries such as networkx or matplotlib.

<br/>

Table of Contents
=================

<!--ts-->
   * [Installation](#installation)
   * [Usage](#usage)
      * [Example](#example)
      * [Error Handling](#error-handling)
   * [Who is Dijkstra?](#who-is-dijkstra?)
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
1. Right-click to enter Vertex points at any point in the window
2. Click the 'Done' Button and click from any vertex point to any other vertex point to create edges, then hit 'Done'
3. Input weights separated by commas and hit 'Input', e.g. A=7, B=8, C=9
4. Input two vertexes, a source and destination vertex. Then click 'Show Results' to see the Shortest Path between the two 
e.g. v1,v2

<br/>

### Example
Geeksforgeeks.org has a well-made undirected weighted graph image that I will use as an example and re-create it in Dijsktra's Canvas. 
If we are given a graph such as this one:

![alt text](https://github.com/kyletimmermans/dijkstras-canvas/blob/master/media/UndirectedWeightedGraph.png "Sample Graph")

Once the graph is initialized with all its vertexes, edges, and edge weights, the program will take all the data and create an "Adjacency Matrix" that the path finding algorithm can read and work on. The Adjacency Matrix for the example graph would look something like this:

![alt text](https://github.com/kyletimmermans/dijkstras-canvas/blob/master/media/adjacencyMatrix.png "Adjacency Matrix")

For instance, to get from point 0 to point 1, the distance is 4. We can see this in the first row of the 2D Array "adjancencyMatrix." Each row acts as a vertex, and each value in the row represents a distance to another vertex. The index of each value within each row represents the other vertexes. So adjacencyMatrix[0][1] is 4, from point 0 to point 1 has a distance of 4. Using that same logic, adjacencyMatrix[1][0] is also 4. Going backwards from point 1 to point 0 is still 4. This is how the entire matrix is built up, it is the way in which the program can interpret the visual data and find the shortest path of our sketched out graph.

<br/>

### Who is Dijktra?
Edsgar W. Dijkstra was a famous Dutch physicist, mathematician, and computer science pioneer who spent most of his life in a small Netherlands town known as Nuenen.

### Dijkstra's Algorithm
An algorithm used to find the shortest paths from a given source node, to all other nodes in a graph. He is the reason why this program was possible.

### Pseudocode
This is the backbone behind his algorithm
![alt text](https://github.com/kyletimmermans/dijkstras-canvas/blob/master/media/pseudocode.png "Pseudocode")
