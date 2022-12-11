FILE_NAME = "input.txt"

with open(FILE_NAME) as file:
  lines = file.readlines()

# init the starting state to equal 1
states = [1]

for line in lines:
  match line.strip().split(" "):
    case ["noop"]:
      states += [states[-1]]
    case ["addx", value]:
      value = int(value)
      states += [states[-1]]
      states += [states[-1] + value]

part1 = [states[cycle - 1] * cycle for cycle in [20,60,100,140,180,220]]
print(sum(part1))

### Part 2
for i in range(0, 6): # Rows 
  for j in range(0, 40): # Columns
    cycle = (i * 40) + j # Caluclate the cycle
    sprite = states[cycle] # Get the current cycles sprite location
    
    # if the current rows falls in the sprite
    if j in [sprite - 1, sprite, sprite + 1]: 
      print("#", end="")
    else:
      print(".", end="")
  print("")