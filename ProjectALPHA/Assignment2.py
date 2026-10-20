# Model-Based Intelligent Agent in Grid Environment

grid = [
    ['S', '0', '0', '0'],
    ['X', 'X', '0', 'X'],
    ['0', '0', '0', '0'],
    ['X', 'X', '0', 'G']
]

rows = len(grid)
cols = len(grid[0])

# Find Start Position
for i in range(rows):
    for j in range(cols):
        if grid[i][j] == 'S':
            x, y = i, j

visited = []

while True:
    # Store current position
    visited.append((x, y))

    # Goal reached
    if grid[x][y] == 'G':
        print("Goal Reached!")
        break

    # Move Right
    if y + 1 < cols and grid[x][y + 1] != 'X':
        y += 1

    # Else Move Down
    elif x + 1 < rows and grid[x + 1][y] != 'X':
        x += 1

    # No path exists
    else:
        print("No Path Found")
        break

print("\nVisited Cells:")
for cell in visited:
    print(cell)
    
    
    
    
    -------OUTPUT---------
    ubuntu@ubuntu-HP-Pro-SFF-280-G9-Desktop-PC:~/Downloads/TECOB11$ python3 MODEL_BASED.py
No Path Found

Visited Cells:
(0, 0)
(0, 1)
(0, 2)
(0, 3)

