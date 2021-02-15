#!/usr/bin/env python3

from src.Pokemon import Pokemon

class Trainer:
    team = {}
    def __init__(self, name, *pokes):
        self.name = name
        pokes = list(*pokes)
        for x in range(0, len(pokes)):
            self.team[pokes[x]] = Pokemon(pokes[x])

    def attack(self, pokemon, opponent, opp_poke):
        print(self.team[pokemon].name, "attacked", opponent.name, opponent.team[opp_poke].name)
