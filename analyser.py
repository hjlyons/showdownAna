#!/usr/bin/env python3

from src.ShowdownLog import ShowdownLog
from src.Trainer import Trainer
from src.Battle import Battle

def main():
    # read in the intial team lists for players 1 and 2
    dummy_log = ShowdownLog("example_logs/1038904108.txt")
    team1, team2 = dummy_log.get_initialteams()

    # initialise each player with their respective teams
    player1 = Trainer("Player1", team1)
    player2 = Trainer("Player2", team2)

    # initialise the battle
    battle = Battle(player1, player2)

    for i in range(1, dummy_log.nturns+1):
        actions_this_turn = dummy_log.get_turn_actions(i)
        battle.process_turn(actions_this_turn)

    print("", repr(player1), "\n", repr(player2))
   

if __name__ == "__main__":
    main()
