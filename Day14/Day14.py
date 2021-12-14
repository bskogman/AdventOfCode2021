# with open('Day14\\test.txt') as f:
with open('Day14\\input.txt') as f:
    file = f.read().split('\n\n')

first_poly = file[0]
rules = file[1].split('\n')

rules_dict = {}
for r in rules:
    split = r.split(' -> ')
    rules_dict[split[0]] = split[0][0] + split[1]

def make_polymer(template:str,num_steps:int):
    end_polymer = template

    for s in range(0,num_steps):
        temp_polymer = ''
        for i in range(0,(len(end_polymer))):
            if i == (len(end_polymer)-1):
                temp_polymer = temp_polymer + end_polymer[i]
            elif (end_polymer[i] + end_polymer[i+1]) in rules_dict.keys():
                # found matching pair
                temp_polymer = temp_polymer + rules_dict[end_polymer[i:i+2]]
            else:
                temp_polymer = temp_polymer + end_polymer[i]
        end_polymer = temp_polymer

    count_chars = {}
    for p in end_polymer:
        if p in count_chars.keys():
            count_chars[p] += 1
        else:
            count_chars[p] = 1
    return max(count_chars.values())-min(count_chars.values())

print("Answer for Pt 1: ",make_polymer(first_poly,10))

better_rules = {}
for r in rules:
    k,v = r.split( ' -> ')
    better_rules[k] = v

def better_make_polymer(template:str,num_steps:int):
    count_pairs = {}
    for i in range(0,len(template)-1):
        pair = template[i] + template[i+1]
        if pair not in count_pairs.keys():
            count_pairs[pair] = 0
        count_pairs[pair] += 1
    
    for x in range(0,num_steps):
        new_count_pairs = {}
        for p in count_pairs:
            new_letter = better_rules[p]
            first_half = p[0]+new_letter
            second_half = new_letter+p[1]
            if first_half not in new_count_pairs.keys():
                new_count_pairs[first_half] = 0
            if second_half not in new_count_pairs.keys():
                new_count_pairs[second_half] = 0
            new_count_pairs[first_half] += count_pairs[p]
            new_count_pairs[second_half] += count_pairs[p]
        count_pairs = new_count_pairs

    count_chars = {}
    for p in count_pairs:
        if p[0] not in count_chars:
            count_chars[p[0]] = 0
        if p[1] not in count_chars:
            count_chars[p[1]] = 0
        count_chars[p[0]] += count_pairs[p]
        count_chars[p[1]] += count_pairs[p]
    count_chars[template[0]] += 1
    count_chars[template[-1]] += 1
    return int((max(count_chars.values())-min(count_chars.values()))/2)
   
print("Answer for Pt 2: ",better_make_polymer(first_poly,40))