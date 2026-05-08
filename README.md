# Maze-Assignment

## Maze Generator and Solver (DFS + Backtracking)

### Menal Abdulkadir ------ UGR/7907/16 ------ Section 1

---

## Project Overview

This project is a maze generator and solver built using **Python’s Turtle graphics** module.

It uses a **Depth-First Search (DFS)** algorithm with stack-based backtracking (often called “mouse logic”) to first generate a perfect maze and then solve it visually.

The program provides real-time animation for both stages:
* **Maze generation process**
* **Maze solving process**

---

## How the Maze Generator Works

The maze is created using an iterative DFS approach with a stack:

1. **Start** at the initial cell (0, 0).
2. **Mark** the current cell as visited.
3. **Randomly select** an unvisited neighboring cell (up, down, left, or right).
4. **Remove the wall** between the current cell and the chosen cell:
    * `northWall[row][col]`
    * `eastWall[row][col]`
5. **Push** the new cell onto the stack.
6. **If no unvisited neighbors exist**, backtrack using stack pop.
7. **Repeat** until all cells are visited.

> This process generates a **perfect maze**, meaning every cell is reachable and there are no isolated sections or loops.

---

## Data Structures Used

### Wall Representation
* `northWall[ROWS][COLS]`
* `eastWall[ROWS][COLS]`

**Values:**
* `1` → wall exists
* `0` → wall removed

### Visited Tracking
* `visited[ROWS][COLS]` → tracks cells during maze generation.
* `solve_visited[ROWS][COLS]` → tracks visited cells during solving.

### Stack (DFS Backtracking)
A stack is used in both phases:
* **Maze generation**
* **Maze solving**

---

## Start and Exit Points
* **Start:** `(0, 0)` (top-left corner).
* **Exit:** `(ROWS - 1, COLS - 1)` (bottom-right corner).
* **Entrance & Exit Setup:** Left boundary is open at the start; right boundary is open at the end.

---

## Maze Solver (Backtracking Algorithm)

The solver works as follows:
* Starts at `(0, 0)`.
* Uses DFS with a stack to explore paths.
* Moves only through open passages.
* Marks visited cells to prevent cycles.
* Backtracks when no valid moves are available.
* Stops when it reaches the exit cell.

**Visual Output:**
* <span style="color:red">**Red trail**</span> → current exploration path.
* <span style="color:blue">**Blue marks**</span> → dead ends (backtracking points).

---

## Visualization (Turtle Graphics)

Two separate turtles are used:
1. `maze_turtle` → draws the maze layout.
2. `solver_turtle` → animates the solving process.

---

## How to Run
```bash
python maze.py
