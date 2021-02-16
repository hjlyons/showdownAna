#!/usr/bin/env python3

from src.ShowdownLog import ShowdownLog
from src.Trainer import Trainer
from src.Battle import Battle
import glob

def main():
    test_files = glob.glob("example_logs/*.txt")[:15]
    for logfile in test_files:
        dummy_log = ShowdownLog(logfile)

        # read in the intial team lists for players 1 and 2
        team1, team2 = dummy_log.get_initialteams()

        # initialise each player with their respective teams
        player1 = Trainer("Player1", team1)
        player2 = Trainer("Player2", team2)

        # change which pokemon each player starts with
        p1_first, p2_first = dummy_log.get_initialpokemon()
        player1.set_current(player1.team[p1_first])
        player2.set_current(player2.team[p2_first])

        # initialise the battle
        battle = Battle(player1, player2)

        #loop over all turns and process them
        for i in range(1, dummy_log.nturns+1):
            actions_this_turn = dummy_log.get_turn_actions(i)
            battle.process_turn(actions_this_turn)

        print(logfile)
        print("", repr(player1), "\n", repr(player2))
   

if __name__ == "__main__":
    main()
