#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 15 12:38:18 2021

@author: yutasuzuki
"""

import librosa
import soundfile as sf

y, sr = librosa.core.load('stim/01migi_m.mp3', sr=44100, mono=True)
sf.write("new_test.wav", y, sr, subtype="PCM_16")
