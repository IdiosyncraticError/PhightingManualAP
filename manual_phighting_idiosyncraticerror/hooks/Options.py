# Object classes from AP that represent different types of options that you can create
from Options import Option, FreeText, NumericOption, Toggle, DefaultOnToggle, Choice, TextChoice, Range, NamedRange, OptionGroup, PerGameCommonOptions
# These helper methods allow you to determine if an option has been set, or what its value is, for any player in the multiworld
from ..Helpers import is_option_enabled, get_option_value
from typing import Type, Any


####################################################################
# NOTE: At the time that options are created, Manual has no concept of the multiworld or its own world.
#       Options are defined before the world is even created.
#
# Example of creating your own option:
#
#   class MakeThePlayerOP(Toggle):
#       """Should the player be overpowered? Probably not, but you can choose for this to do... something!"""
#       display_name = "Make me OP"
#
#   options["make_op"] = MakeThePlayerOP
#
#
# Then, to see if the option is set, you can call is_option_enabled or get_option_value.
#####################################################################


# To add an option, use the before_options_defined hook below and something like this:
#   options["total_characters_to_win_with"] = TotalCharactersToWinWith
#
class TotalPhighterWinCount(Range):
    """
    Number of phighters you must complete maps on to progress the win condition
    """
    display_name = "Number of characters the map requirement must be completed on to goal"
    range_start = 1
    range_end = 15
    default = 10

class TotalMapWinCount(Range):
    """
    Number of maps each phighter must win to progress the win condition
    """
    display_name = "Number of maps that must be beaten on each Phighter to win"
    range_start = 1
    range_end = 30
    default = 5

class StartingPhighterCount(Range):
    """
    Number of phighter unlocks given at the beginning
    """
    display_name = "Starting Phighter Count"
    range_start = 1
    range_end = 15
    default = 1

class MapChecks(Range):
    """
    Number of maps that will be checks on each phighter.
    If number of locations is not large enough for all the enabled items, the minimum amount of maps per phighter will instead be enabled.
    If number of locations is not large enough for victory requirement, the minimum amount of maps per phighter will be enabled.
    """
    display_name = "Number of map locations per phighter"
    range_start = 1
    range_end = 30
    default = 15

class MVPBadges(Toggle):
    """
    Whether MVP badges (SVP, MVP, the icons to the left of your username) will be checks
    Hover over the badge to see its name
    """
    display_name = "MVP badge locations"

class LuckRounds(Toggle):
    """
    Adds x13, x66.6, and Fractured Space to locations
    """
    display_name = "Special Rounds"

class BonusRounds(Toggle):
    """
    Adds round modifiers to locations
    (phighter beans, bonus damage/speed/phinisher charge, one for all, random phighters)
    """
    display_name = "Bonus Rounds"

class SwordEvents(Toggle):
    """
    Adds one minute left sword events to the location pool
    """
    display_name = "Sword Events"

class Doomsekkar(Toggle):
    """
    Adds defeating Doomsekkar as a location
    """
    display_name = "Doomsekkar"

class Boomball(Toggle):
    """
    Adds Boomball as a location
    """
    display_name = "Boomball"

class PhestivalTitles(Toggle):
    """
    Every phestival title rank becomes a location (final location is earning a +)
    """
    display_name = "Phestival title locations"

class HardLocations(Toggle):
    """
    Adds very challenging locations
    As of now, includes the Pentakill badge and the max Sword Events badge (requires badges to be on)
    """
    display_name = "Challenge Locations"

class Abilitysanity(DefaultOnToggle):
    """
    Each ability will be locked until you receive the corresponding unlock item
    DO NOT TURN THIS ON IN A SYNC
    """
    display_name = "Abilitysanity"

class StartingAbility(Range):
    """
    The number of randomly selected abilities that each phighter will start with (not just starting phighters)
    Highly recommended to have at least 1 to make initial locations less painful to get
    """
    display_name = "Starting Ability Count"
    range_start = 0
    range_end = 3
    default = 1

class SwordAbility(Toggle):
    """
    Sword's normal and empowered abilities are now individually locked
    """
    display_name = "Sword Abilitysanity"

