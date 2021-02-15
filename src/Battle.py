#!/usr/bin/env python3

class Battle: 
    def __init__(self, trainer1, trainer2): 
        self.trainer1 = trainer1
        self.trainer2 = trainer2
    
    def process_turn(self, action1, action2):
        if action1[0] == "damage": 
            self.damage(action1[1], action1[2], action1[3])
        elif action1[0] == "heal": 
            self.heal(action1[1], action1[2], action1[3])
        
        if action2[0] == "damage": 
            self.damage(action2[1], action2[2], action2[3])
        elif action2[0] == "heal": 
            self.heal(action2[1], action2[2], action2[3])

    def damage(self, trainer, pokemon, damage):
        trainer.team[pokemon].take_damage(damage)
    
    def heal(self, trainer, pokemon, health):
        trainer.team[pokemon].apply_heal(health)

    def end_turn(self): 
        """
        Check if anyone fainted.
        """
        self.trainer1.check_faints()
        self.trainer2.check_faints()
