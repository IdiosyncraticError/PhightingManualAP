import json

phighters = [
    "Sword",
    "Skateboard",
    "Biograft",
    "Katana",
    "Ban Hammer",
    "Rocket",
    "Slingshot",
    "Hyperlaser",
    "Shuriken",
    "Scythe",
    "Medkit",
    "Boombox",
    "Subspace",
    "Vine Staff",
    "Coil"
]

abilities = [
    "M2",
    "E",
    "Q",
    "Phinisher"
]

output = []
for phighter in phighters:
    obj = {}
    obj["count"] = 1
    obj["name"] = phighter + " Unlock"
    obj["category"] = ["Phighter Unlock"]
    obj["progression"] = True
    output.append(obj)
    
for phighter in phighters:
    if phighter == "Sword":
        for ab in abilities:
            obj = {
                "count": 1,
                "name": "Sword Base " + ab + " Unlock"
            }
            pass
    elif phighter == "Skateboard":
        for ab in abilities:
            pass
    elif phighter == "Scythe":
        for ab in abilities:
            pass
    elif phighter == "Coil":
        for ab in abilities:
            pass
    else:
        for ab in abilities:
            obj = {}
            obj["count"] = 1
            obj["name"] = phighter + " " + ab + " Unlock"
            obj["category"] = [phighter + " Ability Unlock"]
            obj["progression"] = True
            output.append(obj)


with open("data.json", "w") as file:
    json.dump(output, file, indent=4)