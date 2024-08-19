import copy
import numpy as np
from Controller.Othello import Othello
from Utils.Constants import ROWS, COLS, BLACK, WHITE, DIRS

class AI(Othello):
    """ This class represents the AI for the game using minimax with alpha-beta pruning algorithm. """
    def __init__(self) -> None:
        pass

    def evaluate_game_state(self, board: np.ndarray) -> int:
        """
            This method evaluates the game state.
            Args:
                board (np.ndarray): The current board.
            Returns:
                int: The score of players for the current game.
        """
        black_count, white_count = self.count_pieces(board)
        if white_count > black_count:
            return 1
        elif white_count < black_count:
            return -1
        return 0

    def update_board(self, board: np.ndarray, row: int, col: int, player: int) -> np.ndarray:
        """
            This method updates the board with the move.
            Args:
                board (np.ndarray): The current board.
                row (int): The row index.
                col (int): The column index.
                player (int): The player's piece.
            Returns:
                np.ndarray: The updated board.
        """
        opponent = 2 if player == 1 else 1
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
        return board

    def minimax(self, board: np.ndarray, depth: int, alpha: int, beta: int, player: int) -> tuple[int, tuple[int, int]]:
        """ 
            This method implements the minimax algorithm with alpha-beta pruning.
            Args:
                board (np.ndarray): The current board.
                depth (int): The depth of the tree.
                alpha (int): The alpha value.
                beta (int): The beta value.
                player (int): The player's piece.
            Returns:
                tuple[int, tuple[int, int]]: The score of the player and the best move.
        """
        possible_moves = self.get_valid_moves(board, player)
        if depth == 0 or not possible_moves:
            return self.evaluate_game_state(board), ()
        
        if player == WHITE: # maximizing player
            max_eval = float("-inf")
            best_move = ()
            for r, c in possible_moves:
                new_board = self.update_board(copy.deepcopy(board), r, c, player)
                eval, _ = self.minimax(new_board, depth - 1, alpha, beta, BLACK if player == WHITE else WHITE)
                if max_eval < eval:
                    max_eval = eval
                    best_move = (r, c)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
            return max_eval, best_move
        else:           # minimizing player
            min_eval = float("inf")
            best_move = ()
            for r, c in possible_moves:
                new_board = self.update_board(copy.deepcopy(board), r, c, player)
                eval, _ = self.minimax(new_board, depth - 1, alpha, beta, BLACK if player == WHITE else WHITE)
                if min_eval > eval:
                    min_eval = eval
                    best_move = (r, c)
                beta = min(beta, eval)
                if beta <= alpha:
                    break
            return min_eval, best_move