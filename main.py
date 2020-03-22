from maze import Maze

if __name__ == '__main__':
    algorithm = "Wilsons"

    maze = Maze()
    maze.setup(dimensions=(7, 7), start_coordinates=(0, 0), record_distance=True)
    maze.apply(algorithm)
    maze.plot_shortest_path(end_coordinates=(6, 0))
