'''

The "DisjointSet" class is responsible for implementing the disjoint set data structure. It employs a collection of trees, where each tree represents a set of interconnected cells. Within these trees, every node represents an individual cell and maintains a pointer to its parent node. The root node of each tree signifies the entire set and is identified by having a parent pointer that points to itself.

The disjoint set data structure primarily operates through two key methods: "find" and "union." The "find" operation locates and returns the root node of the tree containing a given node. Meanwhile, the "union" operation merges two trees into a single tree by reassigning the root node of one tree to point towards the root node of the other tree, effectively combining their structures.
'''
import random


class DisjointSet:

    def __init__(self, width, height):
        self.set_count = width * height
        self.parent_list = [i for i in range(self.set_count)]
        self.size_list = [1 for i in range(self.set_count)]
        self.width = width
        self.height = height
        self.color_list = [self.generate_random_hex_color()
                           for i in range(self.set_count)]

    def find(self, cell):
        '''
        Description: This function returns the root node of the tree that contains the given node.
        Parameters: cell - The cell.
        Return: The root node of the tree that contains the given node.
        '''
        # Find the root of the tree.
        root_index = (cell.y // 2) * self.width + (cell.x // 2)
        while root_index != self.parent_list[root_index]:
            root_index = self.parent_list[root_index]

        # Compress the path leading back to the root.
        current_node = (cell.y // 2) * self.width + (cell.x // 2)
        while current_node != root_index:
            parent_node = self.parent_list[current_node]
            self.parent_list[current_node] = root_index
            current_node = parent_node

        return root_index

    def union(self, cell1, cell2):
        '''
        Description: This function merges two trees into one tree by making the root node of one tree point to the root node of the other tree.
        Parameters: cell1 - The first cell.
                    cell2 - The second cell.
        '''
        # Find the roots and stop if they are already the same.
        root1 = self.find(cell1)
        root2 = self.find(cell2)
        if root1 == root2:
            return

        # Merge the smaller tree into the larger tree.
        if self.size_list[root1] < self.size_list[root2]:
            self.parent_list[root1] = root2
            self.size_list[root2] += self.size_list[root1]
        else:
            self.parent_list[root2] = root1
            self.size_list[root1] += self.size_list[root2]
        self.set_count -= 1

    def generate_random_hex_color(self):
        '''
        Description: This function generates a random hexadecimal color.
        Return: A random hexadecimal color.
        '''
        return '#' + ''.join([random.choice('0123456789ABCDEF') for j in range(6)])
