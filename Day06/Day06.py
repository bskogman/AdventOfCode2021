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
        # print("starting day: " + str(d))
        new_times = list_times.copy()
        for t in range(0,len(list_times)):
            if list_times[t] == 0:
                new_times.append(8)
                new_times[t] = 6
            else: new_times[t] -= 1
        list_times = new_times.copy()
    return len(list_times)

numfish1 = fishsim(timers1,80)
print("Answer for Pt 1: " + str(numfish1))

def betterfishsim(countdowns:list[int],last_day:int):
    cum_sum = 0
    day_sums = {
        "D0": 0,
        "D1": 0,
        "D2": 0,
        "D3": 0,
        "D4": 0,
        "D5": 0,
        "D6": 0,
        "D7": 0,
        "D8": 0
    }
    for ctdn in countdowns:
        day_sums["D"+str(ctdn)] += 1
    for day in range(0,last_day):
        numzeros = day_sums["D0"]
        day_sums["D0"] = day_sums["D1"]
        day_sums["D1"] = day_sums["D2"]
        day_sums["D2"] = day_sums["D3"]
        day_sums["D3"] = day_sums["D4"]
        day_sums["D4"] = day_sums["D5"]
        day_sums["D5"] = day_sums["D6"]
        day_sums["D6"] = day_sums["D7"]
        day_sums["D7"] = day_sums["D8"]
        if numzeros > 0:
            day_sums["D6"] += numzeros
            day_sums["D8"] = numzeros
        else: day_sums["D8"] = 0
    cum_sum = sum(day_sums.values())
    return cum_sum

numfish2 = betterfishsim(timers2,256)
print("Answer for Pt 2: " + str(numfish2))
