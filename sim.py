# Classic WoW Class simulation
# Want to take in talent tree and run DPS sim.

import json
import random
import sys

num_secs = 0 # Keeping track of the number of steps
time_step_resolution = 0.1 # How many seconds each step is
seconds_to_run = 20 # Time simulator runs in seconds
GCD = 1.5 # in seconds

class Character:
    
    def __init__(self,spec):
        self.spec = spec
        self.casting = False
        self.gcd = False
        self.cast_time = 1000
        self.spell = None
        self.damage = 0.0
        self.gcd_count = 0

        # Spec spell priority
        if self.spec == "Frost":
            self.spell_priority = ['Fire Blast','Frostbolt','Arcane Explosion','Fireball']
        if self.spec == "Fire":
            self.spell_priority = ['Fire Blast','Fireball','Arcane Explosion','Frostbolt']

        # Spell Damage
        self.spell_damage_dict = dict([('Frostbolt', [53,60]),('Fire Blast',[60,74]),('Arcane Explosion',[33,38]),('Fireball',[57,77])])
        if self.spec == "Frost":
            self.spell_casttime_dict = dict([('Frostbolt',1.7),('Fire Blast',0),('Arcane Explosion',0),('Fireball',2.5)])
        if self.spec == "Fire":
            self.spell_casttime_dict = dict([('Frostbolt',2.2),('Fire Blast',0),('Arcane Explosion',0),('Fireball',2.0)])

        # Spell Cooldown
        self.spell_cooldown_dict = dict([('Frostbolt',[False,0]),('Fire Blast',[False,0]),('Arcane Explosion',[False,0]),('Fireball',[False,0])])

        # Spec spell cooldown
        if self.spec == "Frost":
            self.spell_cooldown_time_dict = dict([('Frostbolt',0),('Fire Blast',8),('Arcane Explosion',0),('Fireball',0)])
        if self.spec == "Fire":
            self.spell_cooldown_time_dict = dict([('Frostbolt',0),('Fire Blast',6.5),('Arcane Explosion',0),('Fireball',0)])


    def get_spell_damage(self,spellname="spell"):
        '''
        This function returns a spell's damage
        '''
        return random.randint(self.spell_damage_dict[spellname][0],self.spell_damage_dict[spellname][1]) 
    
    def is_on_cooldown(self,spell):
        return self.spell_cooldown_dict[spell][0]

    def set_cooldown(self,spell,state):
        self.spell_cooldown_dict[spell][0] = state 
        if state == True:
            self.spell_cooldown_dict[spell][1] = self.spell_cooldown_time_dict[spell]

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
        return self.spell_casttime_dict[spellname]

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
        for spell in self.spell_cooldown_dict:
            if self.is_on_cooldown(spell):
                self.spell_cooldown_dict[spell][1] -= time_step_resolution
                if self.spell_cooldown_dict[spell][1] < 0.09:
                    self.spell_cooldown_dict[spell][0] = False  # Spell is now off cooldown

        # Update Global cooldown
        if self.gcd:
            self.gcd_count += time_step_resolution
            if self.gcd_count >= GCD:
                self.gcd = False


        # Add damage
        if (not self.casting) and (self.spell != None):
            spell_damage = self.get_spell_damage(self.spell)
            print("Casted " + self.spell + " for " + str(spell_damage) + " damage! - at time %.2f second(s)" % num_secs)
            self.damage = self.damage + spell_damage
            self.spell = None

    

if __name__ == "__main__":
    print("Starting WoW Classic DPS Simulator Version 0.01...")
    
    if "-spec" in sys.argv:
        spec = sys.argv[sys.argv.index("-spec") + 1]
    print("Running sim for " + str(spec) + " mage...")
    print("Running for " + str(seconds_to_run) + " seconds...")
    player = Character(spec)
    while int(num_secs) != seconds_to_run:
        player.run_step()
        num_secs = num_secs + time_step_resolution
    print("Your DPS is: " + str(player.damage / seconds_to_run))
