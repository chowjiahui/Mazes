from typing import List

import numpy as np

from component.cell import Cell

LINE_NULL = "   "
WALL_NULL = " "


class Grid:

    def __init__(self, rows, columns):
        self.row_dim = rows
        self.col_dim = columns
        self.cell_record = self.prepare_grid()
        self.configure_cell()

    def contents_of(self, cell):
        return WALL_NULL

    def __str__(self):
        output = "+" + "---+" * self.col_dim + "\n"
        for row in self.each_row():
            top = "|"
            bot = "+"
            for cell_or_null in row:
                cell = cell_or_null or Cell(-1, -1)
                body = f" {self.contents_of(cell)} "
                east_wall = WALL_NULL if cell.is_linked(cell.east) else "|"
                top += (body + east_wall)

                south_wall = LINE_NULL if cell.is_linked(cell.south) else "---"
                corner = "+"
                bot += (south_wall + corner)
            output += (top + "\n" + bot + "\n")
        return output

    def prepare_grid(self) -> List[List[Cell]]:
        return [[Cell(r, c) for c in range(self.col_dim)] for r in range(self.row_dim)]

    def random_cell(self) -> Cell:
        r = np.random.randint(self.row_dim)
        c = np.random.randint(self.col_dim)
        return self.cell_record[r][c] if self.cell_record else None

    def size(self):
        return self.row_dim * self.col_dim

    def each_row(self):
        for row in self.cell_record:
            yield row

    def each_cell(self):
        for row in self.cell_record:
            for cell in row:
                if cell:
                    yield cell

    def configure_cell(self):
        for cell in self.each_cell():
            r, c = cell.row, cell.column

            cell.north = self.cell_record[r - 1][c] if 0 < r else None
            cell.south = self.cell_record[r + 1][c] if r + 1 < self.row_dim else None
            cell.west = self.cell_record[r][c - 1] if 0 < c else None
            cell.east = self.cell_record[r][c + 1] if c + 1 < self.col_dim else None
