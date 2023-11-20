'''
To call the gui and take input from user 
'''
import tkinter as tk
from recursivebacktrack_maze import RecursiveBacktrackingMaze
from prim_maze import PrimMaze
from kruskal_maze_optimized import generateKruskalMaze,generateKruskalMazeWithStartAndEnd,display_maze_with_start_and_end
def main():
    root = tk.Tk()
    root.title('Maze Game Level Generator')
    root.configure(bg='#303030')  # Set background color

    width_label = tk.Label(root, text="Enter Width (5-40):", bg='#303030', fg='white')  # Set text and background color
    width_label.pack()
    width_entry = tk.Entry(root)
    width_entry.pack()

    height_label = tk.Label(root, text="Enter Height (5-40):", bg='#303030', fg='white')  # Set text and background color
    height_label.pack()
    height_entry = tk.Entry(root)
    height_entry.pack()

    def generate_kruskal_maze():
        try:
            width = int(width_entry.get())
            height = int(height_entry.get())
            if 5 <= width <= 40 and 5 <= height <= 40:
                maze, start, end = generateKruskalMazeWithStartAndEnd(width, height)
                display_maze_with_start_and_end(maze,start,end)
            else:
                print("Width and height should be between 5 and 40.")
        except ValueError:
            print("Please enter valid integer values for width and height.")

    def generate_recursive_backtracking_maze():
        try:
            width = int(width_entry.get())
            height = int(height_entry.get())
            if 5 <= width <= 40 and 5 <= height <= 40:
                recursive_backtracking_maze = RecursiveBacktrackingMaze(width, height)
            else:
                print("Width and height should be between 5 and 40.")
        except ValueError:
            print("Please enter valid integer values for width and height.")

    def generate_prim_maze():
        try:
            width = int(width_entry.get())
            height = int(height_entry.get())
            if 5 <= width <= 40 and 5 <= height <= 40:
                prim_maze = PrimMaze(width, height)
            else:
                print("Width and height should be between 5 and 40.")
        except ValueError:
            print("Please enter valid integer values for width and height.")


    kruskal_button = tk.Button(root, text="Generate Maze Using Kruskal's Algorithm", command=generate_kruskal_maze, bg='#90ee90')  # Set button color
    kruskal_button.pack()

    recursive_backtracking_button = tk.Button(root, text="Generate Maze using Recursive Backtracking", command=generate_recursive_backtracking_maze, bg='#add8e6')  # Set button color
    recursive_backtracking_button.pack()

    prim_button = tk.Button(root, text="Generate Maze Using Prim's Algorithm", command=generate_prim_maze, bg='#90ee90')  # Set button color
    prim_button.pack()

    root.mainloop()

if __name__ == '__main__':
    main()
