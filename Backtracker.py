from common.opcode_values import *
from common.constants import *

import Stats

class Backtracker():
    def __init__(self, json_data) -> None:
        self.trace = json_data["trace"]

        self.storage_track = set()

        self.stats = Stats.Stats(self)

    # Replay the whole trace.
    def run(self) -> None:
        #TODO: track which and when keys are modified
        for trace in self.trace:
            op = trace["op"]
            stack = [int(elt,16) for elt in trace["stack"]]

            if op == "SSTORE":
                self.storage_track.add(stack.pop())
            elif op == "SLOAD":
                self.storage_track.add(stack.pop())
            else:
                pass

        # Print stats after exeuction.
        #self.stats.print_stats()
        print(self.storage_track)

