import turtle
import random
import time

# MAZE SETTINGS
ROWS = 15
COLS = 15
CELL_SIZE = 30

# Data Structures [cite: 11, 12]
northWall = [[1 for _ in range(COLS)] for _ in range(ROWS + 1)] 
eastWall = [[1 for _ in range(COLS + 1)] for _ in range(ROWS)]
visited = [[False for _ in range(COLS)] for _ in range(ROWS)]

# Interior Start/End [cite: 44]
START_ROW, START_COL = 7, 7
END_ROW, END_COL = 12, 12

screen = turtle.Screen()
screen.title("Maze Assignment - Menal Abdulkadir")
screen.setup(width=800, height=800)
screen.tracer(0) # Turn off auto-animation for speed control 

maze_t = turtle.Turtle()
maze_t.hideturtle()
solver_t = turtle.Turtle()
solver_t.hideturtle()
solver_t.penup()

def get_coords(row, col):
    offset_x, offset_y = -(COLS * CELL_SIZE) / 2, -(ROWS * CELL_SIZE) / 2
    return offset_x + col * CELL_SIZE, offset_y + row * CELL_SIZE

def draw_maze():
    maze_t.clear()
    maze_t.pensize(2)
    # Draw Walls [cite: 14, 16, 17]
    for r in range(ROWS + 1):
        for c in range(COLS):
            if northWall[r][c] == 1:
                x, y = get_coords(r, c)
                maze_t.penup(); maze_t.goto(x, y); maze_t.pendown(); maze_t.goto(x + CELL_SIZE, y)
    for r in range(ROWS):
        for c in range(COLS + 1):
            if eastWall[r][c] == 1:
                x, y = get_coords(r, c)
                maze_t.penup(); maze_t.goto(x, y); maze_t.pendown(); maze_t.goto(x, y + CELL_SIZE)
    screen.update()

def generate_maze(r, c):
    stack = [(r, c)] # Stack-based DFS [cite: 24, 48]
    visited[r][c] = True
    while stack:
        curr_r, curr_c = stack[-1]
        neighbors = []
        for dr, dc, w_type, wr, wc in [(1,0,'N',curr_r+1,curr_c), (-1,0,'N',curr_r,curr_c), (0,1,'E',curr_r,curr_c+1), (0,-1,'E',curr_r,curr_c)]:
            nr, nc = curr_r + dr, curr_c + dc
            if 0 <= nr < ROWS and 0 <= nc < COLS:
                if not visited[nr][nc]:
                    neighbors.append((nr, nc, w_type, wr, wc))
                elif random.random() < 0.05: # Create cycles [cite: 44, 56]
                    if w_type == 'N': northWall[wr][wc] = 0
                    else: eastWall[wr][wc] = 0
        if neighbors:
            nr, nc, wt, wr, wc = random.choice(neighbors)
            if wt == 'N': northWall[wr][wc] = 0
            else: eastWall[wr][wc] = 0
            visited[nr][nc] = True
            stack.append((nr, nc))
            draw_maze() # Show mouse eating [cite: 25, 29]
        else:
            stack.pop()
    draw_maze()

def solve_maze():
    stack = [(START_ROW, START_COL)] # Backtracking algorithm [cite: 33, 35]
    solve_visited = set([(START_ROW, START_COL)])
    while stack:
        r, c = stack[-1]
        x, y = get_coords(r, c)
        solver_t.goto(x + CELL_SIZE/2, y + CELL_SIZE/2)
        solver_t.dot(10, "red") # Current path [cite: 36]
        if (r, c) == (END_ROW, END_COL):
            solver_t.dot(15, "green"); screen.update(); break
        moves = []
        # Move logic checking for missing walls [cite: 15, 34]
        if r+1 < ROWS and northWall[r+1][c] == 0 and (r+1, c) not in solve_visited: moves.append((r+1, c))
        if r-1 >= 0 and northWall[r][c] == 0 and (r-1, c) not in solve_visited: moves.append((r-1, c))
        if c+1 < COLS and eastWall[r][c+1] == 0 and (r, c+1) not in solve_visited: moves.append((r, c+1))
        if c-1 >= 0 and eastWall[r][c] == 0 and (r, c-1) not in solve_visited: moves.append((r, c-1))
        if moves:
            nr, nc = random.choice(moves); solve_visited.add((nr, nc)); stack.append((nr, nc))
        else:
            solver_t.dot(10, "blue") # Mark dead ends [cite: 37, 54]
            stack.pop()
        screen.update()
        time.sleep(0.05)

# START
generate_maze(0, 0)
solve_maze()
print("Execution Finished. Close the window manually.")
screen.mainloop() # Stronger than turtle.done() for keeping window open