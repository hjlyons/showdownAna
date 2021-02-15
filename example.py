#!/usr/bin/env python3

from src.Trainer import Trainer

def main():
    michael = Trainer("Michael", ["Bulba", "Squirt", "Char"])
    harry   = Trainer("Harry", ["Pika", "Jiggly", "Mankey"])

    # move 1
    michael.attack("Bulba", harry, "Pika")
    
    # test fainting feature
    print("~"*5, "Team before turn")
    for pokemon in michael.team:
        print(pokemon)

    michael.team["Bulba"].take_damage(120)
    michael.check_faints()

    print("~"*5, "Team after turn")
    for pokemon in michael.team:
        print(pokemon)


if __name__ == "__main__":
    main()
