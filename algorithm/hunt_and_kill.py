from random import random

from component.grid import Grid


class HuntAndKill:

    @staticmethod
    def on(grid: Grid):
        current = grid.random_cell()

        while current:
            unvisited_cells = [cell for cell in current.neighbours if not cell.links]
            if unvisited_cells:
                neighbor = random.choice(unvisited_cells)
                current.link(neighbor)
                current = neighbor
            else:
                current = None

                for cell in grid.each_cell():
                    visited_cells = [cell for cell in current.neighbours if cell.links]
                    if not cell.links and visited_cells:
                        current = cell

                        neighbor = random.choice(visited_cells)
                        current.link(neighbor)

        return grid
