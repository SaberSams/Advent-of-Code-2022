data = """[H]                 [Z]         [J]
[L]     [W] [B]     [G]         [R]
[R]     [G] [S]     [J] [H]     [Q]
[F]     [N] [T] [J] [P] [R]     [F]
[B]     [C] [M] [R] [Q] [F] [G] [P]
[C] [D] [F] [D] [D] [D] [T] [M] [G]
[J] [C] [J] [J] [C] [L] [Z] [V] [B]
[M] [Z] [H] [P] [N] [W] [P] [L] [C]
 1   2   3   4   5   6   7   8   9 

move 3 from 2 to 1
move 8 from 6 to 4
move 4 from 8 to 2"""

M = []
for line in data.split("\n"):
  if line.split()[0] == "1": break
  M = M + [[*line]]

N = []
for i in range(1, len(M[0]), 4):
  n = []
  for j in reversed(range(0, len(M))):
    if M[j][i] == " ": continue
    n += [M[j][i]]
  N += [n]

for n in N:
  print(n)
