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

skins = []

stickers = []

rng = [
    "x13",
    "x66.6",
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

other = [
    "Defeat Doomsekkar",
    "Experience Boomball",
]

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