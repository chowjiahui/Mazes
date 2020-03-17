import random

from component.grid import Grid


class Wilsons:

    @staticmethod
    def on(grid: Grid):
        unvisited = [cell for cell in grid.each_cell()]

        first = random.choice(unvisited)
        unvisited.remove(first)

        while len(unvisited) > 0:
            cell = random.choice(unvisited)
            path = [cell]

            while cell in unvisited:
                cell = random.choice(cell.neighbours())
                if cell in path:
                    position = path.index(cell)
                    path = path[0:position + 1]
                else:
                    path.append(cell)

            path, unvisited = Wilsons.remove_walls_in_path(path, unvisited)
            # for index in range(0, len(path)-1):
            #     path[index].link(path[index + 1])
            #     unvisited.remove(path[index])
            #print(unvisited)

        return grid

    @staticmethod
    def remove_walls_in_path(path, unvisited):
        for index in range(0, len(path) - 1):
            path[index].link(path[index + 1])
            unvisited.remove(path[index])
        return path, unvisited
