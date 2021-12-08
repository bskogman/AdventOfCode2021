# with open('Day08\\test.txt') as f:
with open('Day08\\input.txt') as f:
    file = f.read().split('\n')

new_notes = []
for line in file:
    note = line.split(" | ")
    new_notes.append(note[1])

num_digits_pt1 = 0
for n in new_notes:
    words = n.split(" ")
    for w in words:
        if len(w) in (2,4,3,7):
            num_digits_pt1 += 1

print("Answer for Pt 1: ", num_digits_pt1)

def string_sort(string_cheese:str):
    shredded_cheese = "".join(sorted(string_cheese))
    return shredded_cheese

def string_to_int(cheese_pizza:str):
    if cheese_pizza == 'abcefg':
        return "0"
    elif cheese_pizza == 'cf':
        return "1"
    elif cheese_pizza == 'acdeg':
        return "2"
    elif cheese_pizza == 'acdfg':
        return "3"
    elif cheese_pizza == 'bcdf':
        return "4"
    elif cheese_pizza == 'abdfg':
        return "5"
    elif cheese_pizza == 'abdefg':
        return "6"
    elif cheese_pizza == 'acf':
        return "7"
    elif cheese_pizza == 'abcdefg':
        return "8"
    elif cheese_pizza == 'abcdfg':
        return "9"
    else: return "-1"
    
def line_solver(line:str):
    output = 0
    cipher = {
        "a" : ['a','b','c','d','e','f','g'],
        "b" : ['a','b','c','d','e','f','g'],
        "c" : ['a','b','c','d','e','f','g'],
        "d" : ['a','b','c','d','e','f','g'],
        "e" : ['a','b','c','d','e','f','g'],
        "f" : ['a','b','c','d','e','f','g'],
        "g" : ['a','b','c','d','e','f','g']
    } 
    split_line = line.split(" | ")
    right_side = split_line[1].split(" ")
    signals = split_line[0].split(" ")+right_side.copy()
    for i in range(0,len(signals)):
        signals[i] = string_sort(signals[i])
    # print(signals)
    signal_set = set(signals.copy())
    signals = list(signal_set)
    # print(right_side)
    # print(signals)
    decoders = []
    for s in signals:
        if len(s) in (2,3,4):
            decoders.append(s)
    decoders.sort(key=len)
    
    # process cases for 1, 4, and 7
    for dec in decoders:
        if len(dec) == 2:
            cipher[str(dec[0])] = ['c','f']
            cipher[str(dec[1])] = ['c','f']
            for k in cipher:
                if (k != str(dec[0])) & (k != str(dec[1])):
                    cipher[k].remove('c')
                    cipher[k].remove('f')
        elif len(dec) == 3:
            new_letter_set = set(dec) - set(decoders[0])
            new_letter = new_letter_set.pop()
            cipher[str(new_letter)] = ['a']
            for k in cipher:
                if len(cipher[k]) > 2:
                    cipher[k].remove('a')
        elif len(dec) == 4:
            new_letter_set = set(dec) - set(decoders[0])
            new_letter_1 = new_letter_set.pop()
            new_letter_2 = new_letter_set.pop()
            cipher[str(new_letter_1)] = ['b','d']
            cipher[str(new_letter_2)] = ['b','d']
            for k in cipher:
                if len(cipher[k]) > 2:
                    cipher[k].remove('b')
                    cipher[k].remove('d')

    # process cases for 0, 6, and 9
    length_six = []
    for s in signals:
        if len(s) == 6:
            length_six.append(s)
    c_f_keys = []
    for cip in cipher:
        if cipher[cip] == ['c','f']:
            c_f_keys.append(cip)
    for l in length_six:
        for k in range(0,2):
            if c_f_keys[k] not in l:
                cipher[str(c_f_keys[k])] = ['c']
                if k == 1:
                    cipher[str(c_f_keys[0])] = ['f']
                else: cipher[str(c_f_keys[1])] = ['f']
    b_d_keys = []
    for cip in cipher:
        if cipher[cip] == ['b','d']:
            b_d_keys.append(cip)
    for l in length_six:
        for k in range(0,2):
            if b_d_keys[k] not in l:
                cipher[str(b_d_keys[k])] = ['d']
                if k == 1:
                    cipher[str(b_d_keys[0])] = ['b']
                else: cipher[str(b_d_keys[1])] = ['b']
    e_g_keys = []
    for cip in cipher:
        if cipher[cip] == ['e','g']:
            e_g_keys.append(cip)
    for l in length_six:
        for k in range(0,2):
            if e_g_keys[k] not in l:
                cipher[str(e_g_keys[k])] = ['e']
                if k == 1:
                    cipher[str(e_g_keys[0])] = ['g']
                else: cipher[str(e_g_keys[1])] = ['g']
    right_side_decoded = []
    for r in right_side:
        new_input = ""
        for s in r:
            new_input += cipher[str(s)][0]
        right_side_decoded.append(string_sort(new_input))
    numbers_string = ""
    for rsd in right_side_decoded:
        numbers_string += string_to_int(rsd)
    output = int(numbers_string)
    return output

cum_sum = 0
for line in file:
    cum_sum += line_solver(line)

print("Answer for Pt 2: ", cum_sum)