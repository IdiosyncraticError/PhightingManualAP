from typing import Optional, Any
from BaseClasses import MultiWorld


# Use this if you want to override the default behavior of is_option_enabled
# Return True to enable the category, False to disable it, or None to use the default behavior
def before_is_category_enabled(multiworld: MultiWorld, player: int, category_name: str) -> Optional[bool]:
    from ..Helpers import get_option_value
    phighters = get_option_value(multiworld, player, "enabled_phighters")
    
    if category_name.endswith("Ability Unlock"):
        ab = get_option_value(multiworld, player, "enabled_abilitysanity")
        enabled_ab = []
        for p in ab:
            enabled_ab.append(p + " Ability Unlock")
        
        enabled_phighters = []
        for p in phighters:
            enabled_phighters.append(p + " Ability Unlock")
        print(category_name in enabled_ab and category_name in enabled_phighters)
        print(category_name)
        print(enabled_ab)
        print(enabled_phighters)
        return (category_name in enabled_ab and category_name in enabled_phighters)
    
    if category_name.endswith(" MVP Badges"):
        enabled_phighters = []
        for p in phighters:
            enabled_phighters.append(p + " MVP Badges")
        return category_name in enabled_phighters
    
    if category_name.endswith(" Map Wins"):
        enabled_phighters = []
        for p in phighters:
            enabled_phighters.append(p + " Map Wins")
        return category_name in enabled_phighters

    return None

# Use this if you want to override the default behavior of is_option_enabled
# Return True to enable the item, False to disable it, or None to use the default behavior
def before_is_item_enabled(multiworld: MultiWorld, player: int, item:  dict[str, Any]) -> Optional[bool]:
    from ..Helpers import get_option_value
    if item["name"].endswith(" Unlock"):
        for c in item["category"]: #if ability unlock, does not affect
            if c.endswith(" Ability Unlock"):
                return None
            
        phighters = get_option_value(multiworld, player, "enabled_phighters")
        enabled_phighters = []
        for p in phighters:
            enabled_phighters.append(p + " Unlock")
        return item["name"] in enabled_phighters
    return None

# Use this if you want to override the default behavior of is_option_enabled
# Return True to enable the location, False to disable it, or None to use the default behavior
def before_is_location_enabled(multiworld: MultiWorld, player: int, location:  dict[str, Any]) -> Optional[bool]:
    return None

# Use this if you want to override the default behavior of is_option_enabled
# Return True to enable the event, False to disable it, or None to use the default behavior
def before_is_event_enabled(multiworld: MultiWorld, player: int, event:  dict[str, Any]) -> Optional[bool]:
    return None
