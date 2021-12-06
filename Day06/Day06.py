# with open('Day06\\test.txt') as f:
with open('Day06\\input.txt') as f:
    file = f.read().split(',')
timers1 = []
timers2 = []
for num in file: 
    timers1.append(int(num))
    timers2.append(int(num))

def fishsim(list_times:list[int],end_day:int):
    for d in range(0,end_day):
        print("starting day: " + str(d))
        new_times = list_times.copy()
        for t in range(0,len(list_times)):
            if list_times[t] == 0:
                new_times.append(8)
                new_times[t] = 6
            else: new_times[t] -= 1
        # print(list_times)
        # print(new_times)
        list_times = new_times.copy()
        # print("changed lists")
        # print(list_times)
        # print(new_times)
    return len(list_times)

numfish1 = fishsim(timers1,80)
print("Answer for Pt 1: " + str(numfish1))

# buckle your seatbelts kids, this is slow and messy
numfish2 = fishsim(timers2,256)
print("Answer for Pt 2: " + str(numfish2))