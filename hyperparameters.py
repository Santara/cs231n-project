MINIBATCH_SIZE = 32
REPLAY_MEMORY_SIZE = 1000000
AGENT_HISTORY_LENGTH = 4
TARGET_UPDATE_FREQUENCY = 10000 # C
DISCOUNT_FACTOR = 0.99
ACTION_REPEAT = 4
UPDATE_FREQUENCY = 4

LEARNING_RATE = 0.00025
GRADIENT_MOMENTUM = 0.95
SQUARED_GRADIENT_MOMENTUM = 0.95
MIN_SQUARED_GRADIENT = 0.01
INITIAL_EXPLORATION = 1
FINAL_EXPLORATION = 0.1
FINAL_EXPLORATION_FRAME = 1000000
REPLAY_START_SIZE = 50000
NO_OP_MAX = 30

CHECKPOINT_FREQUENCY = 100000

INPUT_SIZE = 84

CONV_1_SIZE = 8
CONV_1_STRIDE = 4
CONV_1_DEPTH = 32

CONV_2_SIZE = 4
CONV_2_STRIDE = 2
CONV_2_DEPTH = 64

CONV_3_SIZE = 3
CONV_3_STRIDE = 1
CONV_3_DEPTH = 64

FC_SIZE = 512

