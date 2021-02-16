#!/usr/bin/env python3

from src.Pokemon import Pokemon

class Trainer:
    def __init__(self, name, pokes):
        self.team = {}
        self.name = name
        for x in range(0, len(pokes)):
            self.team[pokes[x]] = Pokemon(pokes[x])


    def __repr__(self):
        team = ",".join([x for x in self.team])
        return "Player: %s Team: %s (%i)" % (self.name, team, len(self.team))


    def check_faints(self): 
        """
        At the end of each turn, check if any pokemon 
        have zero health. If they do remove them from 
        the (self.) team.
        """
        dead = []
        for pokemon in self.team:
            if self.team[pokemon].health == 0: 
                dead.append(pokemon)
                
        for pokemon in dead:
            self.team.pop(pokemon)
