
import json
import random
import sys
from spell_data import create_spell_data
from global_vars import Global_Vars
from stats import create_weapon_stats

#num_secs = 0 # Keeping track of the number of steps
#time_step_resolution = 0.1 # How many seconds each step is
#seconds_to_run = 20 # Time simulator runs in seconds
#GCD = 1.5 # in seconds

class Character:

    
    def __init__(self,spec,sp,g_vars):
        self.g_vars = g_vars
        self.casting = False
        self.gcd = False
        self.dots = []
        self.cast_time = 1000
        self.spell = None
        self.damage = 0.0
        self.gcd_count = 0
        self.crit_chance = 5 # Crit chance in percent
        self.auto_attacking = False
        self.swing_timer = 0.0
        self.swing = False
        self.weapon_stats = create_weapon_stats()
        # Spec spell priority
        self.spell_priority = sp

    def get_spell_damage(self,spellname="spell"):
        '''
        This function returns a spell's damage
        '''
        return random.randint(self.spell_data[spellname][1][0],self.spell_data[spellname][1][1]) 

    def get_weapon_damage(self):
        return random.randint(self.weapon_stats["Damage"][0],self.weapon_stats["Damage"][1])

    def get_spell_mana_cost(self,spellname="spell"):
        '''
        This function returns the spell's mana cost
        '''
        return self.spell_data[spellname][4]

    def get_casting(self):
        return self.casting

    def is_gcd(self):
        return self.gcd
    
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


