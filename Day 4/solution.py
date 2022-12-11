# 2-4,6-8
# 2-3,4-5
# 5-7,7-9
# 2-8,3-7
# 6-6,4-6
# 2-6,4-8


def parse(s):
  return tuple(
    (int(x), int(y)) for (x, y) in [x.split("-") for x in s.split(",")])


def solve(*args):
  answers = {}
  for arg in args:
    with open(arg) as file:
      lines = file.readlines()

    # containers to store answers
    contains, overlaps = [], []
    
    for line in lines:
      ((a, b), (c, d)) = parse(line)

      # Check if one range contains another
      if (a >= c and b <= d) or (c >= a and d <= b):
        contains += [((a, b), (c, d))]

      # find overlaps of the ranges
      overlap = [x for x in range(max(a, c), min(b, d) + 1)]
      if overlap != []:
        overlaps += [(((a, b), (c, d)) , overlap)]

    answers[arg] = {"contains": contains, "overlaps": overlaps}
  return answers


for key, value in solve("test.txt", "input.txt").items():
  print("===", key, "===")
  print("part 1", ": ", len(value["contains"]))
  print("part 2", ": ", len(value["overlaps"]))


