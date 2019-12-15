"""
    * CONTROLLER
        - Run the Controller module from which flow control goes to the Model and then to the View.
"""

from GameController import ConnectFour


def main():
    """
    Run the play_game() controller function to start a game of ConnectFour.

    :return: None
    """

    game = ConnectFour()
    game.play_game()


main()
