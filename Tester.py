from common.constants import *
from common import opcode_values

import Backtracker
import Driver

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

        self.evm_driver = Driver.Driver()
        self.backtracker = Backtracker.Backtracker()

    def run(self) -> None:
        self.evm_driver.init(self.json_data["substate"])
        trace = self.evm_driver.run()

        self.backtracker = Backtracker.Backtracker(trace)
        new_substate = self.bactracker.run()

        self.evm_driver.init(new_substate)
        new_trace = self.evm_driver.run()

        result = self.compare(trace, new_trace)
        print(f"{result}")

    def compare(self, first_run, second_run) -> bool:
        validity = bool()
        return validity

if __name__ == "__main__":
    tester = Tester(args.input_trace)
    tester.run()

