
#!/usr/bin/env python3.6

""" Front-end script for training a RL agent. """

import tensorflow as tf
import numpy as np
import datetime
import random
import time
import json
import sys
import os


from learningai.agent.bestVsecondAgent import bestVsecondAgent as bvsAgent
from learningai.agent.randomAgent import randomAgent
from learningai.agent.valueAgent import valueAgent
from learningai.env.cifar_env import cifar_env
from learningai.env.mnist_env import mnist_env
from learningai.env.emnist_env import emnist_env
from utils.loggingManger import loggingManger
from config import Config


def main():

    start = time.time()
    # tf.logging.set_verbosity(tf.logging.DEBUG)
    os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
    np.set_printoptions(precision=6)
    tf.random.set_random_seed(Config.TF_SEED)
    np.random.seed(Config.NP_SEED)

    agent_type  = Config.AGENT_TYPE
    env_type    = Config.ENV_TYPE


    logger = loggingManger()
    sess = tf.Session()

    if env_type == "cifar":
        cnn_env = cifar_env(sess, lr=1e-4)
    elif env_type == "mnist":
        cnn_env = mnist_env(sess, lr=1e-4)
    elif env_type == "emnist":
        cnn_env = emnist_env(sess, lr=1e-4)         
    
    if agent_type == "valueAgent":
        agent = valueAgent(sess, cnn_env, logger, lr=1e-3, gamma=0.9)
    elif agent_type == "BVSB":
        agent = bvsAgent(sess, cnn_env, logger)
    elif agent_type == "random":
        agent = randomAgent(sess, cnn_env, logger)

    sess.run(tf.global_variables_initializer())
    cnn_env.storeNetworkVar()
    cnn_env.resetNetwork()
    agent.store_network_var()
    agent.reset_network()

    agent.train()
    print("End of Training")

    done = time.time()
    elapsed = done - start
    print(elapsed)
    logger.log([["Time elapsed", elapsed]])
    logger.move_finished_result()

if __name__ == '__main__':
    main()