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

maps = [
    "Banland",
    "BOGIO Skatepark",
    "Chaos Canyon",
    "Craterdust Capital",
    "Darkage Cliffs",
    "DODGEBALL!",
    "Domino Valley",
    "Doomspire",
    "Hotel Elephant",
    "King of the Hill",
    "Nuke The Whales",
    "Protect Telamon",
    "Raven Rock",
    "ROBLOX Arcade",
    "ROBLOX Bowling Alley",
    "ROBLOX City",
    "ROBLOX HQ",
    "ROBLOX Laundromat",
    "ROBLOX Mall",
    "ROBLOX Museum",
    "Rob the ROBLOX Bank",
    "Rocket Arena",
    "Shooting Teapot Observatory",
    "Space Knights",
    "Sword Fight On The Heights",
    "Sword Fighting Tournament",
    "The Bread Factory",
    "The Iron Cafe",
    "Train Demolition",
    "Underground War"
]

mvp_badges = [
    "MVP",
    "SVP",
    "sidekick",
    "perfection",
    "unstoppable",
    "berserker",
    "bloodbath",
    "scourge",
    "bulwark"
]

skins = {
    "Sword": ["Sci-Fi Sword", "Marshmallow Sword", "Follower Sword", "Sunburst Sword", "Harpy Sword"],
    "Skateboard": ["Hoverboard", "Snowboard", "Egobworder", "Surfboard", "Hellboarder"],
    "Biograft": ["Floatie Biograft", "Biocarved", "Betagraft", "Cocoagraft", "Biohazard", "Beetlegraft"],
    "Katana": ["Kramptana", "Moaitana", "Cybertana", "Follower Katana", "Katana Neo", "Fishertana"],
    "Ban Hammer": ["Frankenhammer", "Sunkenhammer", "Clownhammer", "Rockhammer"],
    "Rocket": ["PJ Rocket", "Buster Rocket", "Stargazer Rocket", "Party Rocket"],
    "Slingshot": ["Catshot", "Cozyshot", "Cursedshot", "Seashot", "Bugshot"],
    "Hyperlaser": ["Witchlaser", "Seraphlaser", "Yulaser", "Kittylaser"],
    "Shuriken": ["Shurifin", "Shuri-long", "Astroken", "Shurisuit"],
    "Scythe": ["Dutchman Scythe", "Reaper Scythe"],
    "Medkit": ["Medcarrot", "Pirate Medkit", "Sianachkit", "7MK0", "Bivekit", "Madkit", "Wranglerkit"],
    "Boombox": ["Cooler Boombox", "Eggsquerade Boombox", "Rainbox", "Astrobox", "Boomwave"],
    "Subspace": ["Exorspace", "Cutiespace", "Jesterspace", "Grieferspace", "Outerspace", "Glitchspace"],
    "Vine Staff": ["Valleystaff", "Vine Splash", "Vineberry", "Mothstaff"],
    "Coil": ["Coil 2.0", "Sharkbite Coil", "Punk Coil", "Werecoil"]
}

sticker_count = 39

rng = [
    "a x13 round",
    "a x66.6 round",
    "Fractured Space"
]

bonus_rounds = [
    "One for All",
    "Phighter Beans",
    "Random Phighters",
    "25% more damage",
    "25% more speed",
    "25% more phinisher charge rate"
]

sword_events = [
    "Firebrand",
    "Windforce",
    "Icedagger",
    "Ghostwalker",
    "Venomshank",
    "Darkheart",
    "Illumina",
    "Dom",
    "Valk"
]

phest_titles = [
    "Fan",
    "Member",
    "Enjoyer",
    "Lover",
    "Pawn",
    "Player",
    "Phighter",
    "Pro",
    "Ace",
    "Expert",
    "Knight",
    "Paladin",
    "Champion",
    "Boss",
    "Master",
    "Ruler",
    "Emperor",
    "Monarch",
    "Idol",
    "Divinity",
    "Deity",
    "God",
    "Celestial",
    "Immortal",
    "a +"
]

output = []

victory = {
    "name": "victory",
    "victory": True,
    "requires": "{OptionCount(@Win Progression, total_phighter_win_count)}"
}
output.append(victory)

for m in maps:
    for phighter in phighters:
        obj = {}
        obj["name"] = "Win on " + m + " - " + phighter
        obj["region"] = phighter
        obj["category"] = ["Map Wins", phighter + " Map Wins"]
        output.append(obj)

for b in mvp_badges:
    for phighter in phighters:
        obj = {}
        if b.endswith("VP"):
            obj["name"] = "Be the " + b + " - " + phighter
        else:
            obj["name"] = "Get the " + b + " badge - " + phighter
        
        obj["region"] = phighter
        obj["category"] = ["MVP Badges", phighter + " MVP Badges"]
        output.append(obj)
        
for hi in rng:
    obj = {
        "name": "Experience " + hi,
        "category": ["Luck Rounds"]
    }
    output.append(obj)
    
for hi in bonus_rounds:
    obj = {
        "name": "Experience " + hi,
        "category": ["Bonus Rounds"]
    }
    output.append(obj)

for hi in sword_events:
    obj = {
        "name": "\"Meet\" " + hi,
        "category": ["Sword Events"]
    }
    output.append(obj)

for title in phest_titles:
    obj = {
        "name": "Earn " + title,
        "category": ["Phest Titles"]
    }
    output.append(obj)

doomsekkar = {
    "name": "Defeat Doomsekkar",
    "category": ["Doomsekkar"]
}
output.append(doomsekkar)

boomball = {
    "name": "Play Boomball",
    "category": ["Boomball"]
}

for phighter, skin in skins.items():
    for s in skin:
        obj = {
            "name": "Purchase " + s,
            "region": phighter,
            "category": ["Skins"]
        }
    output.append(obj)

for i in range(sticker_count):
    obj = {
        "name": "Purchase " + str(i+1) + " sticker(s)",
        "category": ["Stickers"]
    }
    output.append(obj)

with open("data.json", "w") as file:
    json.dump(output, file, indent=4)