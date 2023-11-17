'''
Maze Generation with Kruskal's Algorithm
Author: HUI, Macarious Kin Fung

This program generates a maze using Kruskal's algorithm. The maze is represented
as a 2D array of cells. Each cell is either a wall or a passage. The maze is
generated by removing walls between cells. The algorithm starts with a grid of
passages and walls. It then removes walls between cells until all cells are
connected. The algorithm removes walls by selecting a random wall and checking
if the cells on either side of the wall are connected. If the cells are not
connected, the wall is removed and the cells are connected. If the cells are
already connected, the wall is left in place. The algorithm continues until all
cells are connected.

The program uses a disjoint set data structure to keep track of which cells are
connected. The disjoint set data structure is implemented using a forest of
trees. Each tree represents a set of connected cells. Each node in the tree
represents a cell. Each node has a parent pointer that points to the parent
node. The root node of each tree represents the set. The root node has a parent
pointer that points to itself. The disjoint set data structure has two
operations: find and union. The find operation returns the root node of the tree
that contains the given node. The union operation merges two trees into one tree
by making the root node of one tree point to the root node of the other tree.
'''

import sys
import tkinter as tk

from kruskal_maze import KruskalMaze


def main():
    user_width = int(input('Width: '))
    user_height = int(input('Height: '))
    if user_width < 3 or user_height < 3 or user_width % 2 == 0 or user_height % 2 == 0:
        print('Error: Invalid maze dimensions. Dimensions must be greater than or equal to 3 and odd.')
        sys.exit()

    # The initial number of passage cells in the x direction.
    width = (user_width + 1) // 2
    # The initial number of passage cells in the y direction.
    height = (user_height + 1) // 2
    KruskalMaze(width, height)


if __name__ == '__main__':
    main()
