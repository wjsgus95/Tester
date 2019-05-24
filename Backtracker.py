from common.opcode_values import *
from common.constants import *

import Stats

class Backtracker():
    def __init__(self, stats) -> None:
        self.stats = stats

    # Initialize trace and bytecode.
    def init(self, trace, code) -> None:
        self.trace = trace
        self.code = code

    # Replay the whole trace.
    def run(self) -> dict:
        substate = dict()
        substate["code"] = self.code
        substate["stack"] = []
        substate["storage"] = dict()

        for i, trace in enumerate(self.trace):
            op = trace["op"]
            stack = [int(elt,16) for elt in trace["stack"]]

            if op == "SSTORE":
                key = stack.pop()
                value = stack.pop()
                # Can directly tell key-value pair with SSTORE.
                substate["storage"][key] = value
            elif op == "SLOAD":
                key = stack.pop()
                # Top of the stack at next operation is the value that was in the storage.
                substate["storage"][key] = int(self.trace[i+1]["stack"][-1], 16)
            else:
                pass

        return substate

