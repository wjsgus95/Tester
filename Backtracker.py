from common.opcode_values import *
from common.constants import *

import Stats

class Backtracker():
    def __init__(self, stats) -> None:
        self.stats = stats

    def init(self, trace) -> None:
        self.trace = trace
        self.storage_track = list()

    # Replay the whole trace.
    def run(self) -> dict:
        substate = dict()
        #TODO: track which and when keys are modified
        idx = 0
        for trace in self.trace:
            op = trace["op"]
            stack = [int(elt,16) for elt in trace["stack"]]

            if op == "SSTORE":
                self.storage_track.append((stack.pop(), idx))
            elif op == "SLOAD":
                self.storage_track.append((stack.pop(), idx))
            else:
                pass
            idx += 1

        # Print stats after exeuction.
        #self.stats.print_stats()
        print(self.storage_track)
        return substate

