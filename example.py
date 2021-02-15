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
    player1.attack("Corsola-Galar", player2, "Dragapult", 120)
    player1.check_faints()


if __name__ == "__main__":
    main()
