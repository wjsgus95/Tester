
from common.opcode_values import *
from common.constants import *

import Stats


class Backtracker():
	def __init__(self, json_data) -> None:
		self.trace = json_data["trace"]

		self.storage = dict()
		self.storage_write_track = dict()
		self.storage_read_track = dict()
		self.stats = Stats.Stats(self)



	# Replay the whole trace.
	def run(self) -> None:
		# TODO: track which and when keys are modified
		idx = 0
		for trace in self.trace:
			op = trace["op"]
			stack = [int(elt ,16) for elt in trace["stack"]]
			self.storage_write_track[idx] = dict()
			self.storage_read_track[idx] = []

			if op == "SSTORE":
				key = stack.pop()
				value = stack.pop()

				if key in self.storage:
					self.storage_write_track[idx][key] = (self.storage[key], value)
				else:
					self.storage_write_track[idx][key] = ('empty', value)

				self.storage[key] = value


			elif op == "SLOAD":
				key = stack.pop()
				if key in self.storage:
					#stack.append(self.storage[key])
					self.storage_read_track[idx].append(key)

				else:
					print("SLOAD Error: stack poped key doesn't exist in the storage")


			else:
				pass


                    idx += 1
                return self.storage_write_track, self.storage_read_track

	# Print stats after exeuction.
# self.stats.print_stats()
# print(self.storage_track)

