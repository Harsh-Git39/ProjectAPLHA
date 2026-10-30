# Online Python compiler (interpreter)
# Write and run Python online using this editor.
from collections import deque

initial = (("A", "Table") , ("B" , "Table"), ("C" , "Table"))
goal = (("A", "B") , ("B", "C"), ("C" , "Table"))


def get_moves(state):
  moves = []

  blocked = [y for x, y in state if y != "Table"]

  for block, pos in state:

    if block in blocked:
      continue

    if pos != "Table":

      new = [(b, "Table" if b == block else p) for b, p in state]

      moves.append((tuple(sorted(new)), "Moves " + block + "onto table"))

    for target , p in state:
      
      if target != block and target not in blocked:
        
        new = [(b, target if b == block else p) for b, p in state]

        moves.append((tuple(sorted(new)), "Moves " + block + " onto " + target))

        

  return moves
      


def bfs(start, goal):
   vis = {start}
   queue = deque([(start, [])])


   while queue:
     state , path = queue.popleft()

     if state == goal:
       return path

     for new_state, action in get_moves(state):
       if new_state not in vis:
         vis.add(new_state)
         queue.append((new_state, path + [action]))
         
   return None


sol = bfs(initial, goal)

print("block world using BFS")

print("Initial", initial)
print("Goal state", goal)

print("soln")

if sol:
  for i, action in enumerate(sol, 1):
    print("Step" , i , ":" , action)
else:
  print("No solution found")

       
