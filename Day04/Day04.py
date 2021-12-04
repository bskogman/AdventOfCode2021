with open('Day04\\input.txt') as f:
    file = f.read().split('\n')

draw = file[0].split(',')
boards = []
filelen = len(file)

def boardmaker(string_board:list[str]):
    newboard = []
    for line in string_board:
        nums = line.split(' ')
        newnums = nums.copy()
        while(len(newnums) > 5):
            newnums.remove('')
        nums = newnums.copy()
        newboard.append(nums)
    return newboard

for x in range(1,filelen):
    if file[x] == '':
        #print('found a blank at index ' + str(x))
        boards.append(boardmaker(file[x+1:x+6]))




#print(boards)