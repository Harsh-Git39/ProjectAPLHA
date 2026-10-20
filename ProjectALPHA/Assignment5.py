from collections import deque

# Initial State:

initial_state = (
    ("A", "Table"),
    ("B", "Table"),
    ("C", "Table")
)

# Goal State:

goal_state = (
    ("A", "B"),
    ("B", "C"),
    ("C", "Table")
)


def get_moves(state):
    """Generate all possible legal moves."""

    moves = []

  
    blocked = {x for x, y in state if y != "Table"}

 
    for block, position in state:

      
        if block in blocked:
            continue

        if position != "Table":

            new_state = list(state)

            for i, (b, p) in enumerate(new_state):
                if b == block:
                    new_state[i] = (b, "Table")

            new_state = tuple(sorted(new_state))

            moves.append(
                (new_state, f"Move {block} to Table")
            )

      
        for target, target_position in state:

            
            if block == target:
                continue

          
            if target in blocked:
                continue

            new_state = list(state)

            for i, (b, p) in enumerate(new_state):
                if b == block:
                    new_state[i] = (b, target)

            new_state = tuple(sorted(new_state))

            moves.append(
                (new_state, f"Move {block} onto {target}")
            )

    return moves


def bfs(initial, goal):
    """Find the shortest path from initial state to goal state."""

    
    queue = deque([(initial, [])])

    visited = {initial}

    while queue:

        current_state, path = queue.popleft()

   
        if current_state == goal:
            return path

        
        for new_state, action in get_moves(current_state):

    
            if new_state not in visited:

                visited.add(new_state)

                
                queue.append(
                    (new_state, path + [action])
                )

  
    return None




solution = bfs(initial_state, goal_state)



print("========================================")
print("       BLOCKS WORLD USING BFS")
print("========================================")

print("\nInitial State:")
print(initial_state)

print("\nGoal State:")
print(goal_state)


print("\nBFS Solution:")

if solution:
    for step, action in enumerate(solution, 1):
        print(f"Step {step}: {action}")
else:
    print("No solution found.")




--------OUTPUT--------



========================================
       BLOCKS WORLD USING BFS
========================================

Initial State:
(('A', 'Table'), ('B', 'Table'), ('C', 'Table'))

Goal State:
(('A', 'B'), ('B', 'C'), ('C', 'Table'))

BFS Solution:
Step 1: Move A onto B
Step 2: Move B onto C

