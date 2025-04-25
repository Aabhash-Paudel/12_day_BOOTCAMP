a = [
    {"name": "raju", "age": 23, "marks": [45, 50, 40, 60]},
    {"name": "rose", "age": 23, "marks": [45, 50, 40, 60]},
    {"name": "jack", "age": 23, "marks": [45, 50, 40, 60]},
    {"name": "ravi", "age": 23, "marks": [45, 50, 40, 60]},
]


for i in a:
    per = sum(i["marks"]) // 4
    i["p"] = per

pos = 0
rank = ["first", "second", "third", "fourth"]
for i in a:
    print(f"{i["name"]} has scored {i["p"]}% ->{rank[pos]}")
    pos += 1
