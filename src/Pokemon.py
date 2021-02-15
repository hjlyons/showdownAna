#!/usr/bin/env python3

class Pokemon: 
    def __init__(self, name):
        """
        Initialise each pokemon with a name and base
        health of 100. TODO: add types!
        """
        self.name = name
        self.health = 100

    def take_damage(self, lost): 
        """
        When a pokemon is attacked, subtract that
        much health. If health < 0 then the Pokemon
        has fainted, so set health to zero. Can then
        check if health == 0 in Trainer class.
        """
        self.health = self.health - lost
        if self.health < 0: 
            self.health = 0
    
    def apply_heal(self, healed): 
        """
        A pokemon used a healing move.
        Max health is 100.
        """
        self.health = self.health + healed
        if self.health > 100: 
            self.health = 100
