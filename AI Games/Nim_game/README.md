# Nim Game

---

## 🧠 Project Overview

This project implements the **Nim Game** using a **Graphical User Interface (GUI)** built with **Tkinter**. The **AI opponent** is powered by the **Minimax Algorithm**, which ensures the computer plays optimally.

The game follows the **Normal Play Nim rules** — the player who removes the last stone **wins**.

---

## ⚙️ How to Run

1. Make sure **Python 3.x** is installed.
2. Ensure **Tkinter** is available (usually pre-installed). If not, install it using:

   ```bash
   sudo apt install python3-tk   # For Linux
   ```
3. Run the game with:

   ```bash
   python nim_game.py
   ```
4. A GUI window will appear with three piles of stones `[3, 4, 5]`.

---

## 🕹️ How to Play

* **Your Turn (Human):** Click a button to remove 1 or more stones from any pile.
* **AI Turn:** The AI automatically makes its optimal move.
* **Goal:** Take the **last stone** to win.

When the game ends:

* 🎉 *You Win!* → Human wins.
* 🤖 *AI Wins!* → AI wins.

---

## 🧩 Algorithm Used — Minimax

The **Minimax Algorithm** is used for the AI’s decision-making.

* The **AI (Maximizing Player)** tries to maximize its score.
* The **Human (Minimizing Player)** tries to minimize it.
* The AI evaluates every possible move recursively to select the best state.
* Terminal states are evaluated to determine win/loss outcomes.

---

## 📝 Notes

* GUI is developed using **Tkinter Frames** and **Buttons**.
* Buttons get automatically disabled when the game ends.
* Minimax ensures the AI plays with perfect strategy.

---

