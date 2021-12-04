#with open('Day04\\test.txt') as f:
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
        boards.append(boardmaker(file[x+1:x+6]))

def checkbingo(game_board:list[list[str]]):
    #check rows
    rowx = 0
    for row in game_board:
        for ind in range(0,len(row)):
            if row[ind] == 'x':
                #print("increasing rowx") 
                rowx += 1
        if rowx == 5:
            return True
        else: rowx = 0        
    #check columns
    colx = 0
    for x in range(0,len(game_board)):
        for y in range(0,len(game_board[0])):
            if game_board[y][x] == 'x':
                colx += 1
        if colx == 5:
            return True
        else: colx = 0
    return False

def markdraw(drawn_num:str,bingo_card:list[list[str]]):
    new_card = []
    for row in bingo_card:
        new_row = []
        for num in row:
            if num == drawn_num:
                new_row.append('x')
            else:
                new_row.append(num)
        new_card.append(new_row)
    return new_card

def scoreboard(bd:list[list[str]]):
    cum_sum = 0
    for row in bd:
        for num in row:
            if num != 'x':
                cum_sum += int(num)
    return cum_sum

winning_num = 0
winning_score = 0
boardspt2 = boards.copy()
for called_num in draw:
    for ind in range(0,len(boards)):
        new_bd = markdraw(called_num,boards[ind])
        if checkbingo(new_bd):
            winning_num = int(called_num)
            winning_score = scoreboard(new_bd)
            break
        else: 
            boards.pop(ind)
            boards.insert(ind,new_bd)
    if winning_score != 0:
        break

print("Answer for Pt 1: " + str(winning_num*winning_score))

indexes = []
for ind in range(0,len(boardspt2)):
    for num_ind in range(0,len(draw)):
        new_bd = markdraw(draw[num_ind],boardspt2[ind])
        if checkbingo(new_bd):
            indexes.append((num_ind,ind))
            boardspt2.pop(ind)
            boardspt2.insert(ind,new_bd)
            break
        else: 
            boardspt2.pop(ind)
            boardspt2.insert(ind,new_bd)

indexes.sort(reverse=True)
winning_num_pt2 = int(draw[indexes[0][0]])
winning_score_pt2 = scoreboard(boardspt2[indexes[0][1]])

print("Answer for Pt 2: " + str(winning_num_pt2*winning_score_pt2))