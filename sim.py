# Classic WoW Class simulation
# Want to take in talent tree and run DPS sim.

# Need cd_list to take GCD into account.

damage = 0
num_steps = 0

def choose_spell(priority=None,cd_list=None):
    return "Frostbolt"


def get_cast_time(spellname="spell"):
    return 1

def run_step:
    """
    Function runs one step of the simulation. This will equate to 1 sec in real time.
    """

    # 1.) Choose spell from priority
    spell = choose_spell()
    # 2.) Cast spell
    cast_time = get_cast_time(spell)
    # 3.) Add damage
    
