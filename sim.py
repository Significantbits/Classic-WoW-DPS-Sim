# Classic WoW Class simulation
# Want to take in talent tree and run DPS sim.

import json
import random
import sys
from spell_data import create_spell_data

num_secs = 0 # Keeping track of the number of steps
time_step_resolution = 0.1 # How many seconds each step is
seconds_to_run = 20 # Time simulator runs in seconds
GCD = 1.5 # in seconds

class Character:
    
    def __init__(self,spec,sp):
        self.spec = spec
        self.casting = False
        self.gcd = False
        self.dots = []
        self.cast_time = 1000
        self.spell = None
        self.damage = 0.0
        self.gcd_count = 0
        self.crit_chance = 5 # Crit chance in percent
        self.spell_data = create_spell_data()
        # Spec spell priority
        self.spell_priority = sp

    def get_spell_damage(self,spellname="spell"):
        '''
        This function returns a spell's damage
        '''
        return random.randint(self.spell_data[spellname][1][0],self.spell_data[spellname][1][1]) 
    
    def is_on_cooldown(self,spell):
        return self.spell_data[spell][6]

    def set_cooldown(self,spell,state):
        self.spell_data[spell][6] = state 
        if state == True:
            self.spell_data[spell][7] = self.spell_data[spell][5]

    def choose_spell(self,priority=None):
        '''
        This function will return a spell given a priority list
        '''
        chosen_spell = None

        for spell in self.spell_priority:
            if not self.is_on_cooldown(spell):
                chosen_spell = spell
                break
            
        return chosen_spell 


    def get_cast_time(self,spellname="spell"):
        '''
        This function returns the cast time of a spell
        '''
        return self.spell_data[spellname][0]

    def is_crit(self):
        return random.randint(0,100) < self.crit_chance

    def apply_dot(self,dmg_per_tsr):
        self.dots.append(dmg_per_tsr)

    def has_spell_effect(self,spell):
        return spell_effect_dict[spell][0]

    def is_dot(self,spell):
        return (spell_data[spell][2] != 0)


    def run_step(self):
        """
        Function runs one step of the simulation. This will equate to time_step_resolution second(s) in real time.
        """
        # Choose spell from priority
        if (not self.casting) and (not self.gcd):
            self.spell = self.choose_spell(priority=self.spell_priority)
            if self.spell == None:  # Assert on not choosing a spell
                print("DIDN'T CHOOSE A SPELL!")
                exit(0)
            self.set_cooldown(self.spell,True) 
            # Cast spell or Auto attack
            self.cast_time = self.get_cast_time(self.spell)
            self.casting = True
            self.gcd = True

        # Sim cast time
        if self.casting:
            self.cast_time = self.cast_time - time_step_resolution
            if float(self.cast_time) < 0.09:
                self.casting = False

        #Update Cooldowns
        for spell in self.spell_data:
            if self.is_on_cooldown(spell):
                self.spell_data[spell][7] -= time_step_resolution
                if self.spell_data[spell][7] < 0.09:
                    self.spell_data[spell][6] = False  # Spell is now off cooldown

        # Update Global cooldown
        if self.gcd:
            self.gcd_count += time_step_resolution
            if self.gcd_count >= GCD:
                self.gcd_count = 0
                self.gcd = False


        # Check for crit and Add damage and spell effects
        if (not self.casting) and (self.spell != None):
            spell_damage = self.get_spell_damage(self.spell)
            if self.is_crit():
                spell_damage = spell_damage * 2
                print("Casted " + self.spell + " for " + str(spell_damage) + " CRIT damage! - at time %.2f second(s)" % num_secs)
            else:
                print("Casted " + self.spell + " for " + str(spell_damage) + " damage! - at time %.2f second(s)" % num_secs)
            self.damage = self.damage + spell_damage
            self.spell = None

    

if __name__ == "__main__":
    print("Starting WoW Classic DPS Simulator Version 0.01...")
    
    if "-spec" in sys.argv:
        spec = sys.argv[sys.argv.index("-spec") + 1]
    else:
        spec = "Frost"
    if "-spell_priority" in sys.argv:
        spell_priority = sys.argv[sys.argv.index("-spell_priority") + 1].split(',')
    else:
        spell_priority = ['Fire Blast r7','Frostbolt r11','Arcane Explosion r1','Fireball r1']
        
    print("Running sim for " + str(spec) + " mage...")
    print("Running for " + str(seconds_to_run) + " seconds...")
    player = Character(spec,spell_priority)
    while int(num_secs) != seconds_to_run:
        player.run_step()
        num_secs = num_secs + time_step_resolution
    print("Your DPS is: " + str(player.damage / seconds_to_run))
