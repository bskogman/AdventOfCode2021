with open('Day11\\test.txt') as f:
# with open('Day11\\input.txt') as f:
    file = f.read().split('\n')

flash_levels = []
for line in file:
    new_line = []
    for c in line:
        new_line.append(int(c))
    flash_levels.append(new_line)

print(flash_levels)

def make_flash(octos:list[list[int]],y_val:int,x_val:int):
    new_octos = []
    return new_octos

def simulate_flashes(octos:list[list[int]],num_steps:int):
    total_flashes = 0
    for x in range(0,num_steps):
        for i in range(0,len(octos)):
            for j in range(0,len(octos[i])):
                octos[i][j] += 1
        print(octos[0])
        for i in range(0,len(octos)):
            for j in range(0,len(octos[i])):
                if octos[i][j] > 9:
                    # make surrounding octos flash
                    # maybe do a while loop if a line has a 9?
                    # remember that an octo can only flash once during a step - keep list of flashed points??
                    octos[i][j] = 0
        print(octos[0])

    return total_flashes

simulate_flashes(flash_levels,10)