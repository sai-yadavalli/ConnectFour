"""
    * MODEL
        - Class definition for the Player class.
"""

from KeyboardConsoleInput import KeyboardConsoleInput


class Player:
    def __init__(self, number=-1, piece_color='?'):
        """
        Define a player object.

        :param number:      takes in a number.
        :param piece_color: takes in a color.
        """

        self.number = number
        self.piece_color = piece_color

    def chooseMove(self, turn_count):
        """
        Read in a column and prompts the player to choose a move through user input.

        :param turn_count:  Counter that keeps track of the # of turns being made throughout the game.
        :return:            The column (int) that the user reads in.
        """

        column = KeyboardConsoleInput.read_move(turn_count, self.number, self.piece_color)
        return column
