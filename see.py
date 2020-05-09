import  json
genre_map = {}  # Start -> End, End -> done
with open('testing.json') as f:
    genre_map = json.loads(f.read())
s=0
genres = {}
copy = genre_map.copy()
for genre in genre_map.keys():
    if genre not in genre_map.values():
        del copy[genre]
for genre in copy.keys():
    if genre not in copy.values():
        s+=1
print(s)
