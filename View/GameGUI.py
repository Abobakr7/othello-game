import tkinter as tk
from tkinter import messagebox
from Model.Board import Board
from Controller.Othello import Othello
from Controller.AI import AI
from Utils.Constants import *

class GameGUI:
    """ This class represents the GUI of the game. """
    def __init__(self, root: tk.Tk) -> None:
        """
            This method initializes the GUI.
            Args:
                root (tk.Tk): The root window.
        """
        self.root = root
        self.root.title("Othello")
        self.root.geometry("480x600")
        self.root.resizable(False, False)
        self.board = Board("Othello")
        self.othello = Othello()
        self.current_player = BLACK
        self.last_move = None
        self.draw_widgets()
        self.entry_frame.tkraise()

    def draw_widgets(self) -> None:
        """ This method draws the widgets on the window. """
        self.entry_frame_init()
        self.game_play_frame_init()
    
    def entry_frame_init(self) -> None:
        """ This method initializes the entry frame. """
        self.entry_frame = tk.Frame(self.root, bg="#1b4332")
        self.entry_frame.grid(row=0, column=0, sticky="nsew")

        welcome_lbl = tk.Label(self.entry_frame,
                                text="Welcome to Othello",
                                font=("Helvetica", 24, "bold"),
                                bg="#1b4332",
                                fg="#d8f3dc")
        welcome_lbl.place(x=92, y=20)

        play_vs_computer_lbl = tk.Label(self.entry_frame,
                                text="Play Vs Computer",
                                font=("Helvetica", 14, "bold"),
                                bg="#1b4332",
                                fg="#d8f3dc")
        play_vs_computer_lbl.place(x=152, y=240)

        human_mode_btn = tk.Button(self.entry_frame,
                                relief="groove",
                                text="1 vs 1",
                                width=15,
                                font=("Helvetica", 16, "bold"),
                                bg="#52b788",
                                fg="#fff",
                                activebackground="#40916c",
                                activeforeground="#e0e0e0",
                                command=lambda: self.switch_frames(self.game_frame, HUMAN))
        human_mode_btn.place(x=135, y=150)

        easy_lvl_btn = tk.Button(self.entry_frame,
                                relief="groove",
                                text="Easy",
                                width=15,
                                font=("Helvetica", 16, "bold"),
                                bg="#52b788",
                                fg="#fff",
                                activebackground="#40916c",
                                activeforeground="#e0e0e0",
                                command=lambda: self.switch_frames(self.game_frame, EASY))
        easy_lvl_btn.place(x=135, y=290)

        medium_lvl_btn = tk.Button(self.entry_frame,
                                relief="groove",
                                text="Medium",
                                width=15,
                                font=("Helvetica", 16, "bold"),
                                bg="#52b788",
                                fg="#fff",
                                activebackground="#40916c",
                                activeforeground="#e0e0e0",
                                command=lambda: self.switch_frames(self.game_frame, MEDIUM))
        medium_lvl_btn.place(x=135, y=350)

        hard_lvl_btn = tk.Button(self.entry_frame,
                                relief="groove",
                                text="Hard",
                                width=15,
                                font=("Helvetica", 16, "bold"),
                                bg="#52b788",
                                fg="#fff",
                                activebackground="#40916c",
                                activeforeground="#e0e0e0",
                                command=lambda: self.switch_frames(self.game_frame, HARD))
        hard_lvl_btn.place(x=135, y=410)

    def game_play_frame_init(self):
        """ This method initializes the game play frame. """
        self.game_frame = tk.Frame(self.root, bg="#1b4332")
        self.game_frame.grid(row=0, column=0, sticky="nsew")

        top_frame = tk.Frame(self.game_frame, height="120", bg="#1b4332")
        top_frame.pack(side="top", fill="x")
        back_btn = tk.Button(top_frame,
                            relief="groove",
                             text="Back",
                             width=5,
                             font=("Helvetica", 8, "bold"),
                             bg="#52b788",
                             fg="#fff",
                             activebackground="#40916c",
                             activeforeground="#e0e0e0",
                             command=lambda: self.switch_frames(self.entry_frame))
        back_btn.place(x=215, y=90)

        self.black_piece_img = tk.PhotoImage(file="assets/blackPiece.png")
        black_piece_lbl = tk.Label(top_frame, image=self.black_piece_img, bg="#1b4332")
        black_piece_lbl.place(x=40, y=10)

        self.white_piece_img = tk.PhotoImage(file="assets/whitePiece.png")
        white_piece_lbl = tk.Label(top_frame, image=self.white_piece_img, bg="#1b4332")
        white_piece_lbl.place(x=350, y=10)

        self.score_lbl = tk.Label(top_frame,
                                text="0 - 0",
                                font=("Helvetica", 32, "bold"),
                                bg="#1b4332",
                                fg="#fff")
        self.score_lbl.place(x=180, y=25)

        bot_frame = tk.Frame(self.game_frame, height="480")
        bot_frame.pack(side="bottom", fill="x")

        self.canvas = tk.Canvas(bot_frame, width=8 * CELL_SIZE, height=8 * CELL_SIZE, bg="green")
        self.canvas.pack()
        self.canvas.bind("<Button-1>", self.click)
        self.update_board()

    def switch_frames(self, frame: tk.Frame, lvl: int=None) -> None:
        """
            This method switches the frames.
            Args:
                frame (tk.Frame): The frame to be raised.
                lvl (int): The level of the computer (easy, medium, hard).
        """
        if lvl is not None:
            self.board.reset_othello_board()
            self.current_player = BLACK
            self.last_move = None
            self.lvl = lvl
            self.update_board()
            self.agent = AI()
        frame.tkraise()
    
    def update_board(self) -> None:
        """ This method updates the drawn board. """
        self.canvas.delete("all")
        for r in range(ROWS):
            for c in range(COLS):
                x0, y0 = c * CELL_SIZE, r * CELL_SIZE
                x1, y1 = x0 + CELL_SIZE, y0 + CELL_SIZE
                self.canvas.create_rectangle(x0, y0, x1, y1, outline="black", fill="green")

                if self.board.board[r][c] == BLACK:
                    self.canvas.create_oval(x0 + 5, y0 + 5, x1 - 5, y1 - 5, fill="black")
                elif self.board.board[r][c] == WHITE:
                    self.canvas.create_oval(x0 + 5, y0 + 5, x1 - 5, y1 - 5, fill="white")
                elif self.othello.valid_move(self.board.board, r, c, self.current_player):
                    self.canvas.create_oval(x0 + 5, y0 + 5, x1 - 5, y1 - 5, fill="green")

        if self.last_move:
            self.mark_last_play()
        # update score board
        self.update_score_board()
    
    def mark_last_play(self) -> None:
        """ This method marks the last play. """
        row, col = self.last_move
        x0, y0 = col * CELL_SIZE, row * CELL_SIZE
        x1, y1 = x0 + CELL_SIZE, y0 + CELL_SIZE
        self.canvas.create_oval(x0 + 27, y0 + 27, x1 - 27, y1 - 27, fill="red")
    
    def update_score_board(self) -> None:
        """ This method updates the score board. """
        black_score, white_score = self.othello.count_pieces(self.board.board)
        self.score_lbl.config(text=f"{black_score} - {white_score}")
    
    def click(self, event: tk.Event) -> None:
        """
            This method handles the mouse click event.
            Args:
                event (tk.Event): The event object.
        """
        col = event.x // CELL_SIZE
        row = event.y // CELL_SIZE

        if self.othello.valid_move(self.board.board, row, col, self.current_player):
            self.othello.make_move(self.board.board, row, col, self.current_player)
            self.last_move = (row, col)
            self.current_player = WHITE if self.current_player == BLACK else BLACK
            self.update_board()

            if self.player_blocked():
                self.current_player = WHITE if self.current_player == BLACK else BLACK
                self.update_board()

            if self.othello.game_over(self.board.board):
                self.show_result()
            elif self.lvl >= 1 and self.current_player == WHITE:
                self.computer_move()
    
    def player_blocked(self) -> bool:
        """ This method checks if the current player have no moves. """
        valid_moves = self.othello.get_valid_moves(self.board.board, self.current_player)
        return not valid_moves
    
    def show_result(self) -> None:
        """ This method shows the result of the game. """
        black_score, white_score = self.othello.count_pieces(self.board.board)
        if black_score > white_score:
            messagebox.showinfo("Game Over", "Black wins!")
        elif black_score < white_score:
            messagebox.showinfo("Game Over", "White wins!")
        else:
            messagebox.showinfo("Game Over", "It's a tie!")
    
    def computer_move(self) -> None:
        """ This method makes the computer move. """
        row, col = self.agent.minimax(self.board.board, self.lvl, float("-inf"), float("inf"), self.current_player)[1]
        self.othello.make_move(self.board.board, row, col, self.current_player)
        self.last_move = (row, col)
        self.current_player = WHITE if self.current_player == BLACK else BLACK
        self.update_board()

        if self.player_blocked():
            self.current_player = WHITE if self.current_player == BLACK else BLACK
            self.update_board()

        if self.othello.game_over(self.board.board):
            self.show_result()