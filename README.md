


# Game Level Generation - Generating Maze Puzzle Game Levels

This project focuses on generating maze puzzle game levels using Python. It employs various search algorithms like Kruskal's algorithm, Prim's algorithm, recursive backtracking, and Depth-First Search (DFS) to generate and ensure solvability of the maze.

## Languages and Tools Used
- Python
- Tkinter for GUI development

## Aim Of the Project

A python script that can procedurally generate solvable game levels for a maze puzzle game by utlizing Artificial Intelligence Search Algorithms 

## Algorithms Implemented

### Kruskal's Algorithm
Kruskal's algorithm is a minimum-spanning-tree algorithm used to find a minimum spanning tree for a connected weighted graph. It operates by sorting the edges by weight and progressively adding them to the growing spanning tree if they don't create cycles.


![maxresdefault](https://github.com/Anuraag03/Maze-Game-Level-Generation/assets/95640377/95d61cd6-25a8-46a6-812a-e957ce0d0c3e)


### Prim's Algorithm
Prim's algorithm is another minimum spanning tree algorithm. It starts from an arbitrary vertex and grows the spanning tree by adding the minimum-weight edge at each step that connects the tree to a non-tree vertex.

![maxresdefault (1)](https://github.com/Anuraag03/Maze-Game-Level-Generation/assets/95640377/ad2f7248-514a-4143-813e-e44a307efb54)


### Recursive Backtracking
Recursive backtracking is a technique used to solve problems through exploration of all possible solutions, backtracking from dead ends, and continuing the search until the solution is found. In maze generation, recursive backtracking creates the maze by building and carving out paths.

![recursive backtrack](https://github.com/Anuraag03/Maze-Game-Level-Generation/assets/95640377/63588416-c17a-4eed-98b8-b5737ce150fa)


### Depth-First Search (DFS)
DFS is an algorithm used for traversing or searching tree or graph data structures. In maze generation, DFS is used to ensure that the generated maze is solvable by checking for paths between the starting point and endpoint.

## GUI 

![gui](https://github.com/Anuraag03/Maze-Game-Level-Generation/assets/95640377/e05a501c-aafe-498b-9ab9-e2c0317a7419)

## Directions to Run the Script

To run the script, follow these steps:

### Step 1: Install Tkinter and Numpy

Ensure you have Tkinter installed. Tkinter usually comes pre-installed with Python. However, if you encounter any issues, you can install it using pip:

```bash
pip install tk
pip install numpy
```
### Step 2: Run the Script
Run the main.py file in your Python environment. This file serves as the entry point for the maze level generation program.
```bash
python main.py
```

### Step 3: Enter Height and Width Values and generate Mazes
![gui1](https://github.com/Anuraag03/Maze-Game-Level-Generation/assets/95640377/cb70c0ab-6ee1-41ec-a47a-0ac7950f88bb)

Red is the starting point and Green indicates the goal point / ending point.
- Kruskal's Algorithms Maze(example)
  
 ![kruskalmaze](https://github.com/Anuraag03/Maze-Game-Level-Generation/assets/95640377/7fae1c77-9d86-4c37-a128-e0079778713d)


- Prim's Algorithm Maze(example)

  ![prims](https://github.com/Anuraag03/Maze-Game-Level-Generation/assets/95640377/540aa952-6f9d-43aa-a510-385e84868032)

  
- Recursive Backtracking Algorithm Maze(example)
![recursive backtracking maze jpg](https://github.com/Anuraag03/Maze-Game-Level-Generation/assets/95640377/ae878896-0bec-4c12-b772-c2d894697652)

## Efficiency and Complexity analysis with Visualizations

### 1. Kruskal's Algorithm
- **Functionality**: Generates a maze by connecting passages and removing walls between cells.
- **Steps**:
    1. Create a grid of passages and walls.
    2. Randomly select walls and remove if they connect disjoint sets of cells.
- **Time Complexity**: O(E log E)
- **Space Complexity**: O(V + E)
  (v stands for vertices and E for edges)

### 2. Prim's Algorithm
- **Functionality**: Constructs a maze by adding the closest cell to an existing tree.
- **Steps**:
    1. Start with a single cell as the initial tree.
    2. Add the closest cell to the tree until all cells are included.
- **Time Complexity**: O(E log V)
- **Space Complexity**: O(V + E)

### 3. Recursive Backtracking Algorithm
- **Functionality**: Generates a maze by recursively exploring and backtracking.
- **Steps**:
    1. Randomly choose a direction and explore until reaching a dead-end.
    2. Backtrack and explore unvisited paths.
- **Time Complexity**: O(V + E)
- **Space Complexity**: O(V)

## Solvability Checking Algorithm

### Depth-First Search (DFS)
- **Functionality**: Finds a path between start and end cells in the maze.
- **Steps**:
    1. Recursively explore possible directions until reaching the end cell or a dead-end.
    2. Backtrack if a dead-end is reached.
- **Time Complexity**: O(V + E)
- **Space Complexity**: O(V)

## Comparative Analysis
- **Kruskal vs. Prim**:
    - Kruskal's performs better for dense graphs; Prim's for sparse graphs.
    - Kruskal's has higher time complexity but more random layouts.
    - Prim's creates more structured mazes.
- **Kruskal/Prim vs. Recursive Backtracking**:
    - Kruskal's and Prim's guarantee solvability; Recursive Backtracking may not.
    - Recursive Backtracking is faster but may have more dead-ends.

      Kruskal v/s Prim v/s Recusive Backtracking

Scatter Plot:
      
![sctterplot](https://github.com/Anuraag03/Maze-Game-Level-Generation/assets/95640377/71ae931b-0a30-468c-8f2e-c752b2474045)


Line Plot:

![lineplotfinal3](https://github.com/Anuraag03/Maze-Game-Level-Generation/assets/95640377/e2facae2-159a-467b-bce1-09555cdb2cec)


Heatmap :

![heatmapfinal3](https://github.com/Anuraag03/Maze-Game-Level-Generation/assets/95640377/deb59450-75ee-483c-a5ac-928c31f6640d)


Barchart :

![barchartfinal2](https://github.com/Anuraag03/Maze-Game-Level-Generation/assets/95640377/a278e7bc-3ef0-4987-918b-573b3e3b246b)


Box Plot:


![boxplotfinal1](https://github.com/Anuraag03/Maze-Game-Level-Generation/assets/95640377/ac4f4464-387a-4758-ae31-71c688d9a429)



The choice of algorithm depends on desired properties like solvability, maze complexity, and structure.

For detailed code implementations and usage examples, refer to the respective algorithm files.


## Additional Resources
- [Kruskal's Algorithm - Wikipedia](https://en.wikipedia.org/wiki/Kruskal%27s_algorithm)
- [Prim's Algorithm - Wikipedia](https://en.wikipedia.org/wiki/Prim%27s_algorithm)
- [Depth-First Search - Wikipedia](https://en.wikipedia.org/wiki/Depth-first_search)

