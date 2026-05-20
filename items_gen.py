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

victory = {
    "name": "victory",
    "victory": "true",
    
}

output = []
for phighter in phighters:
    obj = {}
    obj["name"] = phighter + " Win Condition"
    obj["category"] = ["Win Progression"]
    obj["requires"] = "{OptionCount(@" + phighter + " Tracker, total_map_win_count)}"
    output.append(obj)

for m in maps:
    for phighter in phighters:
        obj = {}
        obj["name"] = phighter + " " + m + " Tracker"
        obj["category"] = ["Tracker", phighter + " Tracker"]
        obj["copy_location"] = "Win on " + m + " - " + phighter
        output.append(obj)    

with open("data.json", "w") as file:
    json.dump(output, file, indent=4)