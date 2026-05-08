Maze-Assignment
Maze Generator and Solver (DFS + Backtracking)
Menal Abdulkadir------UGR/7907/16------Section 1
Project Overview

This project is a maze generator and solver built using Python’s Turtle graphics module.

It uses a Depth-First Search (DFS) algorithm with stack-based backtracking (often called “mouse logic”) to first generate a perfect maze and then solve it visually.

The program provides real-time animation for both stages:

Maze generation process
Maze solving process
How the Maze Generator Works

The maze is created using an iterative DFS approach with a stack:

Start at the initial cell (0, 0)
Mark the current cell as visited
Randomly select an unvisited neighboring cell (up, down, left, or right)
Remove the wall between the current cell and the chosen cell:
northWall[row][col]
eastWall[row][col]
Push the new cell onto the stack
If no unvisited neighbors exist, backtrack using stack pop
Repeat until all cells are visited

This process generates a perfect maze, meaning every cell is reachable and there are no isolated sections or loops.

Data Structures Used
Wall Representation
northWall[ROWS][COLS]
eastWall[ROWS][COLS]

Values:

1 → wall exists
0 → wall removed

These arrays define the maze structure.

Visited Tracking
visited[ROWS][COLS] → tracks cells during maze generation
solve_visited[ROWS][COLS] → tracks visited cells during solving
Stack (DFS Backtracking)

A stack is used in both phases:

Maze generation
Maze solving

It helps store the current path and allows backtracking when no moves are available.

Start and Exit Points
Start: (0, 0) → top-left corner
Exit: (ROWS - 1, COLS - 1) → bottom-right corner
Entrance & Exit Setup:
Left boundary is open at the start cell
Right boundary is open at the end cell
Maze Solver (Backtracking Algorithm)

The solver works as follows:

Starts at (0, 0)
Uses DFS with a stack to explore paths
Moves only through open passages (where walls are removed)
Marks visited cells to prevent cycles
Backtracks when no valid moves are available
Stops when it reaches the exit cell
Visual Output:
Red trail → current exploration path
Blue marks → dead ends (backtracking points)
Visualization (Turtle Graphics)

Two separate turtles are used:

maze_turtle → draws the maze layout
solver_turtle → animates the solving process

The animation shows:

Maze carving in real time
Step-by-step solving movement
How to Run 
python maze.py
