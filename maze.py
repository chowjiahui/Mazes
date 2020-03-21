from algorithm_factory import AlgorithmFactory
from component.distance_grid import DistanceGrid
from component.distances import Distances
from component.grid import Grid


class Maze:

    def __init__(self, factory=AlgorithmFactory()):
        self.factory = factory
        self.grid = None
        self.start = None

    def setup(self, dimensions, start_coordinates, record_distance=True):
        row, col = dimensions
        self.grid = DistanceGrid(row, col) if record_distance else Grid(row, col)
        row_idx, col_idx = start_coordinates
        start_cell = self.grid.cell_record[row_idx][col_idx]
        self.grid.set_start(start_cell)
        self.start = start_cell

    def apply(self, algorithm_name):
        algorithm = self.factory.get(algorithm_name)
        self.grid = algorithm.on(self.grid)

    def plot_shortest_path(self, end_coordinates):
        row, col = end_coordinates
        end = self.grid.cell_record[row][col]

        new_distances = Distances(self.start)
        new_distances.calculate_distances(self.start)
        new_dist_record = new_distances.path_to(end)
        self.grid.dist_record = new_dist_record
        print(self.grid)

    def plot_longest_path(self):
        new_start_cell, distance = self.grid.dist_record.max_cell_and_distance()

        new_distances = Distances(new_start_cell)
        new_distances.calculate_distances(new_start_cell)
        longest_path_end, _ = new_distances.max_cell_and_distance()

        self.grid.dist_record = new_distances.path_to(longest_path_end)
        print(self.grid)