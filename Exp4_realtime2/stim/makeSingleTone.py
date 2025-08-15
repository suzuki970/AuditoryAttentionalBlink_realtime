#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 13 11:15:01 2021

@author: yutasuzuki
"""

from makeAuditoryStim import makeAuditoryStim
import numpy as np
import shutil
import os
import glob

semitones = 2**(1/12)

ffreq = 529

cfg = {
'freq_pattern' : [],
'vol_pattern'  : [],
'fs'           : 44100,
# 'sec'          : 0.03,
# 'isi'          : 0.08,
'fallTime'     : 2.5,       # 2ms
'sep'          : False,
'reverse'      : False,
'keepFile'     : False
}

# for i in np.arange(21):
#     cfg['freq_pattern'].append(int(round(ffreq*semitones**i)))

#%% Shen 2006
cfg['sec']=0.03
# cfg['sec']=0.03/6

# cfg['sec']=10
cfg['isi']=0.05
cfg['saveFolder'] = './' + str(int(cfg['sec']*1000)) + 'ms'

cfg['freq_pattern'] = [529, 554, 580, 607, 636,
                       666, 697, 730, 764, 800, 
                       838, 877, 918, 961, 1006,
                       1056, 1106, 1158, 1213, 1270, 1330]
cfg['vol_pattern'] = np.ones(len(cfg['freq_pattern']))*4
cfg['vol_pattern'] = cfg['vol_pattern'].tolist()

target_dB = 65
a=[65.6, 66.0, 66.3, 66.7, 66.9,
   67.2, 67.5, 67.9, 68.1, 68.5, 
   68.9, 68.8, 68.8, 68.9, 69.1,
   69.4, 69.6, 69.9, 70.4, 70.4, 71.0]
cfg['vol_pattern'] = cfg['vol_pattern']-(np.array(a)-target_dB)

cfg['iter'] = int(180 / (cfg['sec']*4 + cfg['isi']*4))

m = makeAuditoryStim(cfg)
m.makePureTones()
m.adjustFadein_out('./' + str(int(cfg['sec']*1000)) + 'ms' + '/original/')


m.composeTones(6)
# b = m.synthesizeTones()
# m.makeSweepSound([636,1006],4) # original
# m.repeatTones('./' + str(int(cfg['sec']*1000)) + 'ms' + '/sweep/',500)

# vol = 68.1-target_dB
# m.makeSweepSound([636,1006],vol)

# m.makeSweepSound([452,3462],7.9)


#%% Mondor 1998
# # cfg['freq_pattern'] = [452, 493, 537, 586, 639,
# #                        697, 760, 829, 904, 944, 
# #                        986,1029,1122,1224,1335,
# #                        1456,1587,1731,1888, 2059,4000]

# # cfg['freq_pattern'] = [600,775,1002,1295,1674]

# cfg['vol_pattern'] = np.ones(len(cfg['freq_pattern']))*4
# cfg['vol_pattern'] = cfg['vol_pattern'].tolist()

# cfg['iter'] = int(180 / (cfg['sec']*4 + cfg['isi']*4))

# m = makeAuditoryStim(cfg)
# b = m.synthesizeTones()
# m.adjustFadein_out('./30ms/synthesize')


# fileListRemove = glob.glob('../stim/distractor/*')
# for f in fileListRemove:
#     os.remove(f)

# fileList = glob.glob(cfg['saveFolder']+'/fadeinout/*')
# for fName in fileList:
#     shutil.move(fName, '../stim/distractor')

# fileListRemove = glob.glob('../stim/T1/*')
# for f in fileListRemove:
#     os.remove(f)

# fileList = glob.glob('./5ms/composed/*')
# for fName in fileList:
#     shutil.move(fName, '../stim/T1')

# fileListRemove = glob.glob('../stim/T2/*')
# for f in fileListRemove:
#     os.remove(f)

# fileList = glob.glob('./30ms/sweep/SweepSound_fadeinout*')
# for fName in fileList:
#     shutil.move(fName, '../stim/T2')
