from algorithm.aldous_broder import AldousBroder
from algorithm.wilsons import Wilsons
from component.distance_grid import DistanceGrid
from algorithm.sidewinder import Sidewinder
from component.distances import Distances
from component.grid import Grid

if __name__ == '__main__':
    grid = DistanceGrid(7, 7)
    Wilsons.on(grid)
    print(grid)
    grid.set_start(grid.record[0][0])

    # Shortest path
    # grid.dist_record = grid.dist_record.path_to(grid.record[grid.row_dim - 1][0])
    # print(grid)

    # Longest path
    start = grid.record[0][0]
    distances = grid.dist_record
    new_start_cell, distance = distances._max()

    new_distances = Distances(new_start_cell)
    new_distances.calculate_distances(new_start_cell)
    goal, distance = new_distances._max()

    grid.dist_record = new_distances.path_to(goal)
    print(grid)
