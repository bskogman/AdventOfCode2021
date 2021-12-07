# with open('Day07\\test.txt') as f:
with open('Day07\\input.txt') as f:
    file = f.read().split(',')

depths = []
for num in file: 
    depths.append(int(num))

low_crab = min(depths)
high_crab = max(depths)
tot_fuel1 = 0
tot_fuel2 = 0

for x in range(low_crab,high_crab):
    fuels = []
    for d in depths:
        fuel_cost = abs(x-d)
        fuels.append(fuel_cost)
    new_tot = sum(fuels)
    if tot_fuel1 == 0:
        tot_fuel1 = new_tot
    elif new_tot < tot_fuel1:
        tot_fuel1 = new_tot
    fuels.clear()

print("Answer for Pt 1: " + str(tot_fuel1))

# not efficient but w/e it works
for x in range(low_crab,high_crab):
    fuels = []
    for d in depths:
        units = abs(x-d)
        fuel_cost = 0
        for f in range(0,units+1):
            fuel_cost += f
        fuels.append(fuel_cost)
    new_tot = sum(fuels)
    if tot_fuel2 == 0:
        tot_fuel2 = new_tot
    elif new_tot < tot_fuel2:
        tot_fuel2 = new_tot
    fuels.clear()

print("Answer for Pt 2: " + str(tot_fuel2))