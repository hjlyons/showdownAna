#!/usr/bin/env python3

from src.LogParse import ShowdownLog
import glob

def main():
    test_files = glob.glob("example_logs/*.txt")[:10]
    for logfile in test_files:
        print("\nParsing Logfile: {}".format(logfile))
        dumy_log = ShowdownLog(logfile)
    
if __name__ == "__main__":
    main()
