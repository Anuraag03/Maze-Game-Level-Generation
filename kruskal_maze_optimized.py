import tkinter as tk
import numpy as np
import random
# Your maze generation code goes here...

def generateKruskalMaze(x: int, y: int):
  """generate a random maze with kruskal's algorithm of a given size
     * 0 = green dot e.g. wall
     * 1 = white dot e.g. cell (graph node)
     * 2 = black cell, will be transformed to green or white (graph link)

  Args:
      x (int): x-size of the maze
      y (int): y-size of the maze

  Returns:
      list: 2 dimensional array with 0 (wall) and 1 (cell) representing the maze
  """
  # maze skeleton
  maze = np.tile([[1, 2], [2, 0]], (y // 2 + 1, x // 2 + 1))
  # Strip last element of x and y to make it flipable
  maze = maze[:-1, :-1]
  
  # get disct of coodinates of all cells and all walls
  cells = {(i, j): (i, j) for i, j in np.argwhere(maze == 1)}
  walls = np.argwhere(maze == 2)

  # subroutine union-find
  def find(p: int , q: int):
    """find parent x-y cell of given cell p-q

    Args:
        p (int): location x of cell to locate
        q (int): location y of cell to locate

    Returns:
        list: x-y location of parent cell
    """
    # if x,y not parent cell
    if p != cells[p] or q != cells[q]:
      # get parent cell
      cells[p], cells[q] = find(cells[p], cells[q])
    return cells[p], cells[q]

  # randomly shuffle the walls to so the maze will be different each time
  np.random.shuffle(walls)
  
  # find spanning tree
  for wi, wj in walls:
    if wi % 2:          # black dots on even rows union-find left right neighbors
      p, q = find((wi - 1, wj), (wi + 1, wj))
    else:               # black dots on uneven rows union-find up down neighbors
      p, q = find((wi, wj - 1), (wi, wj + 1))

    # update cell value
    maze[wi, wj] = p != q
    if p != q:
      cells[p] = q

  return maze

def createBorder(maze: list):
  """Create boarder around the maze
  """
  ## make border of the maze walls
  maze[0] = 0
  maze[-1] = 0
  maze[:, 0] = 0
  maze[:, -1] = 0

  return maze







def generateKruskalMazeWithStartAndEnd(x: int, y: int):
    maze = generateKruskalMaze(x, y)  # Generate the maze using your existing function

    # Find solvable start and end points
    start = (1, 1)
    end = (y - 2, x - 2)
    
    # Find random solvable start point
    while maze[start] == 0:
        start = (random.randint(1, y - 2), random.randint(1, x - 2))
    
    # Find random solvable end point
    while maze[end] == 0 or end == start:
        end = (random.randint(1, y - 2), random.randint(1, x - 2))

    # Assign start and end cells
    maze[start] = 3  # Assuming 3 represents the starting cell
    maze[end] = 4    # Assuming 4 represents the ending cell

    return maze, start, end

# Display the maze with random start and end points
  # Example size, adjust as needed

# Display function remains the same
def display_maze_with_start_and_end(maze, start, end):
    root = tk.Tk()
    root.title("Maze")

    canvas = tk.Canvas(root, width=800, height=800)  # Adjust window size as needed
    canvas.pack()

    rows, cols = len(maze), len(maze[0])

    # Calculate cell size based on maze dimensions
    cell_size = min(800 // rows, 800 // cols)  # Adjust window size (800) as needed

    colors = {0: "black", 1: "white", 3: "red", 4: "green"}  # Color mapping for wall, cell, start, and end

    for i in range(rows):
        for j in range(cols):
            x0, y0 = j * cell_size, i * cell_size
            x1, y1 = x0 + cell_size, y0 + cell_size
            canvas.create_rectangle(x0, y0, x1, y1, fill=colors[maze[i][j]])

    root.mainloop()

