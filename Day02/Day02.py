file = open("Day02\\input.txt", "r")
course = file.read().split('\n')
course.remove('')
num = len(course)
pos = 0
dep = 0
for x in course: 
    if x[0] == 'f': 
        pos += int(x[-1])
    elif x[0] == 'd':
        dep += int(x[-1])
    elif x[0] == 'u':
        dep -= int(x[-1])
print("Answer for Pt 1: " + str(pos*dep))

pos = 0
dep = 0
aim = 0
for x in course: 
    if x[0] == 'f': 
        pos += int(x[-1])
        dep += aim*int(x[-1])
    elif x[0] == 'd':
        aim += int(x[-1])
    elif x[0] == 'u':
        aim -= int(x[-1])
print("Answer for Pt 2: " + str(pos*dep))

file.close()