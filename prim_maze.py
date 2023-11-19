'''
Prim's Algorithm for finding the minimum spanning tree (MST) within a connected and undirected graph. Built upon the greedy approach, this algorithm systematically constructs the MST by continuously selecting the lowest-weight edge connecting the existing tree to an unvisited vertex. The algorithm initializes with an arbitrary starting point, expanding iteratively until all vertices are encompassed, ensuring the formation of an acyclic tree with the least cumulative edge weight.
'''
import tkinter as tk
import random

WINDOW_SIZE = 800
CELL_DISPLAY_FILL = 'black'
CELL_SIZE = 20

class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class PrimMaze:
    
    def __init__(self, width, height):
        self.maze_width = width
        self.maze_height = height
        self.maze = [[1 for _ in range(width)] for _ in range(height)]
        self.generate_maze_prim()
        self.set_start_and_end()
        self.draw_maze()

    def generate_maze_prim(self):
        # Initialize maze with walls
        for y in range(self.maze_height):
            for x in range(self.maze_width):
                self.maze[y][x] = 1

        start_x = random.randint(0, self.maze_width - 1)
        start_y = random.randint(0, self.maze_height - 1)
        self.maze[start_y][start_x] = 0

        walls = []
        walls.extend(self.get_neighbours(start_x, start_y))

        while walls:
            wall = random.choice(walls)
            x, y = wall
            neighbours = self.get_neighbours(x, y)
            pass_count = 0

            for neighbour in neighbours:
                nx, ny = neighbour
                if self.maze[ny][nx] == 0:
                    pass_count += 1

            if pass_count == 1:
                self.maze[y][x] = 0
                walls.extend(neighbours)

            walls.remove(wall)

    def get_neighbours(self, x, y):
        neighbours = []
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < self.maze_width and 0 <= ny < self.maze_height:
                neighbours.append((nx, ny))

        random.shuffle(neighbours)
        return neighbours

    def set_start_and_end(self):
        start_x, start_y = self.find_random_passable_cell()
        self.maze[start_y][start_x] = 'start'

        end_x, end_y = self.find_random_passable_cell()
        while (end_x, end_y) == (start_x, start_y):
            end_x, end_y = self.find_random_passable_cell()
        self.maze[end_y][end_x] = 'end'

    def find_random_passable_cell(self):
        x, y = random.randint(0, self.maze_width - 1), random.randint(0, self.maze_height - 1)
        while self.maze[y][x] == 1:
            x, y = random.randint(0, self.maze_width - 1), random.randint(0, self.maze_height - 1)
        return x, y

    def draw_maze(self):
        root = tk.Tk()
        root.title('Maze Generated with Prim\'s Algorithm')
        canvas = tk.Canvas(root, width=WINDOW_SIZE, height=WINDOW_SIZE, bg='black')  # Set canvas background to black
        canvas.pack()

        for y in range(self.maze_height):
            for x in range(self.maze_width):
                if self.maze[y][x] == 0:
                    cell_x = x * CELL_SIZE
                    cell_y = y * CELL_SIZE
                    canvas.create_rectangle(cell_x, cell_y, cell_x + CELL_SIZE, cell_y + CELL_SIZE, fill='white')
                    canvas.create_line(cell_x, cell_y + CELL_SIZE, cell_x + CELL_SIZE, cell_y + CELL_SIZE, fill=CELL_DISPLAY_FILL)
                    canvas.create_line(cell_x + CELL_SIZE, cell_y, cell_x + CELL_SIZE, cell_y + CELL_SIZE, fill=CELL_DISPLAY_FILL)
                elif self.maze[y][x] == 'start':
                    cell_x = x * CELL_SIZE
                    cell_y = y * CELL_SIZE
                    canvas.create_rectangle(cell_x, cell_y, cell_x + CELL_SIZE, cell_y + CELL_SIZE, fill='red')
                elif self.maze[y][x] == 'end':
                    cell_x = x * CELL_SIZE
                    cell_y = y * CELL_SIZE
                    canvas.create_rectangle(cell_x, cell_y, cell_x + CELL_SIZE, cell_y + CELL_SIZE, fill='green')

        root.mainloop()


