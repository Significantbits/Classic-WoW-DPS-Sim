# Classic WoW Class simulation
# Want to take in talent tree and run DPS sim.

import json
import random
import sys
from spell_data import create_spell_data
from character import Character
from global_vars import Global_Vars 

#num_secs = 0 # Keeping track of the number of steps
#time_step_resolution = 0.1 # How many seconds each step is
#seconds_to_run = 20 # Time simulator runs in seconds
#GCD = 1.5 # in seconds

if __name__ == "__main__":
    print("Starting WoW Classic DPS Simulator Version 0.01...")

    g_vars = Global_Vars()
    g_vars.init()
    
    if "-spec" in sys.argv:
        spec = sys.argv[sys.argv.index("-spec") + 1]
    else:
        spec = "Frost"
    if "-spell_priority" in sys.argv:
        spell_priority = sys.argv[sys.argv.index("-spell_priority") + 1].split(',')
    else:
        spell_priority = ['Fire Blast r7','Frostbolt r11','Arcane Explosion r1','Fireball r1']
        
    print("Running sim for " + str(spec) + " mage...")
    print("Running for " + str(g_vars.seconds_to_run) + " seconds...")
    player = Character(spec,spell_priority,g_vars)
    while int(g_vars.num_secs) != g_vars.seconds_to_run:
        player.run_step()
        g_vars.num_secs = g_vars.num_secs + g_vars.time_step_resolution
    print("Your DPS is: " + str(player.damage / g_vars.seconds_to_run))
    print("Your mana efficiency: " + str((player.damage/player.mana_spent)))
