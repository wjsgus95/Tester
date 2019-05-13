from opcode_values import *
from constants import *

import Stats

import math

class Engine():
    def __init__(self, json_data) -> None:
        self.bytecode=str(json_data["bytecode"])
        self.stack_data=json_data["stack"]
        self.memory_data=json_data["memory"]
        self.storage_data=json_data["storage"]
        self.bytecode = json_data["bytecode"]

        self.stack = list()
        self.memory = dict()
        self.storage = dict()

        #self.op_address = dict()
        self.pc = 0

        #self.op_dict = dict()

        self.stats = Stats.Stats(self)

    # Configure operation dictionary.
    def configure_op_dict(self) -> None:

        """
        # Clear operation queue.
        self.op_dict[STOP] = lambda operand: self.op_queue.clear()

        # Confiure arithmetic operations.
        self.op_dict[ADD] = lambda operand: stack[0]=(stack[0]+stack[1])%UINT_256_CEILING
        self.op_dict[MUL] = lambda operand: stack[0]=(stack[0]*stack[1])%UINT_256_CEILING
        self.op_dict[SUB] = lambda operand: stack[0]=(stack[0]-stack[1])%UINT_256_CEILING
        self.op_dict[DIV] = lambda operand: stack[0] = 0 if stack[1] == 0 else stack[0]=(math.floor(stack[0]/stack[1]))%UINT_256_CEILING)
        self.op_dict[SDIV] = lambda operand: 
        self.op_dict[MOD] = lambda operand: 
        self.op_dict[SMOD] = lambda operand: 
        self.op_dict[ADDMOD] = lambda operand: 
        self.op_dict[MULMOD] = lambda operand: 
        self.op_dict[EXP] = lambda operand: 
        self.op_dict[SIGEXTEND] = lambda operand: 

        # Configure logic operations.
        self.op_dict[LT] = lambda operand: 
        self.op_dict[GT] = lambda operand: 
        self.op_dict[SLT] = lambda operand: 
        self.op_dict[SGT] = lambda operand: 
        self.op_dict[EQ] = lambda operand: 
        self.op_dict[ISZERO] = lambda operand: 
        self.op_dict[AND] = lambda operand: 
        self.op_dict[OR] = lambda operand: 
        self.op_dict[XOR] = lambda operand: 
        self.op_dict[NOT] = lambda operand: 
        self.op_dict[BYTE] = lambda operand: 
        self.op_dict[SHL] = lambda operand: 
        self.op_dict[SHR] = lambda operand: 
        self.op_dict[SAR] = lambda operand: 

        # Configure PUSH operations.
        for PUSH in range(PUSH1, PUSH32+1):
            self.op_dict[PUSH] = lambda operand: self.stack.insert(0, operand)
        """
        pass

    # Run the whole bytecode.
    def run_ops(self, op_queue) -> None:
        self.op_queue = op_queue

        for i in range(len(self.op_queue)):
            op, operand, pc = self.op_queue[i]

            # Remember which operation is at which address.
            #self.op_address[self.pc] = i

            self.run_single_op(op, operand)

        # Print stats after exeuction.
        self.stats.print_stats()

    # Run single operation.
    def run_single_op(self, op, operand) -> None:
        #self.op_dict[op](operand)
        if op==STOP:
            print("0x00 STOP")
            print("\tStack: ", self.stack)
            print("\tMemory: ", self.memory)
            print("\tStorage: ", self.storage)
            print("}\n")

        elif op==ADD:
            value1 = self.stack.pop()
            value2 = self.stack.pop()
            self.stack.append((value1+value2)%UINT_256_CEILING)

            print("0x01 ADD")

        elif op==MUL:
            value1 = self.stack.pop()
            value2 = self.stack.pop()
            self.stack.append((value1*value2)%UINT_256_CEILING)
            print("0x02 MUL")

        elif op==SUB:
            value1 = self.stack.pop()
            value2 = self.stack.pop()
            self.stack.append((value1-value2)%UINT_256_CEILING)
            print("0x03 SUB")

        elif op==DIV:
            value1 = self.stack.pop()
            value2 = self.stack.pop()
            if value2 == 0:
                self.stack.append(0)
            else:
                self.stack.append(math.floor((value1/value2))%UINT_256_CEILING)
                #self.stack[0]=(math.floor(self.stack[0]/self.stack[1]))%UINT_256_CEILING
            print("0x04 DIV")

        elif op==SDIV:
            value1 = self.stack.pop()
            value2 = self.stack.pop()
            if value2 == 0:
                value1 = 0
            elif value1 == -UINT_256_CEILING/2 and value2 == -1:
                value1 = -UINT_256_CEILING/2
            else:
                value1 = abs((math.floor(value1/value2)))%UINT_256_CEILING
            self.stack.append(value1)
            print("0x05 SDIV")

        elif op==MOD:
            value1 = self.stack.pop()
            value2 = self.stack.pop()
            if value2 == 0:
                value1 = 0
            else:
                value1 = value1 % value2
            self.stack.append(value1)
            print("0x06 MOD")

        elif op==SMOD:
            value1 = self.stack.pop()
            value2 = self.stack.pop()
            if value2 == 0:
                value1 = 0
            else:
                value1 = abs(value1 % value2)
                #self.stack[0]=abs(self.stack[0]%self.stack[1])
            self.stack.append(value1)
            print("0x07 SMOD")

        elif op==ADDMOD:
            if self.stack[2]==0:
                self.stack[0]=0
            else:
                self.stack[0]=(self.stack[0]+self.stack[1])%self.stack[2]
            print("0x08 ADDMOD")

        elif op==MULMOD:
            value1 = self.stack.pop()
            value2 = self.stack.pop()
            value3 = self.stack.pop()
            if value3 == 0:
                value1 = 0
            else:
                value1=(value1*value2)%value3
            self.stack.append(value1)
            print("0x09 MULMOD")

        elif op==EXP:
            base     = self.stack.pop()
            exponent = self.stack.pop()
            self.stack.append(pow(base, exponent)%UINT_256_CEILING)
            #self.stack[0]=pow(self.stack[0], self.stack[1])%UINT_256_CEILING
            print("0x0a EXP")

        elif op==SIGNEXTEND:
            #need to be done
            print("0x0b SIGNEXTEND")

        #Comparison and Bitwise Logic Ops
        elif op==LT:
            self.stack[0] = (self.stack[0]<self.stack[1]) if 1 else 0
            print("0x10 LT")

        elif op==GT:
            self.stack[0] = (self.stack[0]>self.stack[1]) if 1 else 0
            print("0x11 GT")

        elif op==SLT:
            #signed LT
            print("0x12 SLT")

        elif op==SGT:
            #signed GT
            print("0x13 SGT")

        elif op==EQ:
            self.stack[0] = (self.stack[0]==self.stack[1]) if 1 else 0
            print("0x14 EQ")

        elif op==ISZERO:
            #self.stack[0] = (self.stack[0]==0) if 1 else 0
            value = self.stack.pop()
            self.stack.append(1 if value == 0 else 0)
            print("0x15 ISZERO")

        elif op==AND:
            #bitwise AND
            print("0x16 AND")

        elif op==OR:
            #bitwise OR
            print("0x17 OR")

        elif op==XOR:
            #bitwise XOR
            print("0x18 XOR")

        elif op==NOT:
            #bitwise NOT
            print("0x19 NOT")

        elif op==BYTE:
            #retrieve a byte
            print("0x1a BYTE")

        #SHA3
        elif op==SHA3:
            print("0x20 SHA3")

        #Environmental Information
        #need more information for all those opcodes....
        elif op==ADDRESS:
            # tentative
            self.stack.append(0)
            print("0x30 ADDRESS")

        elif op==BALANCE:
            # tentative
            self.stack.pop()
            self.stack.append(0)
            print("0x31 BALANCE")

        elif op==ORIGIN:
            # tentative
            self.stack.append(0)
            print("0x32 ORIGIN")

        elif op==CALLER:
            # tentative
            self.stack.append(0)
            print("0x33 CALLER")

        elif op==CALLVALUE:
            # tentative
            self.stack.append(0)
            print("0x34 CALLVALUE")

        elif op==CALLDATALOAD:
            # tentative
            self.stack.pop()
            self.stack.append(0)
            print("0x35 CALLDATALOAD")

        elif op==CALLDATASIZE:
            # tentative
            self.stack.append(0)
            print("0x36 CALLDATASIZE")

        elif op==CALLDATACOPY:
            # tentative
            self.stack.pop()
            self.stack.pop()
            self.stack.pop()
            # TODO: Put something in memory
            print("0x37 CALLDATACOPY")

        elif op==CODESIZE:
            self.stack.append(len(self.bytecode)//2)
            print("0x38 CODESIZE")

        elif op==CODECOPY:
            # tentative
            self.stack.pop()
            self.stack.pop()
            self.stack.pop()
            # TODO: Put something in memory
            print("0x39 CODECOPY")

        elif op==GASPRICE:
            # tentative
            self.stack.append(0)
            print("0x3a GASPRICE")

        elif op==EXTCODESIZE:
            # tentative
            self.stack.pop()
            self.stack.append(0)
            print("0x3b EXTCODESIZE")

        elif op==EXTCODECOPY:
            # tentative
            self.stack.pop()
            self.stack.pop()
            self.stack.pop()
            self.stack.pop()
            # TODO: Put something in memory
            print("0x3c EXTCODECOPY")

        elif op==RETURNDATASIZE:
            # tentative
            self.stack.append(0)
            print("0x3d RETURNDATASIZE")

        elif op==RETURNDATACOPY:
            print("0x3e RETURNDATACOPY")

        #Block Information
        elif op==BLOCKHASH:
            #hash of one of the 256 most recent complete blocks
            print("0x40 BLOCKHASH")

        elif op==COINBASE:
            print("0x41 COINBASE")

        elif op==TIMESTAMP:
            print("0x42 TIMESTAMP")

        elif op==NUMBER:
            print("0x43 NUMBER")

        elif op==DIFFICULTY:
            print("0x44 DIFFICULTY")

        elif op==GASLIMIT:
            print("0x45 GASLIMIT")

        #Stack, Memory, Storage and Flow Ops
        elif op==POP:
            self.stack.pop()
            print("0x50 POP")

        elif op==MLOAD:
            address = self.stack.pop()
            self.stack.append(self.memory[address])
            print("0x51 MLOAD")

        elif op==MSTORE:
            address = self.stack.pop()
            value   = self.stack.pop()
            self.memory[address] = value
            print("0x52 MSTORE")

        elif op==MSTORE8:
            address = self.stack.pop()
            value   = self.stack.pop()
            self.memory[address] = value % 256
            print("0x53 MSTORE8")

        elif op==SLOAD:
            address = self.stack.pop()
            self.stack.append(self.storage[address])
            print("0x54 SLOAD")

        elif op==SSTORE:
            address = self.stack.pop()
            value   = self.stack.pop()
            self.storage[address] = value
            print("0x55 SSTORE")

        elif op==JUMP:
            pc = self.stack.pop()
            destination = next(((m_op, m_operand, m_pc) for (m_op, m_operand, m_pc) in self.op_queue \
                                if self.op_queue[2] == destination), None)
            #TODO: change current PC.
            print("0x56 JUMP")

        elif op==JUMPI:
            print("0x57 JUMPI")

        elif op==PC:
            self.stack.append(self.pc)
            print("0x58 PC")

        elif op==MSIZE:
            print("0x59 MSIZE")

        elif op==GAS:
            print("0x5a GAS")

        elif op==JUMPDEST:
            #that's all
            print("0x5b JUMPDEST")
        #Push Ops
        elif op >= PUSH1 and op <= PUSH32:
            self.stack.append(operand)
            print(f"{hex(op)} PUSH{op-(PUSH1-1)}")

        # Duplication Ops
        elif DUP1 <= op <= DUP16:
            target = -(op - (DUP1 - 1))
            self.stack.append(self.stack[target])
            print(f"{hex(op)} DUP{op-(DUP1-1)}")

        #Exchange Ops
        elif SWAP1 <= op <= SWAP16:
            target = -(op - (SWAP1 - 1)) - 1
            self.stack[-1], self.stack[target] = self.stack[target], self.stack[-1]
            print(f"{hex(op)} SWAP{op-(SWAP1-1)}")
        #Logging Ops
        #no need to do
        elif op==LOG0:
            print("0xa0 LOG0")

        elif op==LOG1:
            print("0xa1 LOG1")

        elif op==LOG2:
            print("0xa2 LOG2")

        elif op==LOG3:
            print("0xa3 LOG3")

        elif op==LOG4:
            print("0xa4 LOG4")

        #System Ops
        elif op==CREATE:
            print("0xf0 CREATE")

        elif op==CALL:
            print("0xf1 CALL")

        elif op==CALLCODE:
            print("0xf2 CALLCODE")

        elif op==RETURN:
            print("0xf3 RETURN")

        elif op==DELEGATECALL:
            print("0xf4 DELETEGATECALL")

        elif op==STATICCALL:
            print("0xfa STATICCALL")

        elif op==REVERT:
            print("0xfd REVERT")

        elif op==SELFDESTRUCT:
            print("0xff SELFDESTRUCT")

        else:
            print(f"INVALID OP CODE {hex(op)}")
            exit(1)

        # Advance program counter.
        pc_increment = 1
        if PUSH1 <= op <= PUSH32 : 
            pc_increment += op - (PUSH1 - 1)
        self.pc += pc_increment

        #DEBUG
        print("stack:", self.stack)
        print("memory:", self.memory)
        print("storage:", self.storage, end='\n\n')


    
