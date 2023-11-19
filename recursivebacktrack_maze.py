'''
The Recursive Backtracking algorithm is a method used to create mazes. It works by starting at a particular cell within a grid. It marks the current cell as visited and randomly chooses a neighboring cell that hasn't been visited yet.
If an unvisited neighbor is found, it moves to that cell and repeats the process, marking the new cell as visited. 
This continues until it reaches a dead-end where no unvisited neighbors are available. Upon reaching a dead-end, the algorithm backtracks to the most recently visited cell that has unvisited neighbors and explores those unvisited cells.
This process of exploring, marking as visited, and backtracking continues until all cells have been visited, generating a maze with interconnected pathways.
This algorithm heavily relies on recursion to explore the maze's pathways and backtrack when needed, ensuring all cells are visited and creating a maze with no loops or isolated sections.
'''
import tkinter as tk
import random
from collections import deque
CELL_WALL = 1
CELL_PASSAGE = 0
WINDOW_SIZE = 750
CELL_DISPLAY_FILL = 'black'
START_COLOR = 'red'
END_COLOR = 'green'

class RecursiveBacktrackingMaze:
    def __init__(self, width, height):
        self.maze_width = width 
        self.maze_height = height 
        self.maze = [[CELL_WALL for _ in range(self.maze_width)] for _ in range(self.maze_height)]
        self.root = tk.Tk()
        self.root.title('Maze Generation with Recursive Backtracking')
        self.canvas = tk.Canvas(self.root, width=WINDOW_SIZE, height=WINDOW_SIZE)
        self.canvas.pack()
        self.generate_maze_recursive(1, 1)
        self.assign_start_and_end()
        self.draw_maze()
        self.root.mainloop()
    def generate_maze(self):
        while True:
            self.maze = [[self.CELL_WALL for _ in range(self.maze_width)] for _ in range(self.maze_height)]
            self.generate_maze_recursive(1, 1)
            self.assign_start_and_end()
            if self.is_maze_solvable_dfs():
                break

        self.draw_maze()
        self.root.mainloop()
    def assign_start_and_end(self):
        self.start_x, self.start_y = random.randint(1, self.maze_width - 2), random.randint(1, self.maze_height - 2)
        self.end_x, self.end_y = random.randint(1, self.maze_width - 2), random.randint(1, self.maze_height - 2)
        while self.maze[self.start_y][self.start_x] != CELL_PASSAGE or self.maze[self.end_y][self.end_x] != CELL_PASSAGE:
            self.start_x, self.start_y = random.randint(1, self.maze_width - 2), random.randint(1, self.maze_height - 2)
            self.end_x, self.end_y = random.randint(1, self.maze_width - 2), random.randint(1, self.maze_height - 2)
        self.maze[self.start_y][self.start_x] = 'start'
        self.maze[self.end_y][self.end_x] = 'end'


    def generate_maze_recursive(self, x, y):
        self.maze[y][x] = CELL_PASSAGE
        directions = [(0, -2), (0, 2), (-2, 0), (2, 0)]
        random.shuffle(directions)

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if 0 < nx < self.maze_width - 1 and 0 < ny < self.maze_height - 1 and self.maze[ny][nx] == CELL_WALL:
                mid_x, mid_y = x + dx // 2, y + dy // 2
                self.maze[mid_y][mid_x] = CELL_PASSAGE
                self.generate_maze_recursive(nx, ny)
    
    def is_maze_solvable_dfs(self):
        visited = set()
        queue = deque([(self.start_x, self.start_y)])

        while queue:
            current_x, current_y = queue.popleft()
            if (current_x, current_y) == (self.end_x, self.end_y):
                return True

            if (current_x, current_y) in visited:
                continue

            visited.add((current_x, current_y))

            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                next_x, next_y = current_x + dx, current_y + dy
                if 0 <= next_x < self.maze_width and 0 <= next_y < self.maze_height and self.maze[next_y][next_x] == self.CELL_PASSAGE:
                    queue.append((next_x, next_y))

        return False

    def draw_maze(self):
        self.canvas.delete('all')

        cell_size = WINDOW_SIZE // max(self.maze_width, self.maze_height)
        for y in range(self.maze_height):
            for x in range(self.maze_width):
                if self.maze[y][x] == CELL_WALL:
                    self.canvas.create_rectangle(x * cell_size, y * cell_size, (x + 1) * cell_size,
                                                 (y + 1) * cell_size, fill=CELL_DISPLAY_FILL)

        # Draw vertical and horizontal lines to separate cells
        for y in range(self.maze_height + 1):
            self.canvas.create_line(0, y * cell_size, self.maze_width * cell_size, y * cell_size, fill="black", width=1)

        for x in range(self.maze_width + 1):
            self.canvas.create_line(x * cell_size, 0, x * cell_size, self.maze_height * cell_size, fill="black", width=1)

        # Draw start and end points
        self.canvas.create_rectangle(self.start_x * cell_size, self.start_y * cell_size, (self.start_x + 1) * cell_size,
                                     (self.start_y + 1) * cell_size, fill=START_COLOR)
        self.canvas.create_rectangle(self.end_x * cell_size, self.end_y * cell_size, (self.end_x + 1) * cell_size,
                                     (self.end_y + 1) * cell_size, fill=END_COLOR)

        self.root.update()

