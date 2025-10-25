# AI_Course/AI Games/Nim_Game/nim_game.py
# This project implements the Nim Game using a Graphical User Interface (GUI) 
# built with Tkinter, and the Artificial Intelligence (AI) uses the Minimax 
# algorithm for decision-making.

import tkinter as tk
from tkinter import messagebox
import math
from functools import partial

# ---------- Minimax Algorithm Logic ----------

def is_terminal(state):
    """
    Checks if the game state is terminal (game over).
    The game is over when all piles are empty.
    """
    return all(pile == 0 for pile in state)

def evaluate(state, maximizing_player):
    """
    Evaluates the terminal state. 
    In Normal Play Nim (last player to move wins):
    - If it's the Maximizing player's turn (Human) and the state is terminal, the Minimizing player (AI) made the last move and wins.
    - If it's the Minimizing player's turn (AI) and the state is terminal, the Maximizing player (Human) made the last move and wins.
    Minimax score is 1 for the player who wins, -1 for the player who loses.
    """
    # If it's the Maximizing player's turn now, it means the Minimizing player (AI) just moved and won.
    # Therefore, the score favors the Minimizing player (-1).
    return -1 if maximizing_player else 1

def get_children(state):
    """
    Generates all possible next states (legal moves) from the current state.
    A move consists of removing 'remove' stones from 'pile'.
    """
    children = []
    # Iterate through each pile
    for i, pile in enumerate(state):
        # Iterate through all possible number of stones to remove from that pile (1 up to pile size)
        for remove in range(1, pile + 1):
            new_state = state.copy()
            new_state[i] -= remove  # Apply the move
            children.append(new_state)
    return children

def minimax(state, maximizing_player):
    """
    The core Minimax algorithm. It recursively searches the game tree
    to find the optimal move for the current player.
    """
    # Base Case: If the game is over, return the evaluation score and no move.
    if is_terminal(state):
        return evaluate(state, maximizing_player), None

    if maximizing_player:
        # Maximizing Player (AI in this implementation, aiming for highest score)
        max_eval = -math.inf
        best_move = None
        for child in get_children(state):
            # Recurse for the minimizing player
            eval, _ = minimax(child, False)
            if eval > max_eval:
                max_eval = eval
                best_move = child # The 'move' is the resulting state
        return max_eval, best_move
    else:
        # Minimizing Player (Human, trying to minimize the AI's score)
        min_eval = math.inf
        best_move = None
        for child in get_children(state):
            # Recurse for the maximizing player
            eval, _ = minimax(child, True)
            if eval < min_eval:
                min_eval = eval
                best_move = child # The 'move' is the resulting state
        return min_eval, best_move

# ---------- GUI Logic (Tkinter) ----------
class NimGameGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Nim Game 🎮")

        # Initial game state (piles: [3, 4, 5])
        self.state = [3, 4, 5]
        # True means Human's turn, False means AI's turn
        self.player_turn = True 

        # Info label to show whose turn it is or the winner
        self.info_label = tk.Label(root, text="Your turn 🧑", font=("Helvetica", 14, "bold"))
        self.info_label.pack(pady=10)

        # List to hold the Tkinter frames for each pile
        self.pile_frames = []
        self.update_board()

    def update_board(self):
        """Redraws the entire board state (piles and buttons)."""
        # Remove old frames/widgets
        for frame in self.pile_frames:
            frame.destroy()
        self.pile_frames = []

        # Draw current piles and associated move buttons
        for i, pile in enumerate(self.state):
            frame = tk.Frame(self.root, padx=10, pady=5, bd=2, relief=tk.RIDGE)
            frame.pack(pady=5)
            self.pile_frames.append(frame)

            # Label showing current pile size
            label = tk.Label(frame, text=f"Pile {i}: {pile} stones", font=("Helvetica", 12))
            label.pack(side="left", padx=10)

            # Create buttons for removing 1 up to 'pile' stones
            for r in range(1, pile + 1):
                # partial is used to pass arguments (pile index and stone count) to player_move
                btn = tk.Button(
                    frame, 
                    text=f"-{r}", 
                    command=partial(self.player_move, i, r),
                    bg="#4CAF50" if r % 2 == 1 else "#8BC34A",
                    fg="white",
                    activebackground="#388E3C",
                    relief=tk.RAISED
                )
                btn.pack(side="left", padx=2, pady=2)

    def player_move(self, pile, remove):
        """Handles the human player's move."""
        if not self.player_turn:
            # Ignore click if it's the AI's turn
            return
        
        # Validation check (should ideally be handled by button existence, but good practice)
        if remove <= 0 or remove > self.state[pile]:
            return

        # Apply the move
        self.state[pile] -= remove
        
        # Check if the game ended after the human's move
        if self.check_winner():
            return

        # Pass turn to AI
        self.player_turn = False
        self.info_label.config(text="AI thinking... 🤖", fg="red")
        
        # Schedule AI move after a short delay for better user experience
        self.root.after(800, self.ai_move)

    def ai_move(self):
        """Handles the AI's turn using the Minimax result."""
        
        # Minimax: AI is the Maximizing player in the recursive call, aiming for the 'best_move' state
        # The AI (Maximizing player) uses the Minimax function to find the resulting state ('best_move')
        _, best_move = minimax(self.state, True) 
        
        if best_move is not None:
            self.state = best_move # Update game state to the optimal state found by Minimax
        else:
            # Fallback for terminal states (should be caught by check_winner, but safe)
            return 
            
        self.update_board()
        
        # Check if the game ended after the AI's move
        if self.check_winner():
            return
            
        # Pass turn back to Human
        self.player_turn = True
        self.info_label.config(text="Your turn 🧑", fg="blue")

    def check_winner(self):
        """Checks for the end of the game and displays the winner."""
        self.update_board()
        if is_terminal(self.state):
            # If the state is terminal, the player who just moved is the winner (Normal Play)
            winner = "🎉 You Win!" if self.player_turn else "🤖 AI Wins!"
            
            # Update info label with winner
            self.info_label.config(text=winner, fg="green" if self.player_turn else "red")
            
            # Disable all move buttons to stop play
            for frame in self.pile_frames:
                for widget in frame.winfo_children():
                    if isinstance(widget, tk.Button):
                        widget.config(state="disabled")
            return True # Game is over
        return False # Game continues

# ---------- Run Game ----------
if __name__ == "__main__":
    root = tk.Tk()
    game = NimGameGUI(root)
    root.mainloop()
