# with open('Day09\\test.txt') as f:
with open('Day09\\input.txt') as f:
    file = f.read().split('\n')

# print(file)
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