from common.constants import *
from common import opcode_values

import Backtracker
import Driver
import Stats

import json
import sys
import argparse


# Argparse initialized.
parser = argparse.ArgumentParser(description = \
        "Keypicker, transaction replay from EVM execution trace")
# Input file path positional(required) argument.
parser.add_argument('input_trace', type=str, help='Input JSON trace file')
# Output file path optional.
parser.add_argument('--dest', type=str, help=f"Output stats file path, defaults to {DEFAULT_OUT_PATH}",
                    nargs=1, default=DEFAULT_OUT_PATH)
args = parser.parse_args()

# Will override output file path if any given.
outfile_path = args.dest if type(args.dest) == str else args.dest[0]


class Keypicker():
    # Initialize with given json file path.
    def __init__(self, json_path) -> None:
        with open(json_path) as json_file:
            self.json_data = json.load(json_file)

        self.stats = Stats.Stats()
        self.backtracker = Backtracker.Backtracker(self.stats)
        self.evm_driver = Driver.Driver(self.stats)

    def run(self) -> None:
        # Run EVM with given substate and retrieve trace.
        substate = self.json_data["substate"]
        self.evm_driver.init(substate)
        trace = self.evm_driver.run()
        print(trace)

        # Backtrack starting state from given trace.
        self.backtracker.init(trace, substate["code"])
        new_substate = self.backtracker.run()

        # Run EVM again with generated substate.
        self.evm_driver.init(new_substate)
        new_trace = self.evm_driver.run()
        print();print(new_trace)

        # Validate the result.
        result = self.compare(trace, new_trace)
        print(f"{result}")

        # Print stats to output file.
        self.stats.print_stats()

    def compare(self, trace, new_trace) -> bool:
        validity = True

        for m_trace, m_new_trace in zip(trace, new_trace):
            op, new_op = m_trace["op"], m_new_trace["op"]
            stack, new_stack = [int(elt,16) for elt in m_trace["stack"]], [int(elt,16) for elt in m_new_trace["stack"]]
            # Reverse the stacks.
            stack, new_stack = stack[::-1], new_stack[::-1]

            validity = (op == new_op) and validity
            #validate if top len(new_stack) elements are positioned the same. Just like Tower of Hanoi.
            for i in range(len(new_stack)):
                validity = (stack[i] == new_stack[i]) and validity
            
        return validity

if __name__ == "__main__":
    keypicker = Keypicker(args.input_trace)
    keypicker.run()

