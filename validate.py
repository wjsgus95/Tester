import subprocess
import json

from common.constants import *

for i in range(1000):
    cmd = "python3 -m evmcodegen".split()
    code = subprocess.check_output(cmd).decode().lstrip("0x")

    trace = dict()
    trace["substate"] = dict()

    trace["substate"]["code"] = code
    trace["substate"]["storage"] = dict()

    with open(f"traces/trace{str(i).zfill(3)}.json", 'w') as dump_file:
        json.dump(trace, dump_file, indent=4)

    cmd = f"python3 Keypicker.py traces/trace{str(i).zfill(3)}.json".split()
    result = subprocess.check_output(cmd).decode()

    print(f"trace number: {i}")
    print(result)
    print()

