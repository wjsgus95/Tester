from common.constants import *
from common import opcode_values

import Backtracker
import Driver
import Stats

import json
import math
import sys
import argparse


# Argparse initialized.
parser = argparse.ArgumentParser(description = \
        "Tester, transaction replay from EVM execution trace")
# Input file path positional(required) argument.
parser.add_argument('input_trace', type=str, help='Input JSON trace file')
# Output file path optional.
parser.add_argument('--dest', type=str, help=f'Output stats file path, defaults to {DEFAULT_OUT_PATH}',
                    nargs=1, default=DEFAULT_OUT_PATH)
args = parser.parse_args()

# Will override output file path if any given.
outfile_path = args.dest if type(args.dest) == str else args.dest[0]


class Tester():
    # Initialize with given json file path.
    def __init__(self, json_path) -> None:
        with open(json_path) as json_file:
            self.json_data = json.load(json_file)

        self.stats = Stats.Stats()
        self.backtracker = Backtracker.Backtracker(self.stats)
        self.evm_driver = Driver.Driver(self.stats)

    def run(self) -> None:
        # Run EVM with given substate and retrieve trace.
        self.evm_driver.init(self.json_data["substate"])
        trace = self.evm_driver.run()

        # Backtrack starting state from given trace.
        self.backtracker.init(trace)
        new_substate = self.backtracker.run()

        # Run EVM again with generated substate.
        self.evm_driver.init(new_substate)
        new_trace = self.evm_driver.run()

        # Validate the result.
        result = self.compare(trace, new_trace)
        print(f"{result}")

        # Print stats to output file.
        self.stats.print_stats()

    # Check if second run result is a subset of first run result.
    def compare(self, first_state, second_state) -> bool:
        validity = bool()
        # TODO: do validation
        return validity

if __name__ == "__main__":
    tester = Tester(args.input_trace)
    tester.run()

