import numpy as np
from operator import add

def solve(filename, SNEK_SIZE):

  def is_neigbor(x, y):
    (a, b), (c, d) = x, y
    return a - 1 <= c <= a + 1 and b - 1 <= d <= b + 1

  def traverse(x, y):
    (a, b), (c, d) = x, y
    if is_neigbor((a, b),(c, d)): return (a, b)
    ## Same Row
    if a == c: 
      return (a, b + 1) if d > b else (a, b - 1)
    ## Same Col
    if b == d:
      return (a + 1, b) if c > a else (a - 1, b)
    ## Above
    if c > a:
      return (a + 1, b + 1) if d > b else (a + 1, b - 1)
    ## Below
    if c < a: 
      return (a - 1, b + 1) if d > b else (a - 1, b - 1)

  # stores the coordinates of each node
  visited = [[(0,0)] for x in range(SNEK_SIZE)]

  with open(filename) as file: 
    lines = file.readlines()
    
  for line in lines:
    # set the vector of the head for the current command and count of steps in that direction
    command, value = line.strip().split(" ")
    velocity = int(value)
    vector = [(1, 0), (0, -1), (0, 1), (-1, 0)][[*"ULRD"].index(command)]
  
    # for each step in the current command update the path
    for i in range(velocity):
      visited[0] += [tuple(map(add, vector, visited[0][-1]))]
  
      # Update every node
      for i in range(1, SNEK_SIZE):
        visited[i] += [ traverse(visited[i][-1], visited[i-1][-1]) ]
        
  return visited

"""
### Part 2 ###
"""
# solve the snakes path
snake_path = solve("input.txt", 10)
#print(snake_path[9])
# extract the tails location
#print(last_node)
# find the count of unique values in the tails path
unique_nodes = []
[unique_nodes.append(x) for x in snake_path[-1] if x not in unique_nodes]
#print(unique_nodes)
print(unique_nodes)
print(len(unique_nodes))
