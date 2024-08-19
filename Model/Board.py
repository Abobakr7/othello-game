import numpy as np
from Utils.Constants import ROWS, COLS, BLACK, WHITE

class Board:
    """ This class represents the board of the game and can be used for multiple games. """
    def __init__(self, game: str) -> None:
        """
            This method initializes the board.
            Args:
                game (str): The game name.
        """
        if game == "Othello":
            self.othello_board_init()

    def othello_board_init(self) -> None:
        """
            This method initializes the board with the starting pieces for Othello game.
        """
        self.board = np.zeros((ROWS, COLS), dtype=int)
        self.board[3][3], self.board[3][4] = WHITE, BLACK
        self.board[4][3], self.board[4][4] = BLACK, WHITE
    
    def reset_othello_board(self) -> None:
        """ This method resets the Othello board. """
        self.othello_board_init()