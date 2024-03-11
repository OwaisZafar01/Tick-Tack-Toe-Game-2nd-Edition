Interactive Tic Tac Toe Game in Python

This Python script implements a simple Tic Tac Toe game where two players take turns marking spaces in a 3x3 grid until one player wins by achieving three of their marks in a row, column, or diagonal, or the game ends in a draw. Unlike the previous version, this version takes input from the user to fill in the Tic Tac Toe grid.

Description:
The script prompts users to enter values row by row to fill the Tic Tac Toe grid. It then evaluates the grid to determine if any player has won or if the game has ended in a draw. The game logic remains consistent with the classic Tic Tac Toe rules.

Key Features:
Interactive Input: Players input values to mark their moves, making the game interactive and engaging.
Dynamic Evaluation: The script dynamically evaluates the grid to determine the winner or if the game has ended in a draw.
Simplicity: The code employs basic Python constructs, making it accessible to beginners and easy to understand.
How It Works:
Users are prompted to input values row by row to fill the Tic Tac Toe grid.
The script checks for winning conditions in rows, columns, and diagonals.
If any of these conditions are met, it declares the corresponding player as the winner.
If none of the winning conditions are met and all cells are filled, the game is declared a draw.
Example Usage:

Enter values: 1 2 1
Enter values: 2 1 1
Enter values: 1 1 2

# The output will be: "PLAYER 1 won"
