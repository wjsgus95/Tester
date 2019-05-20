
PLACEHOLDER_JSON = "common/placeholder.json"

# Default output file path.
DEFAULT_OUT_PATH = 'stats.json'

# No operand constant.
NO_OPERAND = None

ANY = 'any'
UINT256 = 'uint256'
BYTES = 'bytes'

UINT_256_MAX = 2**256 - 1
UINT_256_CEILING = 2**256
UINT_255_MAX = 2**255 - 1
UINT_255_CEILING = 2**255
UINT_255_NEGATIVE_ONE = -1 + UINT_256_CEILING
NULL_BYTE = b'\x00'
EMPTY_WORD = NULL_BYTE * 32

UINT_160_CEILING = 2**160

#
# Stack Limit
#
STACK_DEPTH_LIMIT = 1024


#
# Gas Costs and Refunds
#
GAS_NULL = 0
GAS_ZERO = 0
GAS_BASE = 2
GAS_VERYLOW = 3
GAS_LOW = 5
GAS_MID = 8
GAS_HIGH = 10
GAS_EXTCODE = 20
GAS_BALANCE = 20
GAS_SLOAD = 50
GAS_JUMPDEST = 1
GAS_SSET = 20000
GAS_SRESET = 5000

REFUND_SCLEAR = 15000

GAS_SELFDESTRUCT = 0
GAS_SELFDESTRUCT_NEWACCOUNT = 25000
GAS_CREATE = 32000
GAS_CALL = 40
GAS_CALLVALUE = 9000
GAS_CALLSTIPEND = 2300
GAS_NEWACCOUNT = 25000
GAS_EXP = 10
GAS_EXPBYTE = 10
GAS_MEMORY = 3
GAS_TXCREATE = 32000
GAS_TXDATAZERO = 4
GAS_TXDATANONZERO = 68
GAS_TX = 21000
GAS_LOG = 375
GAS_LOGDATA = 8
GAS_LOGTOPIC = 375
GAS_SHA3 = 30
GAS_SHA3WORD = 6
GAS_COPY = 3
GAS_BLOCKHASH = 20
GAS_CODEDEPOSIT = 200

GAS_MEMORY_QUADRATIC_DENOMINATOR = 512


#
# Pre-compile contract gas costs
#
GAS_SHA256 = 60
GAS_SHA256WORD = 12

GAS_RIPEMD160 = 600
GAS_RIPEMD160WORD = 120

GAS_IDENTITY = 15
GAS_IDENTITYWORD = 3

GAS_ECRECOVER = 3000

GAS_ECADD = 500
GAS_ECMUL = 40000

GAS_ECPAIRING_BASE = 100000
GAS_ECPAIRING_PER_POINT = 80000


#
# Gas Limit
#
GAS_LIMIT_EMA_DENOMINATOR = 1024
GAS_LIMIT_ADJUSTMENT_FACTOR = 1024
GAS_LIMIT_MINIMUM = 5000
GAS_LIMIT_MAXIMUM = 2 ** 63 - 1

GAS_LIMIT_USAGE_ADJUSTMENT_NUMERATOR = 3
GAS_LIMIT_USAGE_ADJUSTMENT_DENOMINATOR = 2


#
# Difficulty
#
DIFFICULTY_ADJUSTMENT_DENOMINATOR = 2048
DIFFICULTY_MINIMUM = 131072

BOMB_EXPONENTIAL_PERIOD = 100000
BOMB_EXPONENTIAL_FREE_PERIODS = 2

UNCLE_DEPTH_PENALTY_FACTOR = 8
MAX_UNCLE_DEPTH = 6
MAX_UNCLES = 2

#
# SECPK1N
#
SECPK1_P = 2**256 - 2**32 - 977
SECPK1_N = 115792089237316195423570985008687907852837564279074904382605163141518161494337
SECPK1_A = 0
SECPK1_B = 7
SECPK1_Gx = 55066263022277343669578718895168534326250603453777594175500187360389116729240
SECPK1_Gy = 32670510020758816978083085130507043184471273380659243275938904335757337482424
SECPK1_G = (SECPK1_Gx, SECPK1_Gy)


#
# Genesis Data
#
GENESIS_BLOCK_NUMBER = 0
GENESIS_DIFFICULTY = 17179869184
GENESIS_GAS_LIMIT = 5000
#GENESIS_PARENT_HASH = ZERO_HASH32
#GENESIS_COINBASE = ZERO_ADDRESS
GENESIS_NONCE = b'\x00\x00\x00\x00\x00\x00\x00B'  # 0x42 encoded as big-endian-integer
#GENESIS_MIX_HASH = ZERO_HASH32
GENESIS_EXTRA_DATA = b''

GAS_MOD_EXP_QUADRATIC_DENOMINATOR = 20

#
# BLOCKHASH opcode maximum depth
#
MAX_PREV_HEADER_DEPTH = 256

#
# Call overrides
#
DEFAULT_SPOOF_V = 37
DEFAULT_SPOOF_R = 1
DEFAULT_SPOOF_S = 1
