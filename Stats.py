from Tester import (
    outfile_path
)

import Backtracker
import json

# Maybe we can produce additional stats later?
class Stats():
    # Produce stats directly from Backtracker instance.
    def __init__(self, backtracker) -> None:
        self.outfile_path = outfile_path
        self.backtracker = backtracker

    def print_stats(self) -> None:

        with open(self.outfile_path, 'w') as out_json:
            json.dump(data, out_json, indent=4)

