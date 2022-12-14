import json

file = open("users.json", mode="r", encoding="utf-8")

data = json.load(file)

print(type(data))

for i in data:
    print(i["name"])