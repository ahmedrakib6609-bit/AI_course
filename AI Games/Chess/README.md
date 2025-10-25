♟️ AI Chess Game (Human vs Minimax)🎯 
Project DescriptionThis project implements a two-player Chess game where the human player (White) competes against an Artificial Intelligence (Black). The AI uses the Minimax Algorithm to determine its best move by searching through the game tree up to a defined depth.

🛠️ Requirements and Setup 

i. How to run your:

1.fileSave the File: Save the provided code as chess_minimax.py.
2.Terminal/Command Prompt: Open a terminal or command prompt in the directory where you saved the file and run the following command:python chess_minimax.py
3.A Graphical User Interface (GUI) of the chessboard will open.

ii. Any software/library/framework needs to pre-install

To run the game, you need the following Python library installed:
Python 3+tkinter: 
Usually included with standard Python installations.python-chess: 
This powerful library handles all the core chess logic, rules, and board manipulation. You must install it using pip:
pip install python-chess

🕹️ Gameplay and Visuals

iii. Describe how to play that game (Gameplay)

Player: You control the White pieces.
AI Opponent: The AI controls the Black pieces.
Making a Move:Click on the piece you want to move.
Possible destinations will be highlighted in yellow (move) or red (capture).
Click on the destination square to complete your move.
The AI will automatically make its move shortly after yours.

  AI Difficulty Level:

Use the "🎯 Level" button below the board to change the AI's difficulty, which directly relates to the Minimax search depth:
Easy (Depth 1): The AI only looks at the immediate result of the next move.
Medium (Depth 2): The AI analyzes up to 2 future moves (balanced challenge).
Hard (Depth 3): The AI analyzes up to 3 future moves (very strong challenge).
Pause/Resume: Use the "⏸ Pause" button to temporarily stop the game.

🧠 AI Algorithm 

iv. Which algorithm is used for that game

Algorithm Name: Minimax Algorithm
The Minimax Algorithm is employed here to find the optimal move for the AI (Black).
Algorithm Functionality:
1.Objective: Minimax is a recursive decision-making algorithm used in two-player, zero-sum games. It finds the move that minimizes the maximum possible loss for the AI (Minimizing Player) and maximizes the minimum possible gain for the Human (Maximizing Player).
2.Heuristic/Evaluation Function:The AI evaluates the board primarily based on Material Value (Pawn=1, Queen=9, King=1000, etc.).The score is determined by subtracting the Black pieces' value from the White pieces' value. A positive score favors White, and a negative score favors Black (the AI).
3.Search Depth: The complexity of the AI's decision is controlled by the 'Depth' parameter in the Minimax function, which is adjusted by the difficulty level (1, 2, or 3).
