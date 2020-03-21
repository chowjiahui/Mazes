from component.cell import Cell
from numpy import base_repr


class Distances:

    def __init__(self, root: Cell):
        self.root = root
        self.base = 36
        self.cells = dict()
        self.cells[root] = "0"
        # self.calculate_distances(root)

    def get(self, cell):
        return self.cells[cell] if cell in self.cells else None

    def set(self, cell, distance):
        try:
            self.cells[cell] = base_repr(distance, self.base)
        except TypeError:
            print("Distance to record must be a an integer!")

    def cells(self):
        return self.cells.keys()

    def calculate_distances(self, start: Cell):
        frontier = [start]
        self.set(start, 0)
        while frontier:
            new_frontier = []
            for cell in frontier:
                for link in cell.links.keys():
                    visited_dist = self.get(link)
                    if visited_dist is not None:
                        continue
                    else:
                        self.set(link, self.to_base_ten(self.get(cell)) + 1)
                        new_frontier.append(link)
            frontier = new_frontier
        print("Distance calculation completed!")

    @staticmethod
    def to_base_ten(string):
        return int(string) if string.isdigit() else ord(string) - 55

    def path_to(self, goal: Cell):
        current = goal
        breadcrumbs = Distances(self.root)
        breadcrumbs.cells[current] = self.cells[current]

        while current != self.root:
            for neighbor in current.links:
                if self.cells[neighbor] < self.cells[current]:
                    breadcrumbs.cells[neighbor] = self.cells[neighbor]
                    current = neighbor
                    break
        return breadcrumbs

    def max_cell_and_distance(self):
        max_distance = 0
        max_cell = self.root

        for cell, distance in self.cells.items():
            base_ten_dist = self.to_base_ten(distance)
            if base_ten_dist > max_distance:
                max_cell = cell
                max_distance = base_ten_dist
        return max_cell, max_distance
