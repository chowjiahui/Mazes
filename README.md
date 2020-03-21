## Mazes!

An implementation of maze generation algorithms in Python, based on Mazes for Programmers by Jamis Buck.
The maze output for now is a bunch of ASCII, but I hope to convert this to an SVG or image file in the future.

Set up steps:

```shell
cd path/to/project
virtualenv -p python3.6 mazes
source ./mazes/bin/activate
pip install -r requirements.txt

```

We first plot a maze of 7 rows and columns with the start point being the first 0-indexed row and column.
Distances are recorded so that the longest and shortest paths can eventually be calculated. 

Sample code below:

```python
algorithm = "Wilsons"
maze = Maze()
maze.setup(dimensions=[7, 7], start_coordinates=[0, 0], record_distance=True)
maze.apply(algorithm)
maze.plot_shortest_path(end_coordinates=[6, 0])

```

Running the code above should give a similar maze, with the shortest path plotted from the start point. 

```

+---+---+---+---+---+---+---+
| 0     |                   |
+   +   +   +---+---+---+---+
| 1 |   |       |           |
+   +---+---+   +   +---+   +
| 2   3   4   5 |   |       |
+---+---+---+   +   +   +---+
|   |         6 |   |   |   |
+   +   +---+   +   +---+   +
|       |   | 7         |   |
+   +---+   +   +   +   +   +
|   | A   9   8 |   |       |
+---+   +---+---+---+---+   +
| C   B                 |   |
+---+---+---+---+---+---+---+

```

