#!/usr/bin/env python3

class ShowdownLog:
    def __init__(self, infile):
        
        with open(infile) as f:
            raw_lines = f.readlines()
        raw_lines = [line.rstrip() for line in raw_lines]
        
        # To avoid usernames overlapping with string comparisons, set them to default $PLAYER1$ and $PLAYER2$
        username_list = [line.split("☆")[-1] for line in raw_lines if "|j|☆" in line]
        assert len(username_list) == 2        
        raw_lines = [l.replace(username_list[0], "$PLAYER1$") for l in raw_lines]
        raw_lines = [l.replace(username_list[1], "$PLAYER2$") for l in raw_lines]
        self.log_lines = raw_lines

        # Useful line_index within the logfile
        self.start_index = [i for i, line in enumerate(self.log_lines) if "|start" in line][0]
        self.win_index = [i for i, line in enumerate(self.log_lines) if "|win|" in line][0]
        self.turn_indexlist = [i for i, line in enumerate(self.log_lines) if "|turn|" in line]
        assert len(self.turn_indexlist) > 0

        # Print of collected information
        print("Start Index: {}".format(self.start_index))
        print(self.log_lines[(self.start_index)])
        print("Turn Index List: {}".format(self.turn_indexlist))
        for t in self.turn_indexlist:
            print(self.log_lines[t])
        print("Win Index: {}".format(self.win_index))
        print(self.log_lines[(self.win_index)])


