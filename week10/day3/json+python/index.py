import json

with open("json.json", "r") as f:
    family = json.load(f)
    childrens = family["children"]
    print(childrens)

    for child in childrens:
        print(f"{child['firstName']} - {child['age']}")

    for i in range(len(childrens)):
        childrens[i]["favourite_color"] = "red"
        print(childrens)

with open("json.json", "w") as f:
    json.dump(childrens, f, indent=2)
