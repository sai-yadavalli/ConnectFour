"""
    * MODEL
        - Definition of the Cell class.
"""


class Cell:
    def __init__(self, col=7, row=6, piece=None):
        self.row = row
        self.col = col
        self.piece = piece
        self.occupied = False

    def is_occupied(self):
        """
        Check if a cell is occupied.

        :return: Boolean value of self.occupied.
        """

        return self.occupied

    def update(self, p):
        """
        Mark the cell as occupied and add piece into it.

        :param p:   Piece object.
        :return:    True
        """

        self.occupied = True
        self.piece = p
        return True

    def makeSlotOpen(self):
        """
        Make cell slot empty.

        :return: None
        """

        self.occupied = False

    def __str__(self):
        """
        Check if cell is occupied and return the string display of the piece marker.

        :return: String display of piece marker if cell is occupied, ' ' if cell is empty.
        """

        if self.occupied:
            return str(self.piece)
        return ' '
