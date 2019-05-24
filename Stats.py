#from Keypicker import (
#    outfile_path
#)

import Backtracker
import Driver

import json

# Maybe we can produce additional stats later?
class Stats():
    # Produce stats directly from Backtracker instance.
    def __init__(self) -> None:
        #self.outfile_path = outfile_path

        # Stat dictionary
        self.stats = dict() 

    def register(key, value) -> None:
        self.stats[key] = value

    def print_stats(self) -> None:
        #with open(self.outfile_path, 'w') as out_json:
        #    json.dump(self.stats, out_json, indent=4)
        pass

