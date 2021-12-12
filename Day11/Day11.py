# with open('Day11\\test.txt') as f:
with open('Day11\\input.txt') as f:
    file = f.read().split('\n')

flash_levels = []
for line in file:
    new_line = []
    for c in line:
        new_line.append(int(c))
    flash_levels.append(new_line)

def has_flashing_octo(octos:list[list[int]]):
    big_num = 0
    for i in range(0,len(octos)):
        for j in range(0,len(octos[i])):
            if octos[i][j] > big_num:
                big_num = octos[i][j]
    if big_num > 9:
        return True
    else: return False

def non_nine_adj(coords:list[int],octos:list[list[int]]):
    adj = []
    x = coords[0]
    y = coords[1]
    if y-1 != -1:
        new_element = octos[y-1][x]
        if (new_element <= 9) and (octos[y][x] < new_element):
            adj.append([x,y-1])
    if y+1 < len(octos):
        new_element = octos[y+1][x]
        if (new_element <= 9) and (octos[y][x] < new_element):
            adj.append([x,y+1])
    if x-1 != -1:
        new_element = octos[y][x-1]
        if (new_element <= 9) and (octos[y][x] < new_element):
            adj.append([x-1,y])
    if x+1 < len(octos[y]):
        new_element = octos[y][x+1]
        if (new_element <= 9) and (octos[y][x] < new_element):
            adj.append([x+1,y])
    return adj

def simulate_flashes(octos:list[list[int]],num_steps:int):
    flash_list = []
    for x in range(0,num_steps):
        octos_to_flash = [] # didn't need for pt 1, but I still like the idea of it
        for i in range(0,len(octos)):
            for j in range(0,len(octos[i])):
                octos[i][j] += 1
                if octos[i][j] > 9:
                    octos_to_flash.append([j,i])
        while has_flashing_octo(octos) == True:
            for i in range(0,len(octos)):
                for j in range(0,len(octos[i])):
                    if octos[i][j] > 9:
                        if i-1 != -1:
                            octos[i-1][j] += 1
                            if j-1 != -1:
                                octos[i-1][j-1] += 1
                            if j+1 < len(octos[i]): 
                                octos[i-1][j+1] += 1   
                        if i+1 < len(octos):
                            octos[i+1][j] += 1
                            if j-1 != -1:
                                octos[i+1][j-1] += 1
                            if j+1 < len(octos[i]): 
                                octos[i+1][j+1] += 1   
                        if j-1 != -1:
                            octos[i][j-1] += 1
                        if j+1 < len(octos[i]):
                            octos[i][j+1] += 1
                        octos[i][j] = -1000
        total_flashes = 0
        for i in range(0,len(octos)):
            for j in range(0,len(octos[i])):
                if octos[i][j] < 0:
                    total_flashes += 1
                    octos[i][j] = 0
        flash_list.append(total_flashes)
    return sum(flash_list)

print("Answer for Pt 1: ",simulate_flashes(flash_levels,100))


