#!/usr/bin/env python3

class Battle: 
    def __init__(self, trainer1, trainer2): 
        self.trainer1 = trainer1
        self.trainer2 = trainer2


    def process_turn(self, actions):
        """
        Process the actions taken this turn. The actions are 
        passed as 2 lists, the faster pokemon is first and 
        the slower second. So far the only options are damage 
        heal. Need to add status and switch.
        """
        for action in actions:
            if action[0] == "Player1":
                key = [poke for poke in self.trainer1.team if action[1] in poke][0]
                self.trainer1.team[key].change_health(action[2])
            elif action[0] == "Player2":
                key = [poke for poke in self.trainer2.team if action[1] in poke][0]
                self.trainer2.team[key].change_health(action[2])


        # check if anyone fainted
        self.trainer1.check_faints()
        self.trainer2.check_faints()