class SkateAbility(Toggle):
    """
    Skateboard's onboard and offboard abilities are now individually locked
    """
    display_name = "Skateboard Abilitysanity"

class ScytheAbility(Toggle):
    """
    Scythe's melee and ranged abilities are now individually locked (including phinisher)
    """
    display_name = "Scythe Abilitysanity"

class CoilAbility(Toggle):
    """
    Each ability is also locked per coil mode (not including phinisher)
    """
    display_name = "Coil Abilitysanity"

class CoilPhinisher(Toggle):
    """
    Each fusion coil ability is individually locked on top of the phinisher itself
    """
    display_name = "Coil Phinishersanity"

class Stickers(Toggle):
    """
    Every sticker bought is a check
    If you turn this on inside a sync bro thats your own fault
    """
    display_name = "Stickersanity"

class StickerRange(Range):
    """
    The total number of sticker checks
    Currently unimplemented
    """
    range_start = 1
    range_end = 39
    default = 10

class Skins(Toggle):
    """
    Each skin is now a check
    """
    display_name = "Skinsanity"

class SkinRange(Range):
    """
    Total number of skin checks
    Currently unimplemented
    """
    range_start = 1
    range_end = 73
    default = 10

class Badges(Toggle):
    """
    Adds badges as a location
    Excludes "caged by the dead" since Doomsekkar has its own setting
    "the one" and "Supreme Survivor" must be toggled with the Challenge Locations option
    Vine Staff's badge is currently unavailable
    """
    display_name = "Achievementsanity"

# This is called before any manual options are defined, in case you want to define your own with a clean slate or let Manual define over them
def before_options_defined(options: dict[str, Type[Option[Any]]]) -> dict[str, Type[Option[Any]]]:
    options["total_phighter_win_count"] = TotalPhighterWinCount
    options["total_map_win_count"] = TotalMapWinCount
    options["starting_phighter_count"] = StartingPhighterCount
    options["map_count"] = MapChecks

    options["mvp_badges"] = MVPBadges
    options["luck_rounds"] = LuckRounds
    options["bonus_rounds"] = BonusRounds
    options["sword_events"] = SwordEvents
    options["doomsekkar"] = Doomsekkar
    options["boomball"] = Boomball
    options["phestival_titles"] = PhestivalTitles
    options["hard_locations"] = HardLocations

    options["abilitysanity"] = Abilitysanity
    options["sword_abilitysanity"] = SwordAbility
    options["skateboard_abilitysanity"] = SkateAbility
    options["scythe_abilitysanity"] = ScytheAbility
    options["coil_abilitysanity"] = CoilAbility
    options["coil_phinishersanity"] = CoilPhinisher

    options["skinsanity"] = Skins
    options["stickersanity"] = Stickers
    options["achievementsanity"] = Badges

    return options

# This is called after any manual options are defined, in case you want to see what options are defined or want to modify the defined options
def after_options_defined(options: Type[PerGameCommonOptions]):
    # To access a modifiable version of options check the dict in options.type_hints
    # For example if you want to change DLC_enabled's display name you would do:
    # options.type_hints["DLC_enabled"].display_name = "New Display Name"

    #  Here's an example on how to add your aliases to the generated goal
    # options.type_hints['goal'].aliases.update({"example": 0, "second_alias": 1})
    # options.type_hints['goal'].options.update({"example": 0, "second_alias": 1})  #for an alias to be valid it must also be in options

    pass

# Use this Hook if you want to add your Option to an Option group (existing or not)
def before_option_groups_created(groups: dict[str, list[Type[Option[Any]]]]) -> dict[str, list[Type[Option[Any]]]]:
    # Uses the format groups['GroupName'] = [TotalCharactersToWinWith]
    groups["Optional Locations"] = [HardLocations, MVPBadges, LuckRounds, BonusRounds, SwordEvents, Doomsekkar, Boomball, PhestivalTitles]
    groups["Abilitysanity"] = [Abilitysanity, SwordAbility, SkateAbility, ScytheAbility, CoilAbility, CoilPhinisher]
    groups["Alt Account Locations"] = [Skins, Stickers, Badges]
    return groups

def after_option_groups_created(groups: list[OptionGroup]) -> list[OptionGroup]:
    return groups
