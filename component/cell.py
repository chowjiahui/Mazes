class Cell:

    def __init__(self, row, column):
        self.row = row
        self.column = column
        self.links = dict()
        self.north, self.south, self.west, self.east = None, None, None, None

    def link(self, cell, bidi=True):
        self.links[cell] = True
        if bidi:
            cell.link(self, False)

    def unlink(self, cell, bidi=True):
        self.links.pop(cell)
        if bidi:
            cell.unlink(self, False)

    def links(self):
        return self.links.keys()

    def is_linked(self, cell):
        return cell in self.links

    def neighbours(self):
        _all = [self.north, self.south, self.west, self.east]
        return [x for x in _all if x]
