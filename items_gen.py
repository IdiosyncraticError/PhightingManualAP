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
        types = ["", "Base ", "Empowered "]
        for t in types:
            for ab in abilities:
                if ab != "Phinisher" and (t != "Base " or t != "Empowered "):
                    obj = {}
                    obj["count"] = 1
                    obj["name"] = "Sword " + t + ab + " Unlock"
                    if t == "":
                        obj["category"] = ["Sword Ability Unlock", "!Sword Abilitysanity"]
                    else:
                        obj["category"] = ["Sword Ability Unlock", "Sword Abilitysanity"]
                    obj["progression"] = True
    elif phighter == "Skateboard":
        types = ["", "Offboard ", "Onboard "]
        for t in types:
            for ab in abilities:
                if ab != "Phinisher" and (t!= "Offboard " or t != "Onboard "):
                    obj = {}
                    obj["count"] = 1
                    obj["name"] = "Skateboard " + t + ab + " Unlock"
                    if t == "":
                        obj["category"] = ["Skateboard Ability Unlock", "!Skateboard Abilitysanity"]
                    else:
                        obj["category"] = ["Skateboard Ability Unlock", "Skateboard Abilitysanity"]
                    obj["progression"] = True
    elif phighter == "Scythe":
        types = ["", "Melee ", "Ranged "]
        for t in types:
            for ab in abilities:
                obj = {}
                obj["count"] = 1
                obj["name"] = "Scythe " + t + ab + " Unlock"
                if t == "":
                    obj["category"] = ["Scythe Ability Unlock", "!Scythe Abilitysanity"]
                else:
                    obj["category"] = ["Scythe Ability Unlock", "Scythe Abilitysanity"]
                obj["progression"] = True
    elif phighter == "Coil":
        types = ["", "Regen ", "Bounce ", "Haste "]
        for t in types:
            for ab in abilities:
                obj = {}
                obj["count"] = 1
                obj["name"] = "Coil " + t + ab + " Unlock"
                if t == "":
                    obj["category"] = ["Coil Ability Unlock", "!Coil Abilitysanity"]
                else:
                    obj["category"] = ["Coil Ability Unlock", "Coil Abilitysanity"]
                obj["progression"] = True
            for ab in abilities:
                if ab != "Phinisher":
                    obj = {
                        "count": 1,
                        "name": "Coil Phinisher " + ab + " Unlock",
                        "category": ["Coil Ability Unlock", "Coil Phinisher Abilitysanity"],
                        "progression": True
                    }
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