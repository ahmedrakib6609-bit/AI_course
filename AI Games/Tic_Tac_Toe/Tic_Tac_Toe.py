import tkinter as tk
from tkinter import messagebox

# --- Global Variables ---
PLAYER = "X"
AI = "O"
EMPTY = " "

# --- Initialize Board ---
board = [[EMPTY for _ in range(3)] for _ in range(3)]

# --- Tkinter Window ---
window = tk.Tk()
window.title("Tic Tac Toe - AI (Minimax)")

buttons = [[None for _ in range(3)] for _ in range(3)]

# --- Winner Check Function ---
def check_winner(bd):
    # Rows
    for row in bd:
        if row[0] == row[1] == row[2] != EMPTY:
            return row[0]
    # Columns
    for c in range(3):
        if bd[0][c] == bd[1][c] == bd[2][c] != EMPTY:
            return bd[0][c]
    # Diagonals
    if bd[0][0] == bd[1][1] == bd[2][2] != EMPTY:
        return bd[0][0]
    if bd[0][2] == bd[1][1] == bd[2][0] != EMPTY:
        return bd[0][2]
    return None

# --- Draw Check ---
def is_full(bd):
    for row in bd:
        if EMPTY in row:
            return False
    return True

# --- Minimax Algorithm ---
def minimax(bd, depth, is_maximizing):
    winner = check_winner(bd)
    if winner == AI:
        return 10 - depth
    elif winner == PLAYER:
        return depth - 10
    elif is_full(bd):
        return 0

    if is_maximizing:
        best_score = -float("inf")
        for i in range(3):
            for j in range(3):
                if bd[i][j] == EMPTY:
                    bd[i][j] = AI
                    score = minimax(bd, depth + 1, False)
                    bd[i][j] = EMPTY
                    best_score = max(best_score, score)
        return best_score
    else:
        best_score = float("inf")
        for i in range(3):
            for j in range(3):
                if bd[i][j] == EMPTY:
                    bd[i][j] = PLAYER
                    score = minimax(bd, depth + 1, True)
                    bd[i][j] = EMPTY
                    best_score = min(best_score, score)
        return best_score

# --- Find Best Move for AI ---
def find_best_move():
    best_score = -float("inf")
    best_move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                board[i][j] = AI
                score = minimax(board, 0, False)
                board[i][j] = EMPTY
                if score > best_score:
                    best_score = score
                    best_move = (i, j)
    return best_move

# --- Handle Player Click ---
def on_click(i, j):
    if board[i][j] == EMPTY:
        board[i][j] = PLAYER
        buttons[i][j].config(text=PLAYER, state="disabled")
        result = check_winner(board)
        if result:
            messagebox.showinfo("Game Over", f"{result} জিতেছে!")
            reset_game()
            return
        elif is_full(board):
            messagebox.showinfo("Game Over", "ড্র হয়েছে!")
            reset_game()
            return

        # AI move
        ai_move = find_best_move()
        if ai_move:
            r, c = ai_move
            board[r][c] = AI
            buttons[r][c].config(text=AI, state="disabled")
            result = check_winner(board)
            if result:
                messagebox.showinfo("Game Over", f"{result} জিতেছে!")
                reset_game()
            elif is_full(board):
                messagebox.showinfo("Game Over", "ড্র হয়েছে!")
                reset_game()

# --- Reset Game ---
def reset_game():
    global board
    board = [[EMPTY for _ in range(3)] for _ in range(3)]
    for i in range(3):
        for j in range(3):
            buttons[i][j].config(text=EMPTY, state="normal")

# --- Create Buttons ---
for i in range(3):
    for j in range(3):
        b = tk.Button(window, text=EMPTY, font=("Helvetica", 24), width=5, height=2,
                      command=lambda i=i, j=j: on_click(i, j))
        b.grid(row=i, column=j)
        buttons[i][j] = b

# --- Run Game ---
window.mainloop()
