# 🎮 Tic Tac Toe - AI (Minimax Algorithm)

## 📘 Overview

This project implements a **Tic Tac Toe Game** where a **human player competes against an AI** that uses the **Minimax Algorithm** for optimal decision-making.
The user interface is built using **Tkinter** (Python’s standard GUI library).

The AI is designed to play **perfectly** — it will **never lose**, though it may sometimes draw.

---

## 🧠 Algorithm Used: Minimax

The **Minimax algorithm** is a recursive algorithm used in decision-making and game theory.
It assumes that the opponent plays optimally and tries to minimize the AI’s score.

### **How it works:**

1. The AI simulates **all possible moves**.
2. It assigns a **score** for each possible game state:

   * `+10` for AI win
   * `-10` for Player win
   * `0` for Draw
3. The AI then chooses the move that **maximizes its score** (minimizes the player’s best chance).

---

## 🖥️ Features

✅ Interactive **Graphical User Interface** built with Tkinter.
✅ Human (`X`) vs AI (`O`).
✅ Uses **Minimax algorithm** for optimal AI decisions.
✅ Displays winner and automatically resets after each match.
✅ Detects **draw** and **win** conditions dynamically.

---

## 🕹️ How to Run

### **Step 1:** Clone or download this repository

```bash
git clone https://github.com/yourusername/AI_Course.git
```

### **Step 2:** Navigate to the Tic Tac Toe folder

```bash
cd AI_Course/AI_Games/Tic_Tac_Toe
```

### **Step 3:** Run the program

```bash
python tic_tac_toe.py
```

---

## 📷 Example Gameplay

Below is an example of how the game looks while playing:

![Tic Tac Toe Gameplay](ttt1.png , ttt2.png , ttt3.png)

---

## 🏁 Game Rules

1. The player (`X`) always goes first.
2. Players take turns placing their symbol (`X` or `O`).
3. The first to get **three in a row** (horizontally, vertically, or diagonally) wins.
4. If all cells are filled and no winner — it’s a **Draw**.

---

## 🧮 Example of AI Decision

At each move, the AI:

* Calculates all possible moves using recursion.
* Assigns a score to each future state.
* Picks the move that leads to the **highest guaranteed score**.

Thus, **the AI cannot be beaten.**

---

## 🧑‍💻 Developed Using

* **Language:** Python
* **Library:** Tkinter (for GUI)
* **Algorithm:** Minimax (with Depth Evaluation)

---

## ✨ Output Example

| Scenario    | Output       |
| ----------- | ------------ |
| Player Wins | `X জিতেছে!`  |
| AI Wins     | `O জিতেছে!`  |
| Draw        | `ড্র হয়েছে!` |

---

## 📚 Learning Outcome

From this project, you’ll understand:

* How the **Minimax algorithm** works in practice.
* How to integrate **AI logic with GUI**.
* How to manage **game states and recursion** efficiently.

---
