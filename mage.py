
import json
import random
import sys
from spell_data import create_spell_data
from character import Character
from global_vars import Global_Vars

class Mage(Character):

    def __init__(self,spec,sp,g_vars):
        super().__init__(spec,sp,g_vars)
        self.info = "This is for the mage class"
        self.spell_data = create_spell_data("Mage")
        self.spec = spec
        self.mana_spent = 0

    def print_info(self):
        print(self.info)

    def run_step(self):
        """
        Function runs one step of the simulation. This will equate to time_step_resolution second(s) in real time.
        """
        # Choose spell from priority
        #if (not self.casting) and (not self.gcd):
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
            self.cast_time = self.cast_time - self.g_vars.time_step_resolution
            if float(self.cast_time) < 0.09:
                self.casting = False

        #Update Cooldowns
        for spell in self.spell_data:
            if self.is_on_cooldown(spell):
                self.spell_data[spell][7] -= self.g_vars.time_step_resolution
                if self.spell_data[spell][7] < 0.09:
                    self.spell_data[spell][6] = False  # Spell is now off cooldown

        # Update Global cooldown
        if self.gcd:
            self.gcd_count += self.g_vars.time_step_resolution
            if self.gcd_count >= self.g_vars.GCD:
                self.gcd_count = 0
                self.gcd = False


        # Check for crit and Add damage and spell effects
        if (not self.casting) and (self.spell != None):
            spell_damage = self.get_spell_damage(self.spell)
            if self.is_crit():
                spell_damage = spell_damage * 1.5
                print("Casted " + self.spell + " for " + str(spell_damage) + " CRIT damage! - at time %.2f second(s)" % self.g_vars.num_secs)
            else:
                print("Casted " + self.spell + " for " + str(spell_damage) + " damage! - at time %.2f second(s)" % self.g_vars.num_secs)
            self.damage = self.damage + spell_damage
            self.mana_spent += self.get_spell_mana_cost(self.spell)
            self.spell = None

