with open('Day05\\test.txt') as f:
#with open('Day05\\input.txt') as f:
    file = f.read().split('\n')

# parse coordinates
line_ends = []
for line in file:
    no_arrows = line.split(' -> ')
    final_coor = []
    for arr in no_arrows:
        no_commas = arr.split(',')
        final_coor.append(no_commas)
    line_ends.append(final_coor.copy())
    final_coor.clear()

# get height and width
gridpt1 = []
bigx = 0
bigy = 0
for pts in line_ends:
    for pt in pts:
        if int(pt[0]) > bigx:
            bigx = int(pt[0])
        if int(pt[1]) > bigy:
            bigy = int(pt[1])

empty_row = []
for x in range(0,bigx):
    empty_row.append(0)
for y in range(0,bigy):
    gridpt1.append(empty_row.copy())

    