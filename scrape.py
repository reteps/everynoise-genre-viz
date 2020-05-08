import requests
import json
from bs4 import BeautifulSoup

def getAllLinks(url,row=None):
    res = requests.get(url)
    html = res.content
    soup = BeautifulSoup(html, "lxml")
    if row is not None:
        link = soup.select_one(
        f'tr:nth-of-type({row})').find("a", {'title': 'Re-sort the list starting from here.'})
        return link
    links = soup.find_all("a", {"title": "Re-sort the list starting from here."})

    return links

BASE_URL = 'http://everynoise.com/everynoise1d.cgi'
ROOT_URL = f'{BASE_URL}?scope=all'
GENRE_URL = f'{BASE_URL}?scope=mainstream%20only&root='
root_links = getAllLinks(ROOT_URL)

scores = {}
genre_map = {} # Start -> End, End -> done
with open('testing.json') as f:
    genre_map = json.loads(f.read())
print(genre_map)
START_POS = 4249
for i, a in enumerate(root_links):
    scores[a.text] = i
for i, a in enumerate(root_links[START_POS:]):
    actual_i = i+START_POS
    next_link = BASE_URL + a['href'][:-3] + 'mainstream%20only'
    secondLink = getAllLinks(next_link, row=2)
    if scores[secondLink.text] < actual_i:
        genre_map[a.text] = secondLink.text
        print(actual_i, secondLink.text)
    else:
        genre_map[a.text] = "done"
        print(actual_i, f'{a.text} is the best')
    if (i % 50 == 0):
        with open('testing.json', 'w') as f:
            f.write(json.dumps(genre_map,indent=2))
with open('testing.json', 'w') as f:
    f.write(json.dumps(genre_map, indent=2))
