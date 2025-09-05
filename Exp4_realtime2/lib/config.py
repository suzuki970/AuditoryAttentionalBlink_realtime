#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 17 16:51:32 2025

@author: yutasuzuki
"""

import numpy as np
import glob
import soundfile as sf
from itertools import product
import random
import pandas as pd

from pyglet import canvas
display = canvas.Display()

import platform
os_name = platform.system()

if os_name == "Darwin":
    print("Running on macOS.\n")
elif os_name == "Windows":
    print("Running on Windows.\n")
    
import sounddevice as sd
for i, device in enumerate(sd.query_devices()):
    if device['max_output_channels'] > 0:
        print(f"{i}: {device['name']}")


EYE_TRACKER="Eyelink"
# EYE_TRACKER="Neon"

SOUND_DEVICE = 13
# SOUND_DEVICE = 3

TIME_FIXATION = 6
TIME_ISI = 0.05
AUDIO_SAMPLING_RATE = 44100

FRAME_RATE = 60
RESAMPLING_RATE = 100
SAMPLING_RATE = 1000
VISUAL_DISTANCE = 60

NUM_TRIAL_TRAINING = 20
ITERATION = 8
NUM_SOUNDS = 16

Lag = list(range(1, 6))
# TargetLocs = [4,6]
TargetLocs = [1]
# NUM_TRIAL = 4 * len(Lag) * len(TargetLocs)
# NUM_TRIAL = 2

LUMINANCE_BACKGROUND = -1
# LUMINANCE_BACKGROUND = [-1,-1,-1]

DOT_PITCH = 0.33
TASK_JITTER = [40, 50]
# NUM_TASK = NUM_TRIAL
# NUM_SESSION = 1

# REF_WINDOW = 10 * SAMPLING_RATE
# EVAL_WINDOW = 5 * SAMPLING_RATE

SCREEN_RANGE = 1
# SCREEN_RANGE = 0.5

FULL_SCREEN = True
# FULL_SCREEN = False

SCREEN_NUM = 1

window_analysis = 15
keyList = ['escape', 'left', 'right']

screenSize = []
for i, screen in enumerate(display.get_screens()):
    print(f"Screen {i}: {screen.width} x {screen.height}")
    screenSize.append([int(screen.width*SCREEN_RANGE), int(screen.height*SCREEN_RANGE)])

def load_stimuli(folder):
    file_list = sorted(glob.glob(folder+'/*.wav'))
    stimuli = []
    for filepath in file_list:
        data, fs = sf.read(filepath)
        stereo = np.tile(data[:, None], (1, 2))
        
        stimuli.append(stereo.astype('float32'))
        
    return stimuli

def make_condition_sequence():
    
    tmp = []
    iter_count = [ITERATION//4]*2 + [ITERATION]
    for i,cond in enumerate(["T1_only","T2_only","Both"]):
        combs = list(product([cond], TargetLocs, Lag))
        tmp.extend(combs * iter_count[i])

    trial_indices = list(range(1, 21))
    tmp2 = []
    for _ in range(len(tmp)//len(trial_indices)):
        shuffled = trial_indices.copy()
        random.shuffle(shuffled)
        tmp2.extend(shuffled)

    for i, t in enumerate(tmp):
        tmp[i] = list(t) + [tmp2[i]]

    random.shuffle(tmp)
  
    condition_frame = pd.DataFrame({
        'seq': [x[0] for x in tmp],
        't1_order': [x[1] for x in tmp],
        't1_target': [x[3] for x in tmp],
        't2_order': [x[2] for x in tmp],
    })
    
    low, high = TASK_JITTER
    condition_frame['jitter'] = list(np.random.randint(low, high + 1, size=(len(tmp), 1)).reshape(-1))        
    
    condition_frame['t0_order'] = [np.random.randint(0, NUM_SOUNDS,x).tolist() for x in condition_frame['jitter']]
    condition_frame['t0_no_tar_order'] = [np.random.randint(0, NUM_SOUNDS,x).tolist() for x in condition_frame['jitter']]
  
    condition_frame.loc[condition_frame["seq"]==0,"t1_order"]=-1
    condition_frame.loc[condition_frame["seq"]==0,"t1_target"]=-1
    condition_frame.loc[condition_frame["seq"]==0,"t2_order"]=-1
    
    condition_frame.loc[condition_frame["seq"]==1,"t1_order"]=-1
    condition_frame.loc[condition_frame["seq"]==1,"t1_target"]=-1
    
    condition_frame.loc[condition_frame["seq"]==2,"t2_order"]=-1
    
    return condition_frame