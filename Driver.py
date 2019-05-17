import subprocess
import json

from common.constants import *

address = "0000000000000000000000000000000000000000"

# EVM Driver
class Driver():
    def __init__(self) -> None:
        pass

    def init(self, substate) -> None:
        self.substate = substate

        with open(PLACEHOLDER_JSON) as json_file:
            self.json_data = json.load(json_file)

        self.json_data["accounts"][address]["code"] = self.substate["code"]
        self.json_data["accounts"][address]["storage"] = self.substate["storage"]

        with open(PLACEHOLDER_JSON, 'w') as dump_file:
            json.dump(self.json_data, dump_file)

    def run(self) -> list:
        args = f"--chain {PLACEHOLDER_JSON} --to {address} --std-json"
        cmd = "./bin/parity-evm " + args
        cmd = cmd.split()
        print(args)
        subprocess.run(*cmd)
        subprocess.run(f"./bin/parity-evm --chain {PLACEHOLDER_JSON} --to {address} --std-json", shell=True)

        trace = list()
        return trace 

