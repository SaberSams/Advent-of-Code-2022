def part_1():
  data = {
  1: "MJCBFRLH", 
  2: "ZCD", 
  3: "HJFCNGW",
  4: "PJDMTSB",
  5: "NCDRJ",
  6: "WLDQPJGH",
  7: "PZTFRH",
  8: "LVMG",
  9: "CBGPFQRJ"
}
    
  with open("input.txt") as file:
    lines = file.readlines()
  
  for line in lines:
    print(line)
    _, amount, _, origin, _, destination = line.strip().split()
    amount = int(amount)
    origin = int(origin)
    destination = int(destination)
  
    for _ in range(0,amount):
      if data[origin] == "": break
      data[destination] = data[destination] + data[origin][-1]
      data[origin] = data[origin][:-1]
  
  for x in data.values():
    print(x[-1], end="")

def part_2():
  data = {
  1: "MJCBFRLH", 
  2: "ZCD", 
  3: "HJFCNGW",
  4: "PJDMTSB",
  5: "NCDRJ",
  6: "WLDQPJGH",
  7: "PZTFRH",
  8: "LVMG",
  9: "CBGPFQRJ"
}
    
  with open("input.txt") as file:
    lines = file.readlines()
  
  for line in lines:
    _, amount, _, origin, _, destination = line.strip().split()
    amount, origin, destination = int(amount), int(origin), int(destination)
    
    amount = min(len(data[origin]), amount)
    data[destination] += data[origin][-amount::]
    data[origin] = data[origin][:-amount]
  
  for x in data.values():
    print(x[-1], end="")

part_2()