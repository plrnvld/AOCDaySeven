file = open('Input.txt', 'r')
crabText = file.readlines()[0].split(",")
crabs = list(map(lambda c: int(c), crabText))
print(f'Crabs count {len(crabs)}.')

minCrab = min(crabs)
maxCrab = max(crabs)
print(f'Min {minCrab} and max {maxCrab}.')

def calc_fuel(all_crabs,center_pos):
  fuel = 0
  for c in all_crabs:
    fuel += abs(c - center_pos)
  return fuel

minFuel = len(crabs) * maxCrab

for pos in range(minCrab, maxCrab):
  res = calc_fuel(crabs, pos)
  if res < minFuel:
      minFuel = res

print(f'Min fuel {minFuel}.')




