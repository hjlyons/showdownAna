#!/usr/bin/env python3

from src.Pokemon import Pokemon

class Trainer:
    team = {}
    def __init__(self, name, pokes):
        self.name = name
        for x in range(0, len(pokes)):
            self.team[pokes[x]] = Pokemon(pokes[x])

    def attack(self, pokemon, opponent, opp_poke, damage):
        """
        Do we really need our own pokemon here if we are dealing 
        a set amount of damage to the opponent?
        """
        #self.team[pokemon]
        opponent.team[opp_poke].take_damage(damage)

    def check_faints(self): 
        dead = []
        for pokemon in self.team:
            if self.team[pokemon].health == 0: 
                dead.append(pokemon)
                
        for pokemon in dead:
            self.team.pop(pokemon)
            print(pokemon, "died!!!")
