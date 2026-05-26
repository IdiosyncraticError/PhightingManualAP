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
    for ab in abilities:
        obj = {}
        obj["count"] = 1
        obj["name"] = phighter + " " + ab + " Unlock"
    if phighter == "Sword":
        for ab in abilities:
            pass
    if phighter == "Skateboard":
        for ab in abilities:
            pass
    if phighter == "Scythe":
        for ab in abilities:
            pass
    if phighter == "Coil":
        for ab in abilities:
            pass

with open("data.json", "w") as file:
    json.dump(output, file, indent=4)