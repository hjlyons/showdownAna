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
            if action[1] == "Player1":
                trainer = self.trainer1
            elif action[1] == "Player2":
                trainer = self.trainer2

            if action[0] == "switch_rename": 
                trainer.change_name(action[2], action[3])
                trainer.set_current(trainer.team[action[3]])
            elif action[0] == "switch": 
                trainer.set_current(trainer.team[action[2]])
            elif action[0] == "change_hp":
                try:
                    trainer.team[action[2]].change_health(action[3])
                except KeyError:
                    print(action[2], "not in team!", action, trainer.team)


        # check if anyone fainted
        self.trainer1.check_faints()
        self.trainer2.check_faints()
