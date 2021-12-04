with open('Day04\\input.txt') as f:
    file = f.read().split('\n')

draw = file[0].split(',')
boards = []
filelen = len(file)

print(file[2:7])
def boardmaker(string_board):
    newboard = []
    for line in string_board:
        nums = line.split(' ')
        print(nums)
        newboard.append(nums)
    print(newboard)
    return newboard

for x in range(1,2):
    if file[x] == '':
        print('found a blank at index ' + str(x))
        
        boards.append(boardmaker(file[x+1:x+6]))

print(boards)