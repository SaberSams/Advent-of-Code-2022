import numpy as np
from functools import reduce

def visible(line, vis = []):
  if line == []: return vis
  
  if vis == []:
    vis = [False for i in range(len(line))]

  max_index = line.index(max(line))
  vis[max_index] = True
  return visible(line[:max_index], vis)


if __name__ == "__main__":
  # load file
  with open("input.txt") as file:
    lines = file.readlines()
  
  M = np.array([[int(y) for y in x.strip()] for x in lines])
  V = np.full(M.shape, False)
  Z = np.full(M.shape, 1)

    
  # Part 1
  for i in range(4):
    M = np.rot90(M)
    V = np.rot90(V)
    
    for idx, row in enumerate(M):
      V[idx] = np.array([item or V[idx][jdx] for jdx, item in enumerate(visible(M[idx].tolist()))])
  print("Part 1:", np.sum(V == True))

  # Part 2
  for i, row in enumerate(M):
    for j, col in enumerate(M):
      views = [ 
        M[:i ,j][::-1], # up
        M[i, :j][::-1], # left
        M[i, j:][1::],  # right
        M[i: ,j][1::]   # down
      ]

      ## Calculate the score for each tree
      for view in views:
        count = 0
        for tree in view:
          count += 1;
          if tree >= M[i][j]: break
            
        Z[i][j] *= count
      
  print("Part 2:\n", Z.max())



  
