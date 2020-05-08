import json
def indexOf(arr, name):
    return next((index for (index, d) in enumerate(arr)
                      if d["name"] == name), None)
genres = {}
with open('testing.json') as f:
    genres = json.loads(f.read())
tree = {'name': 'root', 'children':[]}
for genre in genres:
    stack = []
    start = genre
    print('Starting at',start)
    while True:
        stack.append(start)
        if genres[start] == 'done':
            break
        start = genres[start]
    
    current_tree = tree
    stack.reverse()
    stack = stack[:-1]
    print(stack)
    last_item = stack[-1:]
    print(last_item)
    for item in stack:
        if item not in [c['name'] for c in current_tree['children']]:
            structure = {'name': item}
            if item != last_item:
                structure['children'] = []
            current_tree['children'].append(structure)
        # print('CURRENT TREE', current_tree)
        index = indexOf(current_tree['children'], item)
        current_tree = current_tree['children'][index]
    # tree = current_tree

with open('tree.json','w') as f:
    f.write(json.dumps(tree, indent=2))
