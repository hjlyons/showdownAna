#!/usr/bin/env python3

from src.Trainer import Trainer

def main():
    michael = Trainer("Michael", ["Bulba", "Squirt", "Char"])
    harry   = Trainer("Harry", ["Pika", "Jiggly", "Mankey"])

    # move 1
    michael.attack("Bulba", harry, "Pika")

if __name__ == "__main__":
    main()
