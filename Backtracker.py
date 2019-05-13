from common.opcode_values import *
from common.constants import *

import Stats

import math

class Backtracker():
    def __init__(self, json_data) -> None:
        self.trace = json_data["trace"]
        self.ops = [trace[0] for trace in self.trace]
        self.stacks = [trace[1] for trace in self.trace]

        self.stats = Stats.Stats(self)

    # Replay the whole trace.
    def run(self) -> None:
        for op, stack in self.trace:
            pass

        # Print stats after exeuction.
        self.stats.print_stats()

    
