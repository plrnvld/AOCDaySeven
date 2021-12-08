file = open('Input.txt', 'r')
crabText = file.readlines()[0].split(",")
crabs = list(map(lambda c: int(c), crabText))
print(f'Crabs count {len(crabs)}.')

minCrab = min(crabs)
maxCrab = max(crabs)
print(f'Min {minCrab} and max {maxCrab}.')

def sum_naturals(n):
  return (n*(n+1))/2

def calc_fuel_new_way(x1, x2):
  return sum_naturals(abs(x1 - x2))

def calc_fuel(all_crabs, center_pos):
  fuel = 0
  for c in all_crabs:
    fuel += calc_fuel_new_way(c, center_pos)
  return fuel

bestPos = 0
minFuel = len(crabs) * calc_fuel_new_way(minCrab, maxCrab)

for pos in range(minCrab, maxCrab):
  res = calc_fuel(crabs, pos)
  if res < minFuel:
      minFuel = res
      bestPos = pos

print(f'Min fuel {minFuel}, best pos {bestPos}.')




