#!/usr/bin/env python3
"""
TODO: If Increased performance needed, may convert string checks into regex
"""

class ShowdownLog:
    def __init__(self, infile):
        
        with open(infile) as f:
            raw_lines = f.readlines()
        raw_lines = [line.rstrip() for line in raw_lines]
        
        # To avoid usernames overlapping with string comparisons, set them to default $PLAYER1$ and $PLAYER2$
        username1 = [line.split("|player|p1|")[-1].split("|")[0] for line in raw_lines if "|player|p1|" in line][0]
        username2 = [line.split("|player|p2|")[-1].split("|")[0] for line in raw_lines if "|player|p2|" in line][0]
        assert (username1 and username2)
        raw_lines = [l.replace(username1, "$PLAYER1$") for l in raw_lines]
        raw_lines = [l.replace(username2, "$PLAYER2$") for l in raw_lines]
        self.log_lines = raw_lines

        # Defining useful line_index within the logfile
        self.start_index = [i for i, line in enumerate(self.log_lines) if "|start" in line][0]
        self.win_index = [i for i, line in enumerate(self.log_lines) if "|win|" in line][0]
        self.turn_indexlist = [i for i, line in enumerate(self.log_lines) if "|turn|" in line]
        assert len(self.turn_indexlist) > 0

        self.teampreview_indexlist = [i for i, line in enumerate(self.log_lines) if "|poke|p" in line]

    def print_indexvals(self):
        """ 
        Print of collected information 
        """
        print("TeamPreview Index List: {}".format(self.teampreview_indexlist))
        print("Start Index: {}".format(self.start_index))
        print("Turn Index List: {}".format(self.turn_indexlist))
        print("Win Index: {}".format(self.win_index))


    def get_initialteams(self):
        """ 
        Returns list of pokemon, Player1, Player2 
        Requires splitting 
        Logfile Line: 
            |poke|p1|Excadrill, M|
            |poke|p2|Ditto|
        """

        poke_lines = [self.log_lines[i] for i in self.teampreview_indexlist]
        team_player1 = [p.split("|p1|")[-1].split("|")[0].split(",")[0] for p in poke_lines if "p1" in p]
        team_player2 = [p.split("|p2|")[-1].split("|")[0].split(",")[0] for p in poke_lines if "p2" in p]
        
        return team_player1, team_player2


    def get_initialpokemon(self):
        """ 
        Returns Starting Pokemon for Player1 and Player2 
        |start
        |switch|p1a: Ferrothorn|Ferrothorn, M|100/100
        |switch|p2a: Shuckle|Shuckle, M|100/100
        |turn|1
        Should be the 2 lines between start_index and turn_indexlist[0]
        """

        poke_lines = [self.log_lines[i] for i in range(self.start_index, self.turn_indexlist[0]+1)]

        pokemon_player1 = [p.split("|")[3].split("|")[0].split(",")[0] for p in poke_lines if "|switch|p1a" in p][0]
        pokemon_player2 = [p.split("|")[3].split("|")[0].split(",")[0] for p in poke_lines if "|switch|p2a" in p][0]

        return pokemon_player1, pokemon_player2


    def get_turnlogs(self,turn_number=1):
        """ 
        Returns Starting Pokemon for Player1 and Player2 
        |start
        |switch|p1a: Ferrothorn|Ferrothorn, M|100/100
        |switch|p2a: Shuckle|Shuckle, M|100/100
        |turn|1
        Should be the 2 lines between start_index and turn_indexlist[0]
        """

        turn_lines = [self.log_lines[i] for i in range(self.turn_indexlist[turn_number-1], self.turn_indexlist[turn_number])]
        print(turn_number)
        for t in turn_lines:
            print(t)


        return pokemon_player1, pokemon_player2
