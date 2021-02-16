#!/usr/bin/env python3

from src.Pokemon import Pokemon

class Trainer:
    def __init__(self, name, pokes):
        self.team = {}
        self.name = name
        
        if len(pokes) != 6: 
            raise AttributeError("There were", len(pokes), "on the team, not 6!!")

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
        dead = [poke for poke in self.team if self.team[poke].health == 0]       
        for pokemon in dead:
            self.team.pop(pokemon)
