import timeit
import numpy as np
import matplotlib.pyplot as plt
from kruskal_maze_optimized import generateKruskalMaze
from prim_maze import PrimMaze
from recursivebacktrack_maze import RecursiveBacktrackingMaze
import time
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

def kruskal_maze(n):
    generateKruskalMaze(n,n)
    pass

def prim_maze(n):
    PrimMaze(n,n)
    pass

def recursive_backtracking_maze(n):
    RecursiveBacktrackingMaze(n,n)
    pass

# Function to measure execution time of maze generation algorithms
def measure_execution_time(algorithm, size):
    start_time = time.time()
    algorithm(size)
    end_time = time.time()
    return end_time - start_time
maze_sizes = []
for i in range(3,40):
    maze_sizes.append(i)
algorithms = [kruskal_maze, prim_maze, recursive_backtracking_maze]
execution_times = np.zeros((len(algorithms), len(maze_sizes)))

for i, algorithm in enumerate(algorithms):
    for j, size in enumerate(maze_sizes):
        execution_times[i][j] = measure_execution_time(algorithm, size)

# Scatter plot comparing execution times for different algorithms and maze sizes
plt.figure(figsize=(10, 6))
for i, algorithm in enumerate(algorithms):
    plt.scatter(maze_sizes, execution_times[i], label=algorithm.__name__)
plt.xlabel('Maze Size')
plt.ylabel('Execution Time (seconds)')
plt.title('Comparison of Maze Generation Algorithms')
plt.legend()
plt.grid(True)
plt.show()

# Heatmap comparing execution times for different algorithms and maze sizes
plt.figure(figsize=(8, 6))
plt.imshow(execution_times, cmap='viridis', interpolation='nearest')
plt.colorbar(label='Execution Time (seconds)')
plt.xticks(np.arange(len(maze_sizes)), maze_sizes)
plt.yticks(np.arange(len(algorithms)), [algo.__name__ for algo in algorithms])
plt.xlabel('Maze Size')
plt.ylabel('Algorithm')
plt.title('Heatmap of Execution Times')
plt.show()

avg_execution_times = np.mean(execution_times, axis=1)

# Bar chart for comparative analysis of average execution times
plt.figure(figsize=(8, 6))
plt.bar([algo.__name__ for algo in algorithms], avg_execution_times)
plt.xlabel('Algorithm')
plt.ylabel('Average Execution Time (seconds)')
plt.title('Average Execution Time of Maze Generation Algorithms')
plt.grid(axis='y')
plt.show()

# Line plots for comparative analysis of execution times for each algorithm across different maze sizes
plt.figure(figsize=(10, 6))
for i, algorithm in enumerate(algorithms):
    plt.plot(maze_sizes, execution_times[i], label=algorithm.__name__, marker='o')
plt.xlabel('Maze Size')
plt.ylabel('Execution Time (seconds)')
plt.title('Execution Times of Maze Generation Algorithms Across Different Sizes')
plt.legend()
plt.grid(True)
plt.show()


colors = ['blue', 'orange', 'green']

# Boxplot for comparative analysis of execution times distribution
plt.figure(figsize=(8, 6))
boxplot_parts = plt.boxplot(execution_times.T, labels=[algo.__name__ for algo in algorithms], patch_artist=True)

# Set colors for each part of the boxplot
for i, box in enumerate(boxplot_parts['boxes']):
    box.set(facecolor=colors[i])

for whisker, cap, median in zip(boxplot_parts['whiskers'], boxplot_parts['caps'], boxplot_parts['medians']):
    whisker.set(color='black', linewidth=1.2)
    cap.set(color='black', linewidth=1.2)
    median.set(color='red', linewidth=1.5)

plt.xlabel('Algorithm')
plt.ylabel('Execution Time (seconds)')
plt.title('Distribution of Execution Times for Maze Generation Algorithms')
plt.grid(axis='y')
plt.show()