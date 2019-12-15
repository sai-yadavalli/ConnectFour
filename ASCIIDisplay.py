"""
    * VIEW
        - Overview of the View aspect, which consists of the ASCIIDisplay class.
"""


class ASCIIDisplay:
    def __init__(self, spacing=1):
        self.spacing = spacing

    def printState(self, b):
        """
        Print the ASCIIDisplay of the entire board.

        :param b:   Board object.
        :return:    None
        """

        print
        fullString = ""

        across = range(0, b.cols)
        up = range(b.rows-1, -1, -1)
        spaces = range(self.spacing)

        for i in up:
            top = "+"
            for j in across:
                for k in spaces:
                    top = top + "-"
                top = top + "-"
                for k in spaces:
                    top = top + "-"
                top = top + "+"
            top = top + "\n"
            fullString = fullString + top
            top = "+"
            for j in across:
                for k in spaces:
                    top = top + " "
                top = top + str(b.cells[j][i])
                for k in spaces:
                    top = top + " "
                if j == b.cols:
                    top = top + "+"
                else:
                    top = top + "|"
            top = top + "\n"
            fullString = fullString + top
        top = "+"

        for j in across:
            for k in spaces:
                top = top + "-"
            top = top + "-"
            for k in spaces:
                top = top + "-"
            top = top + "+"
        top = top + "\n"
        fullString = fullString + top
        # indices
        top = " "
        for j in across:
            for k in spaces:
                top = top + " "
            top = top + str(j + 1)
            for k in range(self.spacing - len(str(j + 1)) + 1):
                top = top + " "
            top = top + " "
        top = top + "\n"
        fullString = fullString + top
        print(fullString)

    @staticmethod
    def prompt_for_spacing():
        """
        Ask player to input valid boardspacing.

        :return: Valid integer value of board spacing.
        """

        num = input("Please choose the board spacing: ")
        return num

    @staticmethod
    def prompt_for_move(turn_count, player_count, player_color):
        """
        Prompt player to choose their move.

        :param turn_count:      Number of turns made.
        :param player_count:    Player number.
        :param player_color:    Player color.
        :return:                Integer value of selected column.
        """

        num = input("Turn {}: Player {} ({}), choose your move: ".format(turn_count, player_count, player_color))
        return num

    @staticmethod
    def invalid_move_out_of_bounds():
        """
        Display an error message for making an invalid move out of bounds.

        :return: None
        """

        print("Invalid move, outside board, try again: ")

    @staticmethod
    def col_full_error(loc):
        """
        Display an error message for selecting a column that is already entirely filled with pieces.

        :return: None
        """

        print("Invalid move, column {} is full, try again: ".format(loc))

    @staticmethod
    def invalid_spacing_error():
        """
        Display an error message for selecting invalid board spacing.

        :return: None
        """

        print("Invalid size, choose again: ")

    @staticmethod
    def invalid_yes_or_no_option():
        """
        Display an error message for selecting an invalid yes/no option when game results in a win or tie.

        :return: None
        """

        print("Invalid y/n option, choose again: ")
