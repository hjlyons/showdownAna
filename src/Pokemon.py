#!/usr/bin/env python3

class Pokemon: 
    def __init__(self, name):
        """
        Initialise each pokemon with a name and base
        health of 100. TODO: add types!
        """
        self.name = name
        self.health = 100

    def change_health(self, new_health): 
        """
        Change the health of a pokemon
        to whatever it was at the end of the turn.
        This applies to both heals and damage.
        """
        self.health = new_health

    def change_name(self, old_name, new_name): 
        """
        Some people are weird and rename their pokemon.
        The name is only updated when they are switched in
        so we need to change the name in our team.
        """
        self.team[new_name] = self.team[old_name]
        self.team.pop(old_name)
