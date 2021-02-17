#!/usr/bin/env python3

PLAYER_CONDITIONS =  ["StealthRocks", "Spikes", "ToxicSpikes", "StickyWeb"]

class Field: 
    def __init__(self): 
        self.field_conditions = {}

        for c in PLAYER_CONDITIONS:
            self.field_conditions["Player1_{}".format(c)] = 0
            self.field_conditions["Player2_{}".format(c)] = 0
        
        self.field_conditions["Weather"] = "None"
        self.field_conditions["Terrain"] = "None"
        self.field_conditions["TrickRoom"] = False
        self.field_conditions["Gravity"] = False

    def __repr__(self):

        conditions_summary = "    FieldSummary    \n"
        conditions_summary += "--------------------\n"
        for c in PLAYER_CONDITIONS:
            conditions_summary+= "{}: Player1 {}, Player2 {}\n".format(c,self.field_conditions["Player1_{}".format(c)], self.field_conditions["Player2_{}".format(c)] )
        conditions_summary += "--------------------\n"
        conditions_summary += "Weather: {}\n".format(self.field_conditions["Weather"])
        conditions_summary += "Terrain: {}\n".format(self.field_conditions["Terrain"])
        conditions_summary += "TrickRoom: {}\n".format(self.field_conditions["TrickRoom"])
        conditions_summary += "Gravity: {}\n".format(self.field_conditions["Gravity"])
        conditions_summary += "===================="

        return conditions_summary

if __name__ == '__main__':
    test_field = Field()
    print(test_field)


