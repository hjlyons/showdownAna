#!/usr/bin/env python3

from src.Trainer import Trainer
from src.ShowdownLog import ShowdownLog

def main():
    # read in the intial team lists for players 1 and 2
    dummy_log = ShowdownLog("example_logs/1038904108.txt")
    team1, team2 = dummy_log.get_initialteams()

    # initialise each player with their respective teams
    player1 = Trainer("Player1", team1)
    player2 = Trainer("Player2", team2)
   
    # fake turn 1
    player2.team["Dragapult"].take_damage(120)
    
    # check if any poke's died
    player1.check_faints()
    player2.check_faints()

    print(repr(player1), "\n", repr(player2))
    

if __name__ == "__main__":
    main()
