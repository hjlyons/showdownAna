#!/usr/bin/env python3

class Pokemon: 
    def __init__(self, name):
        self.name = name
        self.health = 100

    def take_damage(self, lost): 
        self.health = self.health - lost
        if self.health < 0: 
            self.health = 0
