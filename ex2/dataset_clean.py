import json
import re

with open("dataset.json", "r", encoding='utf-8') as file:
    content = json.load(file)

def break_strin2list(value):

    regex = r'\[(.*)\]'
    compiler = re.compile(regex)
    temp = compiler.findall(value)[0]
    r = [v.replace("'", "").strip() for v in temp.split(",")]
    return r if r[0] != "" else []

for book in content:

    book["genres"] = break_strin2list(book["genres"])
    book["characters"] = break_strin2list(book["characters"])
    book["awards"] = break_strin2list(book["awards"])
    book["ratingsByStars"] = break_strin2list(book["ratingsByStars"])
    book["setting"] = break_strin2list(book["setting"])

with open("dataset_2.json", "w", encoding='utf-8') as file:
    file.write(json.dumps(content, ensure_ascii=False))