# with open('Day05\\test.txt') as f:
with open('Day05\\input.txt') as f:
    file = f.read().split('\n')

# file = file[40:50]
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
gridpt2 = []
bigx = 0
bigy = 0
for pts in line_ends:
    for pt in pts:
        if int(pt[0]) > bigx:
            bigx = int(pt[0])
        if int(pt[1]) > bigy:
            bigy = int(pt[1])

empty_row = []
for x in range(0,bigx+1):
    empty_row.append(0)
for y in range(0,bigy+1):
    gridpt1.append(empty_row.copy())
    gridpt2.append(empty_row.copy())

# fill grid with lines for part 1 (only vertical/horizontal)
for ends in line_ends:
    if (ends[0][0] == ends[1][0]):
        # draw horizontal line on grid
        x1 = int(ends[0][0])
        x2 = int(ends[1][0])
        y1 = min(int(ends[0][1]),int(ends[1][1]))
        y2 = max(int(ends[0][1]),int(ends[1][1]))
        for ypts in range(y1,y2+1):
            gridpt1[ypts][x1] += 1
    elif (ends[0][1] == ends[1][1]):
        # draw vertical line on grid
        y1 = int(ends[0][1])
        y2 = int(ends[1][1])
        x1 = min(int(ends[0][0]),int(ends[1][0]))
        x2 = max(int(ends[0][0]),int(ends[1][0]))
        for xpts in range(x1,x2+1):
            gridpt1[y1][xpts] += 1

def findoverlaps(filled_grid):
    cum_sum = 0
    for row in filled_grid:
        for gridpoint in row:
            if gridpoint > 1:
                cum_sum += 1
    return cum_sum
    
pt1overlaps = findoverlaps(gridpt1)
print("Answer for Pt 1: " + str(pt1overlaps))

