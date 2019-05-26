# Data structure for characer stats
# Classic WoW Stats: https://classic.wowhead.com/guides/classic-wow-stats-and-attributes-overview

def create_character_stats():
    stats = {}

    # In the future hopefully this can be filled in based on gear
    stats["Intellect"] = 12
    stats["Strength"] = 12
    stats["Agility"] = 12
    stats["Stamina"] = 12
    stats["Spirit"] = 12

    return stats

def create_weapon_stats():
    stats = {}

    # In the future hopefully this can be filled in based on gear
    stats["Damage"] = [2,3]
    stats["Attack Speed"] = 2
    stats["Attack Power"] = 0
    stats["Crit"] = 5

    return stats

