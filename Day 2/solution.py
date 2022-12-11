# A, X = Rock = 1
# B, Y = Paper = 2
# C, Z = Scissors = 3
# X lose
# Y draw
# Z win

f = "input.txt"
with open(f) as file:
  lines = file.readlines()
  
points = {
  ("A", "X") : 1 + 3,   ("A", "Y") : 2 + 6,   ("A", "Z") : 3 + 0,
  ("B", "X") : 1 + 0,   ("B", "Y") : 2 + 3,   ("B", "Z") : 3 + 6,
  ("C", "X") : 1 + 6,   ("C", "Y") : 2 + 0,   ("C", "Z") : 3 + 3
}

strats = {
  ("A", "X") : 3 + 0,   ("A", "Y") : 1 + 3,   ("A", "Z") : 2 + 6,
  ("B", "X") : 1 + 0,   ("B", "Y") : 2 + 3,   ("B", "Z") : 3 + 6,
  ("C", "X") : 2 + 0,   ("C", "Y") : 3 + 3,   ("C", "Z") : 1 + 6
}

part_1, part_2 = 0, 0

for line in lines:
  elf, you = line.strip().split(" ")
  part_1 = part_1 + points[(elf, you)]
  part_2 = part_2 + strats[(elf, you)]

print("part 1 ", part_1) #11475
print("part 2 ", part_2) #16862

