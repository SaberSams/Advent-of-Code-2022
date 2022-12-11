import math

with open('input.txt') as file:
  lines = file.readlines()


def priority(c):
  if ord(c) >= 97:
    return ord(c) - 97 + 1
  else:
    return ord(c) - 65 + 26 + 1


def part_one():
  sum = 0
  for line in lines:
    mid = math.floor(len(line) / 2)
    l, r = line[0:mid], line[mid:-1]
    for c in l:
      if c in r:
        sum += priority(c)
        break
  return sum


def part_two():
  sum = 0
  for x in range(0, len(lines), 3):
    (x, y, z) = (lines[x].strip(), lines[x + 1].strip(), lines[x + 2].strip())
    for c in x:
      if c in y:
        if c in z:
          sum += priority(c)
          break
  return sum


print(f"{part_one()} {part_two()}")
