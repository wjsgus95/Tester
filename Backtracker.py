from common.opcode_values import *
from common.constants import *

import Stats

import math

class Backtracker():
    def __init__(self, json_data) -> None:
        self.trace = json_data["trace"]

        self.storage_track = list()

        self.stats = Stats.Stats(self)

    # Replay the whole trace.
    def run(self) -> None:
        for trace in self.trace:
            op = trace["op"]
            stack = trace["stack"]

            if op == "SSTORE":
                self.storage_track.append(stack.pop())
            elif op == "SLOAD":
                self.storage_track.append(stack.pop())
            else:
                pass

        # Print stats after exeuction.
        #self.stats.print_stats()
        print(self.storage_track)

    
