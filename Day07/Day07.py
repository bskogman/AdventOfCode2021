with open('Day07\\test.txt') as f:
# with open('Day07\\input.txt') as f:
    file = f.read().split(',')

depths = []
for num in file: 
    depths.append(int(num))

