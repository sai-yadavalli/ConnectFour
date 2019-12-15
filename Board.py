"""
    * MODEL
        - Class definition for the Board class.
"""

from Cell import Cell


class Board:

    def __init__(self, col=7, row=6):
        """
        Define a Board entity.

        :param col: Number of columns.
        :param row: Number of rows.
        """

        self.rows = row
        self.cols = col
        self.cells = []
        self.num_slots_remaining = row*col

        for cell_col in range(0, self.cols):
            new_row = []
            for cell_row in range(0, self.rows):
                new_row.append(Cell(cell_row, cell_row))
            self.cells.append(new_row)

    def numSlotsRemaining(self):
        """
        Keep track of the number of empty slots remaining in the board.

        :return: # of empty slots left in the board.
        """

        return self.num_slots_remaining

    def decrementNumSlotsOpen(self):
        """
        Decrement the number of empty slots remaining in the board.

        :return: None
        """

        self.num_slots_remaining -= 1

    def makeAllSlotsOpen(self):
        """
        Make each slot in the board empty at once.

        :return: None
        """

        self.num_slots_remaining = self.rows * self.cols

        for i in range(0, self.rows):
            for j in range(0, self.cols):
                self.cells[j][i].makeSlotOpen()

    def makeMove(self, col, piece):
        """
        Place the piece into the lowest unoccupied position in the specified column.

        :param col:     column that the player wishes to place the piece in.
        :param piece:   piece that player places in the column.
        :return:        True if move is successful, False if column is entirely filled with pieces.
        """

        for i in range(0, self.rows):
            if self.cells[col-1][i].is_occupied():
                continue
            else:
                self.cells[col-1][i].update(piece)
                self.decrementNumSlotsOpen()
                return True

        return False

    def checkIfWinner(self, piece):
        """
        Examine the entire board for all winning possibilities containing the piece passed in.
        :param piece:   piece being used for checking all winning conditions.
        :return:        True if any winning condition is detected, False if none were detected (i.e a Tie game).
        """

        # Horizontal check
        for i in range(0, self.rows):
            for j in range(0, self.cols-3):
                if self.cells[j][i].__str__() != ' ':
                    if self.cells[j][i].__str__().__eq__(piece.display):
                        if (self.cells[j][i].__str__() == self.cells[j+1][i].__str__() and
                            self.cells[j+1][i].__str__() == self.cells[j+2][i].__str__() and
                                self.cells[j+2][i].__str__() == self.cells[j+3][i].__str__()):
                            return True

        # Vertical check
        for i in range(0, self.rows-3):
            for j in range(0, self.cols):
                if self.cells[j][i].__str__() != ' ':
                    if self.cells[j][i].__str__().__eq__(piece.display):
                        if (self.cells[j][i].__str__() == self.cells[j][i+1].__str__() and
                            self.cells[j][i+1].__str__() == self.cells[j][i+2].__str__() and
                                self.cells[j][i+2].__str__() == self.cells[j][i+3].__str__()):
                            return True

        # Upper diagonal check
        for i in range(0, self.rows-3):
            for j in range(0, self.cols-3):
                if self.cells[j][i].__str__() != ' ':
                    if self.cells[j][i].__str__().__eq__(piece.display):
                        if (self.cells[j][i].__str__() == self.cells[j+1][i+1].__str__() and
                            self.cells[j+1][i+1].__str__() == self.cells[j+2][i+2].__str__() and
                                self.cells[j+2][i+2].__str__() == self.cells[j+3][i+3].__str__()):
                            return True

        # Lower diagonal check
        for i in range(self.rows-1, 2, -1):
            for j in range(0, self.cols-3):
                if self.cells[j][i].__str__() != ' ':
                    if self.cells[j][i].__str__().__eq__(piece.display):
                        if (self.cells[j][i].__str__() == self.cells[j+1][i-1].__str__() and
                            self.cells[j+1][i-1].__str__() == self.cells[j+2][i-2].__str__() and
                                self.cells[j+2][i-2].__str__() == self.cells[j+3][i-3].__str__()):
                            return True

        return False
