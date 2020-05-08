import  json
genre_map = {}  # Start -> End, End -> done
with open('tree.json') as f:
    genre_map = json.loads(f.read())
s=0
for genre in genre_map['children']:
    print(genre['name'])
    s+=1
print(s)