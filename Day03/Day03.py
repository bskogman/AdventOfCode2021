#file = open("Day03\\test.txt", "r")
file = open("Day03\\input.txt", "r")
diag = file.read().split('\n')

numd = len(diag[0])
gamma = ''
epsilon = ''
for x in range(0,numd):
    num0 = 0
    num1 = 0
    for y in diag:
        if y[x] == '0': 
            num0+=1
        else: 
            num1+=1
    if num0 > num1: 
        gamma += '0'
        epsilon += '1'
    else: 
        gamma += '1'
        epsilon += '0'
gammadec = int(gamma,2)
epsilondec = int(epsilon,2)

print("Answer for Pt 1: " + str(gammadec*epsilondec))

oxyrate = ''
co2rate = ''
diagoxy = diag.copy()
remoxy = ''
for x in range(0,numd):
    num0 = 0
    num1 = 0
    for y in diagoxy:
        if y[x] == '0': 
            num0+=1
        else: 
            num1+=1
    if num0 == num1: 
        remoxy = '0'
    elif num0 > num1: 
        remoxy = '1'
    else: 
        remoxy = '0'
    keep = []
    if len(diagoxy) == 1: 
        break    
    else:
        for z in diagoxy: 
            if z[x] != remoxy:
                keep.append(z)
        diagoxy = keep.copy()
oxyrate = diagoxy[0]
oxydec = int(oxyrate,2)

diagco2 = diag.copy()
remco2 = ''
for x in range(0,numd):
    num0 = 0
    num1 = 0
    for y in diagco2:
        if y[x] == '0': 
            num0+=1
        else: 
            num1+=1
    if num0 == num1: 
        remco2 = '1'
    elif num0 > num1: 
        remco2 = '0'
    else: 
        remco2 = '1'
    keep = []
    if len(diagco2) == 1: 
        break    
    else:
        for z in diagco2: 
            if z[x] != remco2:
                keep.append(z)
        diagco2 = keep.copy()
co2rate = diagco2[0]
co2dec = int(co2rate,2)

print("Answer for Pt 2: " + str(oxydec*co2dec))

file.close()