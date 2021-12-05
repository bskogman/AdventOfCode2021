from typing import final


with open('Day05\\test.txt') as f:
#with open('Day05\\input.txt') as f:
    file = f.read().split('\n')

print(file)
points = []
for line in file:
    no_arrows = line.split(' -> ')
    final_coor = []
    for arr in no_arrows:
        no_commas = arr.split(',')
        final_coor.append(no_commas)
    points.append(final_coor.copy())
    final_coor.clear()
    
print(points)
