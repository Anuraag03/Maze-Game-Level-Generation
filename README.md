


# Game Level Generation - Generating Maze Puzzle Game Levels

This project focuses on generating maze puzzle game levels using Python. It employs various search algorithms like Kruskal's algorithm, Prim's algorithm, recursive backtracking, and Depth-First Search (DFS) to generate and ensure solvability of the maze.

## Languages and Tools Used
- Python
- Tkinter for GUI development

## Algorithms Implemented

### Kruskal's Algorithm
Kruskal's algorithm is a minimum-spanning-tree algorithm used to find a minimum spanning tree for a connected weighted graph. It operates by sorting the edges by weight and progressively adding them to the growing spanning tree if they don't create cycles.


![maxresdefault](https://github.com/Anuraag03/Maze-Game-Level-Generation/assets/95640377/95d61cd6-25a8-46a6-812a-e957ce0d0c3e)


### Prim's Algorithm
Prim's algorithm is another minimum spanning tree algorithm. It starts from an arbitrary vertex and grows the spanning tree by adding the minimum-weight edge at each step that connects the tree to a non-tree vertex.

![maxresdefault (1)](https://github.com/Anuraag03/Maze-Game-Level-Generation/assets/95640377/ad2f7248-514a-4143-813e-e44a307efb54)


### Recursive Backtracking
Recursive backtracking is a technique used to solve problems through exploration of all possible solutions, backtracking from dead ends, and continuing the search until the solution is found. In maze generation, recursive backtracking creates the maze by building and carving out paths.



### Depth-First Search (DFS)
DFS is an algorithm used for traversing or searching tree or graph data structures. In maze generation, DFS is used to ensure that the generated maze is solvable by checking for paths between the starting point and endpoint.

#### Code Snippet Example:


## Additional Resources
- [Kruskal's Algorithm - Wikipedia](https://en.wikipedia.org/wiki/Kruskal%27s_algorithm)
- [Prim's Algorithm - Wikipedia](https://en.wikipedia.org/wiki/Prim%27s_algorithm)
- [Depth-First Search - Wikipedia](https://en.wikipedia.org/wiki/Depth-first_search)

