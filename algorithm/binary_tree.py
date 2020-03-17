import random


class BinaryTree:

    @staticmethod
    def on(grid):
        for cell in grid.each_cell():
            neighbours = []
            if cell.north:
                neighbours.append(cell.north)
            if cell.east:
                neighbours.append(cell.east)

            if neighbours:
                neighbour = random.choice(neighbours)
                cell.link(neighbour)
