# with open('Day10\\test.txt') as f:
with open('Day10\\input.txt') as f:
    file = f.read().split('\n')

bracket_swap = {
    "(": "A",
    ")": "a",
    "[": "B",
    "]": "b",
    "{": "E",
    "}": "e",
    "<": "G",
    ">": "g"
}

pt1_points = {
    'a': 3,
    'b': 57,
    'e': 1197,
    'g': 25137
}

def bracket_to_letter(chunks:list[str]):
    new_chunks = []
    for line in chunks:
        new_str = ''
        for i in line:
            new_str += bracket_swap[i]
        new_chunks.append(new_str)
    return new_chunks

letter_file = bracket_to_letter(file)

corrupted_chars = []
for i in range(0,len(letter_file)):
    work_dir = []
    for j in range(0,len(letter_file[i])):
        if letter_file[i][j] == letter_file[i][j].upper():
            work_dir.append(letter_file[i][j])
        elif letter_file[i][j] == work_dir[-1].lower(): 
            work_dir.pop()
        else:
            corrupted_chars.append(letter_file[i][j])
            break
cum_sum = 0
for cc in corrupted_chars:
    cum_sum += pt1_points[cc]

print("Answer for Pt 1: ", cum_sum)

new_lines = letter_file.copy()
solve_inc = []
for i in range(0,len(letter_file)):
    work_dir = []
    for j in range(0,len(letter_file[i])):
        if letter_file[i][j] == letter_file[i][j].upper():
            work_dir.append(letter_file[i][j])
        elif letter_file[i][j] == work_dir[-1].lower(): 
            work_dir.pop()
        else:
            new_lines.remove(letter_file[i])
            work_dir.clear()
            break
    solve_inc.append(work_dir)

while [] in solve_inc:
    solve_inc.remove([])

for s in solve_inc:
    s.reverse()

pt2_points = {
    "A": 1,
    "B": 2,
    "E": 3,
    "G": 4
}
scores = []
for i in solve_inc:
    total_score = 0
    for j in i:
        total_score = (total_score*5)+pt2_points[j]
    scores.append(total_score)
scores.sort()
middle_score = scores[int((len(scores)-1)/2)]

print("Answer for Pt 2: ",middle_score)