#!/usr/bin/env python3

from src.Trainer import Trainer
from src.ShowdownLog import ShowdownLog

def main():
    team1 = [] 
    team2 = []
    dummy_log = ShowdownLog("example_logs/1038904108.txt")
    team1, team2 = dummy_log.get_initialteams()

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
