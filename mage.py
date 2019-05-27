
import random
import sys
from spell_data import create_spell_data
from character import Character
from global_vars import Global_Vars
import math

class Mage(Character):

    def __init__(self,spec,sp,g_vars):
        super().__init__(spec,sp,g_vars)
        self.info = "Mage"
        self.spell_data = create_spell_data("Mage")
        self.spec = spec
        self.mana = int(math.ceil(self.char_stats["Intellect"] * 15)) + 111
        print("Mana: " + str(self.mana))
        self.crit_chance = self.char_stats["Intellect"] / 59.5  # Spell crit chance
        self.mana_spent = 0
        self.current_spell_cost = 0

    def print_info(self):
        print(self.info)

    def run_step(self):
        """
        Function runs one step of the simulation. This will equate to time_step_resolution second(s) in real time.
        """
        # Choose spell from priority
        if (not self.casting) and (not self.gcd):
            self.spell = self.choose_spell(priority=self.spell_priority)
            self.current_spell_cost = self.get_spell_mana_cost(self.spell)
            if self.current_spell_cost > self.mana:
                self.spell = None
            if self.spell == None:  # Might be oom if no spell
                self.auto_attacking = True
            else:
                self.set_cooldown(self.spell,True) 
                # Cast spell
                self.cast_time = self.get_cast_time(self.spell)
                self.casting = True
                self.gcd = True

        # Sim cast time
        if self.casting:
            self.cast_time = self.cast_time - self.g_vars.time_step_resolution
            if float(self.cast_time) < 0.09:
                self.casting = False
                self.mana -= self.current_spell_cost

        # Sim auto attack timer
        if self.auto_attacking:
            self.swing_timer += self.g_vars.time_step_resolution
            if float(self.swing_timer) >= self.weapon_stats["Attack Speed"]:
                self.auto_attacking = False
                self.swing = True


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

        # Apply Auto Attack Damage
        if self.swing:
            wep_temp = self.get_weapon_damage()
            print("OUT OF MANA: " + str(self.mana))
            print("Auto Attacked for " + str(wep_temp) + " damage! - at time %.2f second(s)" % self.g_vars.num_secs)
            self.damage += wep_temp
            self.swing = False
            self.swing_timer = 0

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



