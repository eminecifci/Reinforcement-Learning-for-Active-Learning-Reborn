class Config:

    # GENERAL INFO
    VERSION = 1.00
    NAME = "dqn-with-exploration"
    DESCRIPTION = ""
    
    # TRANING SETTING
    AGENT_TRAINING_EPISODES = 50
    CLASSIFICATION_BUDGET = 1000
    CLASSIFICATION_EPOCH = 50
    SELECTION_BATCHSIZE = 50
    TRAINING_BATCHSIZE = 10


    # loggerManger
    LOG_TOP_FOLDER = "result"

    # MEMORY_SIZE = 100000
    # NUM_LAST_FRAMES = 4
    # LEVEL = "snakeai/levels/10x10-blank.json"
    # NUM_EPISODES = -1
    # BATCH_SIZE = 64
    # DISCOUNT_FACTOR = 0.95
    # USE_PRETRAINED_MODEL = False
    # PRETRAINED_MODEL = "dqn-00000000.model"
    # # Either sarsa, dqn, ddqn
    # LEARNING_METHOD = "dqn"
    # MULTI_STEP_REWARD = False
    # MULTI_STEP_SIZE = 5
    # PRIORITIZED_REPLAY = False
    # PRIORITIZED_RATING = 1
    # DUEL_NETWORK = False
    # #foodspeed =0 no movement. foodspeed =2 food moves one step every 2 timesteps
    # FOODSPEED = 0