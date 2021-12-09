# with open('Day09\\test.txt') as f:
with open('Day09\\input.txt') as f:
    file = f.read().split('\n')

def sum_risk_level(levels:list[str]):
    cum_sum = 0
    for y in range(0,len(levels)):
        for x in range(0,len(levels[0])):
            adj = []
            if y == 0:
                # top row
                if x == 0:
                    adj.append(levels[y+1][x])
                    adj.append(levels[y][x+1])
                elif x == len(levels[0])-1:
                    adj.append(levels[y+1][x])
                    adj.append(levels[y][x-1])
                else: 
                    adj.append(levels[y+1][x])
                    adj.append(levels[y][x-1])
                    adj.append(levels[y][x+1])
            elif y == len(levels)-1:
                # bottom row
                if x == 0:
                    adj.append(levels[y-1][x])
                    adj.append(levels[y][x+1])
                elif x == len(levels[0])-1:
                    adj.append(levels[y-1][x])
                    adj.append(levels[y][x-1])
                else: 
                    adj.append(levels[y-1][x])
                    adj.append(levels[y][x-1])
                    adj.append(levels[y][x+1])
            elif x == 0:
                # first column in middle rows
                adj.append(levels[y-1][x])
                adj.append(levels[y+1][x])
                adj.append(levels[y][x+1])
            elif x == len(levels[0])-1:
                # last column in middle rows
                adj.append(levels[y-1][x])
                adj.append(levels[y+1][x])
                adj.append(levels[y][x-1])
            else:
                adj.append(levels[y-1][x])
                adj.append(levels[y+1][x])
                adj.append(levels[y][x-1])
                adj.append(levels[y][x+1])
            if levels[y][x] < min(adj):
                cum_sum += (int(levels[y][x])+1)
    return cum_sum
            
print("Answer for Pt 1: ",sum_risk_level(file))

def find_lowpoints(levels:list[str]):
    lowpoints = []
    for y in range(0,len(levels)):
        for x in range(0,len(levels[0])):
            adj = []
            if y == 0:
                # top row
                if x == 0:
                    adj.append(levels[y+1][x])
                    adj.append(levels[y][x+1])
                elif x == len(levels[0])-1:
                    adj.append(levels[y+1][x])
                    adj.append(levels[y][x-1])
                else: 
                    adj.append(levels[y+1][x])
                    adj.append(levels[y][x-1])
                    adj.append(levels[y][x+1])
            elif y == len(levels)-1:
                # bottom row
                if x == 0:
                    adj.append(levels[y-1][x])
                    adj.append(levels[y][x+1])
                elif x == len(levels[0])-1:
                    adj.append(levels[y-1][x])
                    adj.append(levels[y][x-1])
                else: 
                    adj.append(levels[y-1][x])
                    adj.append(levels[y][x-1])
                    adj.append(levels[y][x+1])
            elif x == 0:
                # first column in middle rows
                adj.append(levels[y-1][x])
                adj.append(levels[y+1][x])
                adj.append(levels[y][x+1])
            elif x == len(levels[0])-1:
                # last column in middle rows
                adj.append(levels[y-1][x])
                adj.append(levels[y+1][x])
                adj.append(levels[y][x-1])
            else:
                adj.append(levels[y-1][x])
                adj.append(levels[y+1][x])
                adj.append(levels[y][x-1])
                adj.append(levels[y][x+1])
            if levels[y][x] < min(adj):
                lowpoints.append([x,y])
    return lowpoints

def non_nine_adj(coords:list[int],levels:list[str]):
    adj = []
    x = coords[0]
    y = coords[1]
    if y-1 != -1:
        new_element = levels[y-1][x]
        if (new_element != '9') and (levels[y][x] < new_element):
            adj.append([x,y-1])
    if y+1 < len(levels):
        new_element = levels[y+1][x]
        if (new_element != '9') and (levels[y][x] < new_element):
            adj.append([x,y+1])
    if x-1 != -1:
        new_element = levels[y][x-1]
        if (new_element != '9') and (levels[y][x] < new_element):
            adj.append([x-1,y])
    if x+1 < len(levels[y]):
        new_element = levels[y][x+1]
        if (new_element != '9') and (levels[y][x] < new_element):
            adj.append([x+1,y])
    return adj

def find_basins(levels:list[str]):
    low_points = find_lowpoints(levels)
    basins = []
    for i in range(0,len(low_points)):
        basins.append(levels[low_points[i][1]][low_points[i][0]])
        lp_adj = non_nine_adj(low_points[i],levels)
        pts_in_basin = []
        for np in lp_adj:
            pts_in_basin.append(np)
        while lp_adj != []:
            search_for = []
            for l in lp_adj:
                add_pts = non_nine_adj(l,levels)
                for s in add_pts:
                    search_for.append(s)
                for n in lp_adj:
                    if n not in pts_in_basin:
                        pts_in_basin.append(n)
            lp_adj = search_for
        for pib in pts_in_basin:
            basins[i] += levels[pib[1]][pib[0]]
    basins.sort(key=len, reverse=True)
    return len(basins[0])*len(basins[1])*len(basins[2])

# time to bring me my money
print("Answer for Pt 2: ",find_basins(file))