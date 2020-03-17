import random

from component.grid import Grid


class AldousBroder:

    @staticmethod
    def on(grid: Grid):
        cell = grid.random_cell()
        assert cell
        unvisited = grid.size() - 1

        while unvisited:
            neighbour = random.choice(cell.neighbours())

            if not neighbour.links.keys():
                cell.link(neighbour)
                unvisited -= 1
            cell = neighbour

        return grid
