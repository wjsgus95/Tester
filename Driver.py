import subprocess
import json
import re

from common.constants import *

address = "0000000000000000000000000000000000000001"

# EVM Driver
class Driver():
    def __init__(self, stats) -> None:
        self.stats = stats

    def init(self, substate) -> None:
        self.substate = substate

        # Open placeholder JSON file.
        with open(PLACEHOLDER_JSON) as json_file:
            self.json_data = json.load(json_file)

        # Inject input trace into the placeholder.
        self.json_data["accounts"][address]["code"] = self.substate["code"]
        self.json_data["accounts"][address]["storage"] = self.substate["storage"]

        # Write back placeholder.
        with open(PLACEHOLDER_JSON, 'w') as dump_file:
            json.dump(self.json_data, dump_file, indent=4)

    def run(self) -> list:
        # Return trace is a list of dicts.
        trace = list()

        # Run EVM with trace given at initialization.
        bin, args = "./bin/parity-evm ", f"stats --chain {PLACEHOLDER_JSON} --to {address} --json"
        cmd = (bin + args).split()
        evm_log = subprocess.check_output(cmd).decode()

        # Retrieve operations from EVM log.
        ops = re.findall("\"opName\":\"(.*?)\"", evm_log)

        # Retrieve stack logs at each operation's execution.
        stacks =  re.findall("\"stack\":\[(.*?)\]", evm_log)
        stacks = [stack.split(',') for stack in stacks]
        for stack in stacks:
            for i in range(len(stack)):
                if stack[i] != '': stack[i] = eval(stack[i])
                else: stack.pop(i)

        assert len(ops) == len(stacks)
        # Create list of dictionaries from retrieved operation and stack list.
        for i in range(len(ops)):
            trace_elt = dict(zip(["op", "stack"], [ops[i], stacks[i]]))
            trace.append(trace_elt)
        print()
        print(trace)
        return trace 

