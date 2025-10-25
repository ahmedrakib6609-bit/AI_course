# AI_Course/AI Games/Chess_Game/chess_minimax.py

import tkinter as tk
from tkinter import messagebox, simpledialog
import chess

# ===================== AI Minimax Algorithm =====================
# Piece values for basic material evaluation (used by the AI)
piece_values = {
    chess.PAWN: 1,
    chess.KNIGHT: 3,
    chess.BISHOP: 3,
    chess.ROOK: 5,
    chess.QUEEN: 9,
    # King value is high to ensure safety is prioritized
    chess.KING: 1000 
}

# Heuristic Evaluation Function: Calculates the material advantage
def evaluate_board(board):
    """
    Evaluates the current board position based purely on material count.
    Positive value favors White, Negative value favors Black (AI).
    """
    value = 0
    # Calculate White's score (Maximizing player)
    for piece_type, val in piece_values.items():
        value += len(board.pieces(piece_type, chess.WHITE)) * val
    
    # Calculate Black's score (Minimizing player, the AI)
    for piece_type, val in piece_values.items():
        value -= len(board.pieces(piece_type, chess.BLACK)) * val
        
    return value

# Minimax Algorithm Implementation
def minimax(board, depth, is_maximizing):
    """
    The core Minimax algorithm for decision making.
    It returns the best score achievable from the current state and the corresponding best move.
    """
    # Base Case: If depth limit is reached or game is over, return the board evaluation.
    if depth == 0 or board.is_game_over():
        return evaluate_board(board), None

    best_move = None
    
    # Maximizing Player (Human - White)
    if is_maximizing:
        max_eval = float('-inf')
        for move in board.legal_moves:
            board.push(move) # Make the move
            eval, _ = minimax(board, depth - 1, False) # Recurse for the minimizing player
            board.pop() # Undo the move (Backtracking)
            if eval > max_eval:
                max_eval = eval
                best_move = move
        return max_eval, best_move
    
    # Minimizing Player (AI - Black)
    else:
        min_eval = float('inf')
        for move in board.legal_moves:
            board.push(move) # Make the move
            eval, _ = minimax(board, depth - 1, True) # Recurse for the maximizing player
            board.pop() # Undo the move (Backtracking)
            if eval < min_eval:
                min_eval = eval
                best_move = move
        return min_eval, best_move

# ===================== GUI Constants =====================
SQUARE_SIZE = 60
COLORS = ["#EEEED2", "#769656"] # light / dark chess colors
HIGHLIGHT_MOVE = "#F7D154"  # Yellow for possible move destination
HIGHLIGHT_CAPTURE = "#E74C3C" # Red for capture squares
CHECK_HIGHLIGHT = "#FF7B7B" # Light red for check signal
CHECKMATE_BLINK_COLOR = "#FF3333" # Strong red blink

