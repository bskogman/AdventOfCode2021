from random import choice

# with open('Day12\\test.txt') as f:
# with open('Day12\\test2.txt') as f:
with open('Day12\\input.txt') as f:
    file = f.read().split('\n')

connections = []
for line in file: 
    connections.append(line.split('-'))

distinct_nodes = []
node_dict = {}
for pair in connections:
    if pair[0] not in distinct_nodes:
        distinct_nodes.append(pair[0])
    if pair[1] not in distinct_nodes:
        distinct_nodes.append(pair[1])
# print(distinct_nodes)
for d in distinct_nodes:
    node_dict[d] = []

for pair in connections:
    node_dict[pair[0]].append(pair[1])
    node_dict[pair[1]].append(pair[0])
# print(node_dict)
keys_to_remove = []
for k in node_dict:
    if 'start' in node_dict[k]:
        node_dict[k].remove('start')
    if len(node_dict[k]) == 1:
        keys_to_remove.append(k)
node_dict.pop('end')
for k in keys_to_remove:
    node_dict.pop(k)
    for v in node_dict:
        if k in node_dict[v]:
            node_dict[v].remove(k)
    
def remove_dupes(paths:list[list[str]]):
    new_list = []
    for p in paths:
        if p not in new_list:
            new_list.append(p)
    return new_list

def remove_dupe_smalls(paths:list[list[str]]):
    new_paths = []
    for i in range(0,len(paths)):
        append_flag = 1
        lower_seen = []
        new_list = []
        for j in range(0,len(paths[i])):
            if paths[i][j] not in lower_seen:
                new_list.append(paths[i][j])
                if paths[i][j] != paths[i][j].upper():
                    lower_seen.append(paths[i][j])
            else: 
                append_flag = 0
        if append_flag == 1:
            new_paths.append(new_list)
    return new_paths

# print(node_dict)
full_paths = []
for i in range(0,10000000):
    path = ['start']
    string_path = 'start'
    last_node = path[-1]
    while last_node != 'end':
        random_choice = choice(node_dict[last_node])
        path.append(random_choice)
        string_path += str(','+str(random_choice))
        last_node = path[-1]
    full_paths.append(string_path) 

full_paths = list(set(full_paths))

new_paths = []
for l in full_paths:
    new_paths.append(l.split(','))

full_paths = remove_dupe_smalls(new_paths)
print(len(full_paths))