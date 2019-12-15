"""
    * CONTROLLER
        - Class definition for the KeyboardConsoleInput class.
"""


class KeyboardConsoleInput:

    def __init__(self):
        """ No constructor defined for this class. """
        pass

    @staticmethod
    def read_move(turn_count, player_count, player_color):
        """
        Read in a column through user input while displaying turn #, player #, and player color.

        :param turn_count:      Counter that keeps track of the # of turns being made throughout the game.
        :param player_count:    Player #.
        :param player_color:    Player color
        :return:                Column (int) that the user reads in.
        """

        column = input("Turn {}: Player {} ({}), choose your move: ".format(turn_count, player_count, player_color))
        return column