# ===================== GUI Class (Tkinter) =====================
class ChessGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Chess Game (Human vs AI)")

        self.canvas = tk.Canvas(root, width=8*SQUARE_SIZE, height=8*SQUARE_SIZE)
        self.canvas.pack()

        # Control buttons setup
        self.button_frame = tk.Frame(root)
        self.button_frame.pack(pady=5)

        self.restart_button = tk.Button(self.button_frame, text="♻ Restart", command=self.restart_game)
        self.restart_button.grid(row=0, column=0, padx=5)

        self.pause_button = tk.Button(self.button_frame, text="⏸ Pause", command=self.toggle_pause)
        self.pause_button.grid(row=0, column=1, padx=5)

        self.level_button = tk.Button(self.button_frame, text="🎯 Level: Medium", command=self.change_level)
        self.level_button.grid(row=0, column=2, padx=5)

        self.board = chess.Board() # Initialize the chess board
        self.selected_square = None
        self.legal_moves_from_selected = []
        self.paused = False

        self.ai_level = "Medium"
        self.ai_depth = 2 # Default AI search depth

        self.blinking = False
        self.blink_rect_id = None

        self.canvas.bind("<Button-1>", self.on_click)
        self.draw_board()

    # ============== DRAWING BOARD AND PIECES ==============
    def draw_board(self):
        self.canvas.delete("all")
        check_square_white = None
        check_square_black = None

        # Check if the current player (White/Human) is in check
        if self.board.is_check():
            king_square = self.board.king(self.board.turn)
            if king_square is not None:
                if self.board.turn == chess.WHITE:
                    check_square_white = king_square
                else:
                    check_square_black = king_square

        for row in range(8):
            for col in range(8):
                square = chess.square(col, 7 - row)
                color = COLORS[(row + col) % 2]

                # Highlight possible destination squares
                for move in self.legal_moves_from_selected:
                    if move.to_square == square:
                        if self.board.piece_at(square):
                            color = HIGHLIGHT_CAPTURE # Capture square highlight
                        else:
                            color = HIGHLIGHT_MOVE # Empty move square highlight

                # Highlight the King if in Check
                if square == check_square_white or square == check_square_black:
                    color = CHECK_HIGHLIGHT

                # Draw the square rectangle
                x1, y1 = col * SQUARE_SIZE, row * SQUARE_SIZE
                x2, y2 = x1 + SQUARE_SIZE, y1 + SQUARE_SIZE
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="")

                # Draw the piece using Unicode symbols
                piece = self.board.piece_at(square)
                if piece:
                    self.canvas.create_text(
                        x1 + SQUARE_SIZE / 2,
                        y1 + SQUARE_SIZE / 2,
                        text=self.get_piece_unicode(piece),
                        font=("Arial", 30)
                    )

    def get_piece_unicode(self, piece):
        """Maps chess.Piece object to corresponding Unicode character."""
        symbols = {
            "P": "♙", "N": "♘", "B": "♗", "R": "♖", "Q": "♕", "K": "♔",
            "p": "♟", "n": "♞", "b": "♝", "r": "♜", "q": "♛", "k": "♚"
        }
        return symbols[piece.symbol()]

    # ============== HANDLE CLICK (USER MOVE) ==============
    def on_click(self, event):
        if self.blinking or self.paused or self.board.is_game_over():
            return

        col = event.x // SQUARE_SIZE
        row = event.y // SQUARE_SIZE
        square = chess.square(col, 7 - row)

        if self.selected_square is None:
            # First click: Select a White piece
            piece = self.board.piece_at(square)
            if piece and piece.color == chess.WHITE:
                self.selected_square = square
                # Find all legal moves originating from the selected square
                self.legal_moves_from_selected = [m for m in self.board.legal_moves if m.from_square == square]
        else:
            # Second click: Attempt to move or deselect
            move = chess.Move(self.selected_square, square)

            # Handle Pawn promotion check
            piece = self.board.piece_at(self.selected_square)
            if piece and piece.piece_type == chess.PAWN and chess.square_rank(square) == 7:
                promotion_choice = self.ask_promotion()
                move = chess.Move(self.selected_square, square, promotion=promotion_choice)

            if move in self.board.legal_moves:
                # Valid move: push the move, clear selection, draw, and trigger AI
                self.board.push(move)
                self.selected_square = None
                self.legal_moves_from_selected = []
                self.draw_board()
                self.check_game_over_and_signal()
                if not self.board.is_game_over():
                    # Delay AI move slightly for better user experience
                    self.root.after(400, self.ai_move)
            else:
                # Invalid move or deselect: clear selection
                self.selected_square = None
                self.legal_moves_from_selected = []

        self.draw_board() # Redraw board for highlights/deselection

    # ============== AI MOVE ==============
    def ai_move(self):
        if self.paused or self.board.is_game_over():
            return

        # Find the best move using Minimax (AI is the Minimizing player - Black)
        _, best_move = minimax(self.board, self.ai_depth, False)
        
        if best_move:
            # Handle AI pawn promotion (always promote to Queen for simplicity)
            if self.board.piece_type_at(best_move.from_square) == chess.PAWN and chess.square_rank(best_move.to_square) == 0:
                best_move = chess.Move(best_move.from_square, best_move.to_square, promotion=chess.QUEEN)
            
            self.board.push(best_move)
            
        self.draw_board()
        self.check_game_over_and_signal()

    # ============== GAME OVER CHECK + SIGNAL ==============
    def check_game_over_and_signal(self):
        if self.board.is_game_over():
            # Handle Checkmate blink signal
            if self.board.is_checkmate():
                # Get the square of the checkmated king (the current turn is the checkmated side)
                checkmated_color = self.board.turn
                king_square = self.board.king(checkmated_color)
                if king_square is not None:
                    self.signal_checkmate_on_square(king_square)

            # Determine and show the result message
            result = self.board.result()
            if result == "1-0":
                winner = "White (Human) Wins!"
            elif result == "0-1":
                winner = "Black (AI) Wins!"
            else:
                winner = "Draw Game!"
            
            # Show the message box after a slight delay
            self.root.after(100, lambda: messagebox.showinfo("Game Over", f"Game Over!\nResult: {winner}"))

    # ============== CHECKMATE BLINKING EFFECT ==============
    def signal_checkmate_on_square(self, square):
        self.blinking = True
        blink_times = 8
        interval = 300 # Blink every 300ms

        # Calculate square coordinates
        file = chess.square_file(square)
        rank = chess.square_rank(square)
        col = file
        row = 7 - rank
        x1, y1 = col * SQUARE_SIZE, row * SQUARE_SIZE
        x2, y2 = x1 + SQUARE_SIZE, y1 + SQUARE_SIZE

        def do_blink(count, show):
            if count <= 0:
                # Stop blinking
                if self.blink_rect_id is not None:
                    self.canvas.delete(self.blink_rect_id)
                    self.blink_rect_id = None
                self.blinking = False
                self.draw_board()
                return
            
            # Toggle color
            if show:
                self.blink_rect_id = self.canvas.create_rectangle(
                    x1+2, y1+2, x2-2, y2-2, fill=CHECKMATE_BLINK_COLOR, outline=""
                )
            else:
                if self.blink_rect_id is not None:
                    self.canvas.delete(self.blink_rect_id)
                    self.blink_rect_id = None
                    
            # Schedule the next blink
            self.root.after(interval, lambda: do_blink(count-1, not show))

        do_blink(blink_times, True)

    # ============== AUXILIARY FUNCTIONS ==============
    def ask_promotion(self):
        """Asks the user for a promotion choice."""
        choice = simpledialog.askstring("Promotion", "Choose piece: Q/R/B/N (default Q)")
        if not choice:
            return chess.QUEEN
        choice = choice.strip().upper()
        return {
            "Q": chess.QUEEN,
            "R": chess.ROOK,
            "B": chess.BISHOP,
            "N": chess.KNIGHT
        }.get(choice, chess.QUEEN)

    def restart_game(self):
        """Resets the board state and GUI."""
        if self.blinking:
            return
        self.board.reset()
        self.selected_square = None
        self.legal_moves_from_selected = []
        self.paused = False
        self.pause_button.config(text="⏸ Pause")
        self.draw_board()

    def toggle_pause(self):
        """Pauses or resumes the game."""
        if self.blinking:
            return
        self.paused = not self.paused
        self.pause_button.config(text="▶ Resume" if self.paused else "⏸ Pause")

    def change_level(self):
        """Cycles through AI difficulty levels (depth)."""
        if self.ai_level == "Easy":
            self.ai_level = "Medium"
            self.ai_depth = 2
        elif self.ai_level == "Medium":
            self.ai_level = "Hard"
            self.ai_depth = 3
        else:
            self.ai_level = "Easy"
            self.ai_depth = 1
        self.level_button.config(text=f"🎯 Level: {self.ai_level}")

# ===================== MAIN EXECUTION =====================
if __name__ == "__main__":
    root = tk.Tk()
    gui = ChessGUI(root)
    root.mainloop()
