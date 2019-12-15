"""
    * CONTROLLER
        - Class definition for the ConnectFour class.
"""

from Board import Board
from Player import Player
from ASCIIDisplay import ASCIIDisplay
from Piece import Piece


class ConnectFour:
    def __init__(self, display=None):
        """
        Define the ConnectFour entity.

        :param display: ASCIIDisplay view of the board.
        """

        self.display = display

    @staticmethod
    def spacing(board_spacing):
        """
        Prompt for valid spacing of each cell in the board.

        :param board_spacing:   Spacing of each cell in the board.
        :return:                ASCIIDisplay of the board with valid, specified spacing.
        """

        while 1:
            if board_spacing < 0:
                board_spacing = ASCIIDisplay.invalid_spacing_error()
                board_spacing = ASCIIDisplay.prompt_for_spacing()
                continue
            if board_spacing > 2:
                board_spacing = ASCIIDisplay.invalid_spacing_error()
                board_spacing = ASCIIDisplay.prompt_for_spacing()
                continue
            elif 0 <= board_spacing <= 2:
                display = ASCIIDisplay(board_spacing)

                print("Type the column in which you wish to move.")

                break
            else:
                board_spacing = ASCIIDisplay.prompt_for_spacing()
                continue

        return display

    @staticmethod
    def reinitialize(board, board_spacing, red_player, black_player):
        """
        Reinitialize the board with the same spacing number.

        :param board:           Board being utilized throughout the game.
        :param board_spacing:   Spacing of each cell in the board.
        :param red_player:      Red player object.
        :param black_player:    Black player object.
        :return:                None.
        """

        board.makeAllSlotsOpen()
        display = ASCIIDisplay(board_spacing)
        ConnectFour.take_turns(board, board_spacing, display, red_player, black_player)

    @staticmethod
    def take_turns(board, board_spacing, display, red_player, black_player):
        """
        Prompt both players to take turns throughout the entire duration of the game.

        :param board:           Board being utilized throughout the game.
        :param board_spacing:   Spacing of each cell in the board.
        :param display:         ASCIIDisplay
        :param red_player:      Red player object
        :param black_player:    Black player object
        :return:                None
        """

        column = None
        turn_count = 1

        while 1:

            if turn_count % 2 == 1:
                display.printState(board)
                column = red_player.chooseMove(turn_count)

                while 1:
                    if column < 1 or column > 7:
                        column = ASCIIDisplay.invalid_move_out_of_bounds()
                        column = red_player.chooseMove(turn_count)
                    else:
                        red_piece = Piece(column, board, 1, 'R')
                        if board.makeMove(column, red_piece) is True:

                            if board.checkIfWinner(red_piece) is False and board.numSlotsRemaining() == 0:
                                display.printState(board)
                                option = raw_input("Tie Game!  Play again? (y/n): ")

                                while 1:
                                    if option == 'y':
                                        ConnectFour.reinitialize(board, board_spacing, red_player, black_player)
                                    elif option == 'n':
                                        print "Goodbye!"
                                        exit(-1)
                                    else:
                                        option = ASCIIDisplay.invalid_yes_or_no_option()
                                        option = raw_input("Tie Game!  Play again? (y/n): ")

                            elif board.checkIfWinner(red_piece):
                                display.printState(board)
                                option = raw_input("Player 1 Wins!  Play again? (y/n): ")

                                while 1:
                                    if option == 'y':
                                        ConnectFour.reinitialize(board, board_spacing, red_player, black_player)
                                    elif option == 'n':
                                        print "Goodbye!"
                                        exit(-1)
                                    else:
                                        option = ASCIIDisplay.invalid_yes_or_no_option()
                                        option = raw_input("Player 1 Wins!  Play again? (y/n): ")

                            break
                        else:
                            column = ASCIIDisplay.col_full_error(column)
                            column = black_player.chooseMove(turn_count)

                turn_count += 1

            if turn_count % 2 == 0:
                display.printState(board)
                column = black_player.chooseMove(turn_count)

                while 1:
                    if column < 1 or column > 7:
                        column = ASCIIDisplay.invalid_move_out_of_bounds()
                        column = black_player.chooseMove(turn_count)
                    else:
                        black_piece = Piece(column, board, 2, 'B')
                        if board.makeMove(column, black_piece) is True:

                            if board.checkIfWinner(black_piece) is False and board.numSlotsRemaining() == 0:
                                display.printState(board)
                                option = raw_input("Tie Game!  Play again? (y/n): ")

                                while 1:
                                    if option == 'y':
                                        ConnectFour.reinitialize(board, board_spacing, red_player, black_player)
                                    elif option == 'n':
                                        print "Goodbye!"
                                        exit(-1)
                                    else:
                                        option = ASCIIDisplay.invalid_yes_or_no_option()
                                        option = raw_input("Tie Game!  Play again? (y/n): ")

                            elif board.checkIfWinner(black_piece):
                                display.printState(board)
                                option = raw_input("Player 2 Wins!  Play again? (y/n): ")

                                while 1:
                                    if option == 'y':
                                        ConnectFour.reinitialize(board, board_spacing, red_player, black_player)
                                    elif option == 'n':
                                        print "Goodbye!"
                                        exit(-1)
                                    else:
                                        option = ASCIIDisplay.invalid_yes_or_no_option()
                                        option = raw_input("Player 2 Wins!  Play again? (y/n): ")
                            break
                        else:
                            column = ASCIIDisplay.col_full_error(column)
                            column = black_player.chooseMove(turn_count)

                turn_count += 1

    def play_game(self):
        """
        Initialize a new board, red and black players, choose spacing, display the board, and play the game.

        :return: None
        """

        board = Board(7, 6)

        red_player = Player(1, 'R')
        black_player = Player(2, 'B')

        board_spacing = ASCIIDisplay.prompt_for_spacing()

        display = self.spacing(board_spacing)

        self.take_turns(board, board_spacing, display, red_player, black_player)
