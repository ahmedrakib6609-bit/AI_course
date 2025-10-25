🪨 AI Nim Game (Minimax Strategy)

🎯 Project Description

This project implements the classic impartial game of Nim with a Graphical User Interface (GUI). The game is played between a human user and an Artificial Intelligence (AI). The AI determines its optimal moves using the Minimax Algorithm to ensure a win whenever possible.

🛠️ Requirements and Setup (Point 3.c.i & 3.c.ii)

i. How to run your file

Save the File: Save the provided code as nim_game.py.

Terminal/Command Prompt: Open a terminal or command prompt in the directory where you saved the file and run the following command:

python nim_game.py


A small, interactive GUI window will open, displaying the piles of stones.

ii. Any software/library/framework needs to pre-install

To run the game, you only need:

Python 3+

tkinter: This is a standard Python library used for the GUI and is usually included with Python installations. No external installation is typically required.

🕹️ Gameplay and Visuals (Point 3.c.iii & 3.c.iv)

iii. Describe how to play that game (Gameplay)

Initial Setup: The game starts with three piles of stones: Pile 0 (3 stones), Pile 1 (4 stones), and Pile 2 (5 stones).

Objective (Normal Play): The player who takes the last stone wins.

Turns: The Human player starts first ("Your turn 🧑").

Making a Move:

Below each pile label (e.g., "Pile 0: 3 stones"), you will see buttons labeled -1, -2, etc.

Click on the button that corresponds to the number of stones you wish to remove from that single pile.

After your move, the AI will process its turn and update the piles.

Winning/Losing: The game announces the winner when the piles are empty.

iv. Keep images/Screenshots of the game (Visuals)

(Please insert two screenshots of your running Nim Game GUI here:)

Image 1: Screenshot showing the initial board state with the move buttons.

Image 2: Screenshot showing the "You Win!" or "AI Wins!" message in the info label.

🧠 AI Algorithm (Point 3.c.v)

v. Which algorithm is used for that game

Algorithm Name: Minimax Algorithm (Applied to Nim)

The Minimax Algorithm is used by the AI to play Nim optimally.

Algorithm Functionality:

Decision Tree: Minimax explores the entire game tree from the current state to find the move that leads to a forced win (if one exists).

Evaluation: The game is finite and impartial, allowing for a simple terminal evaluation:

If the end state is reached, the evaluation is 1 for the winner and -1 for the loser (depending on whose turn it was previously).

Optimal Strategy: By assuming the human player will also play optimally, Minimax ensures the AI (Minimizing Player) always chooses a move that minimizes the maximum potential gain for the opponent (Maximizing Player). This is equivalent to finding the P-positions (Previous player winning positions) in Nim theory, guaranteeing the AI's victory when mathematically possible.
