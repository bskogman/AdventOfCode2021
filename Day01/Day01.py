depths = open("Day01\\input.txt", "r")
file = depths.read().split()

readings = []
for line in file:
    readings.append(int(line))
count = 0
numreadings = len(readings)
for x in range(1,numreadings):
    if readings[x] > readings[x-1]: count+=1
print("Count for Pt 1:")
print(count)

readingsums = []
for x in range(0,numreadings-2):
    readingsums.append(int(readings[x]+readings[x+1]+readings[x+2]))
numsums = len(readingsums)
sumscount = 0
for x in range(1,numsums):
    if readingsums[x] > readingsums[x-1]: sumscount+=1
print("Count for Pt 2:")
print(sumscount)

depths.close()