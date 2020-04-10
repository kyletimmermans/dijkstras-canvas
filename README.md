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
   * [Who is Dijkstra?](#who-is-dijkstra)
      * [Dijkstra's Algorithm](#dijkstras-algorithm)
      * [Pseudocode](#pseudocode)
<!--te-->

<br/>

### Installation
1. If you don't already have Python 3 on your system, download the installer [here](https://www.python.org/downloads/ "Python Installer").
2. Run `git clone https://github.com/kyletimmermans/dijkstras-canvas/DijsktrasCanvas.py`
3. Run `python3 DijsktrasCanvas.py`

### Usage

### Example
Geeksforgeeks.org has a well-made undirected weighted graph image that I will use as an example and re-create it in Dijsktra's Canvas. 
If we are given a graph such as this one:
![alt text](https://github.com/kyletimmermans/dijkstras-canvas/blob/master/media/UndirectedWeightedGraph.png "Sample Graph")
