from component.cell import Cell
from component.distances import Distances
from component.grid import Grid, WALL_NULL


class DistanceGrid(Grid):

    def __init__(self, rows, columns):
        super(DistanceGrid, self).__init__(rows, columns)
        self.dist_record = None

    def contents_of(self, cell):
        if self.dist_record:
            content = self.dist_record.get(cell)
            return content or WALL_NULL
        return WALL_NULL

    def set_start(self, cell):
        self.dist_record = Distances(cell)
        self.dist_record.calculate_distances(cell)

    def path_to(self, goal: Cell):
        current = goal
        breadcrumbs = Distances(self.dist_record.root)
        breadcrumbs.cells[current] = self.dist_record.cells[current]

        while current != self.dist_record.root:
            for neighbor in current.links:
                if self.dist_record.cells[neighbor] < self.dist_record.cells[current]:
                    breadcrumbs.cells[neighbor] = self.dist_record.cells[neighbor]
                    current = neighbor
                    break
        return breadcrumbs
