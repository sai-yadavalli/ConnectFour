"""
    * MODEL
        - Class definition for the Piece class.
"""


class Piece:
    def __init__(self, col=-1, board=None, number=-1, display='&'):
        """
        Define a Piece entity.

        :param col:     Column that piece is in.
        :param board:   Board object.
        :param number:  Piece number
        :param display: Piece marker
        """

        self.col = col
        self.display = display
        self.board = board
        self.number = number

    def __str__(self):
        """
        Store a string representation of the piece marker.
        :return: String display of piece marker.
        """

        return self.display
