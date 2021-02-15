#!/usr/bin/env python3

class Battle: 
    def __init__(self, trainer1, trainer2): 
        self.trainer1 = trainer1
        self.trainer2 = trainer2


    def process_turn(self, action1, action2):
        """
        Process the actions taken this turn. The actions are 
        passed as 2 lists, the faster pokemon is first and 
        the slower second. So far the only options are damage 
        heal. Need to add status and switch.
        """
        action1[0].team[action1[1]].change_health(action1[2])
        action2[0].team[action2[1]].change_health(action2[2])

        # check if anyone fainted
        self.trainer1.check_faints()
        self.trainer2.check_faints()
