import random

from component.grid import Grid


class Sidewinder:

    @staticmethod
    def on(grid: Grid):
        for row in grid.each_row():
            run = []  # a cluster of cells
            for cell in row:
                run.append(cell)

                at_eastern_boundary = cell.east is None
                at_northern_boundary = cell.north is None
                heads = random.randint(1, 2) == 1

                should_close_run = at_eastern_boundary or (not at_northern_boundary and heads)
                if should_close_run:
                    member = random.choice(run)
                    if member.north:
                        member.link(member.north)
                    run = []
                else:
                    cell.link(cell.east)
