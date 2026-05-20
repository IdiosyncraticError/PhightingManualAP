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
    """
    range_start = 1
    range_end = 30
    default = 15

# This is called before any manual options are defined, in case you want to define your own with a clean slate or let Manual define over them
def before_options_defined(options: dict[str, Type[Option[Any]]]) -> dict[str, Type[Option[Any]]]:
    options["total_phighter_win_count"] = TotalPhighterWinCount
    options["total_map_win_count"] = TotalMapWinCount
    options["starting_phighter_count"] = StartingPhighterCount
    options["map_count"] = MapChecks
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
    return groups

def after_option_groups_created(groups: list[OptionGroup]) -> list[OptionGroup]:
    return groups
