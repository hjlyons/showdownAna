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

    turnlines = []
    turnlines.append([[player2, "Dragapult", 50], [player2, "Dragapult", 100]])
    for line in turnlines: 
        battle.process_turn(line[0], line[1])

    print("", repr(player1), "\n", repr(player2))
   

if __name__ == "__main__":
    main()
