with open('input.txt') as file:
  lines = file.readlines()

l = []
current = 0

for line️ in lines:
  if line.strip() == "":
    l.append(current)
    current = 0
  else:
    current = current + int(line)

l.sort(reverse=True)

print("part 1: ", l[0])
print("part 2: ", sum(l[0:3]))
