from Utils.Constants import ROWS, COLS, EMPTY, BLACK, WHITE, DIRS
import numpy as np

class Othello:
    """ This class represents the game Othello's Logic. """
    def __init__(self) -> None:
        pass

    def count_pieces(self, board: np.ndarray) -> tuple[int, int]:
        """
            This method counts the number of black and white pieces on the board. 
            Args:
                board (np.ndarray): The current board.
            Returns:
                tuple[int, int]: The number of black and white pieces on the board.
        """
        black_count = np.sum(board == BLACK)
        white_count = np.sum(board == WHITE)
        return black_count, white_count
    
    def valid_move(self, board: np.ndarray, row: int, col: int, player: int) -> bool:
        """
            This method checks if the move is valid or not.
            Args:
                board (np.ndarray): The current board.
                row (int): The row index.
                col (int): The column index.
                player (int): The player's piece.
            Returns:
                bool: True if the move is valid, False otherwise.
        """
        if board[row][col] != EMPTY:
            return False

        opponent = BLACK if player == WHITE else WHITE
        for dr, dc in DIRS:
            r, c = row + dr, col + dc
            pieces_to_flip = []
            while 0 <= r < ROWS and 0 <= c < COLS and board[r][c] == opponent:
                pieces_to_flip.append((r, c))
                r += dr
                c += dc
            
            if pieces_to_flip and 0 <= r < ROWS and 0 <= c < COLS and board[r][c] == player:
                return True
        return False
    
    def make_move(self, board: np.ndarray, row: int, col: int, player: int) -> None:
        """
            This method makes the move on the board.
            Args:
                board (np.ndarray): The current board.
                row (int): The row index.
                col (int): The column index.
                player (int): The player's piece.
        """
        opponent = BLACK if player == WHITE else WHITE
        board[row][col] = player

        for dr, dc in DIRS:
            r, c = row + dr, col + dc
            pieces_to_flip = []
            while 0 <= r < ROWS and 0 <= c < COLS and board[r][c] == opponent:
                pieces_to_flip.append((r, c))
                r += dr
                c += dc
            if pieces_to_flip and 0 <= r < ROWS and 0 <= c < COLS and board[r][c] == player:
                for r, c in pieces_to_flip:
                    board[r][c] = player
    
    def get_valid_moves(self, board: np.ndarray, player: int) -> list[tuple[int, int]]:
        """
            This method returns the list of valid moves for the player.
            Args:
                board (np.ndarray): The current board.
                player (int): The player's piece.
            Returns:
                list[tuple[int, int]]: The list of valid moves.
        """
        valid_moves = []
        for row in range(ROWS):
            for col in range(COLS):
                if self.valid_move(board, row, col, player):
                    valid_moves.append((row, col))
        return valid_moves
    
    def game_over(self, board: np.ndarray) -> bool:
        """
            This method checks if the game is over or not.
            Args:
                board (np.ndarray): The current board.
            Returns:
                bool: True if the game is over, False otherwise.
        """
        for r in range(ROWS):
            for c in range(COLS):
                if self.valid_move(board, r, c, BLACK) or self.valid_move(board, r, c, WHITE):
                    return False
        return True