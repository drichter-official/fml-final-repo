# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 16:38:10 2022

@author: danie
"""
TRANSITHIST = 10000

# CALLBACKS-Training Settings
EPSILON_START = 1
EPSILON_MIN = 0.1
EPSILON_DECAY = 0.9995
EPSILON_IMITATE = 0.8
EPSILON_IMITATE_DECAY = 0.9999

IMITATE = True

# TRAIN Settings
GAMMA = 0.99

BATCH_SIZE = 32
UPDATE_ACTIONS = 4
UPDATE_TARGET = 2000

LOADCHECKPOINT = True

LEARNINGRATE = 0.0001