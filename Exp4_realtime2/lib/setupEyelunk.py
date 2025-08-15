#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 18 13:44:00 2025

@author: yutasuzuki
"""

# el = pylink.EyeLink()

# # el.startRecording(1, 1)
# el.startRecording(1, 1, 1, 1)

# while not el.getNextData() == pylink.SAMPLE_TYPE:
#     pass

# # サンプル取得
# sample = el.getNewestSample()

# if sample.isRightSample():
#     gaze = sample.getRightEye().getGaze()      # (x, y)
#     pupil = sample.getRightEye().getPupilSize()
# else:
#     gaze = sample.getLeftEye().getGaze()
#     pupil = sample.getLeftEye().getPupilSize()

# print(f"Gaze: {gaze}, Pupil: {pupil}")

import pylink
from psychopy import visual, core,monitors
from EyeLinkCoreGraphicsPsychoPy import EyeLinkCoreGraphicsPsychoPy
import sys
import config as config

# %%

# Set the screen resolution
scn_w, scn_h = (config.screenSize[0], config.screenSize[1])

# Connect to the tracker
el_tracker = pylink.EyeLink()

# Open an EDF data file on the Host PC
el_tracker.openDataFile('test.edf')

# Open a window, be sure to specify the monitor resolution
mon = monitors.Monitor('myMonitor', width=53.0, distance=70.0)
mon.setSizePix((scn_w, scn_h))

win = visual.Window((scn_w, scn_h),
                    # fullscr=False,
                    fullscr=True,
                    monitor=mon,
                    winType='pyglet',
                    units='pix')

# Send over a command to let the tracker know the correct screen resolution
scn_coords = "screen_pixel_coords = 0 0 %d %d" % (scn_w - 1, scn_h - 1)
el_tracker.sendCommand(scn_coords)

# Instantiate a graphics environment (genv) for calibration
genv = EyeLinkCoreGraphicsPsychoPy(el_tracker, win)

# Set background and foreground colors for calibration
foreground_color = (-1, -1, -1)
background_color = win.color
genv.setCalibrationColors(foreground_color, background_color)

# The target could be a "circle" (default), a "picture", a "movie" clip,
# or a rotating "spiral".
genv.setTargetType('circle')
# Configure the size of the calibration target (in pixels)
genv.setTargetSize(24)

# Beeps to play during calibration, validation and drift correction
# parameters: target, good, error
# Each parameter could be ''--default sound, 'off'--no sound, or a wav file
# genv.setCalibrationSounds('', '', '')

# Request Pylink to use the graphics environment (genv) we customized above
pylink.openGraphicsEx(genv)

# Calibrate the tracker
el_tracker.doTrackerSetup()

# Close the data file
el_tracker.closeDataFile()

# Disconnect from the tracker
el_tracker.close()

# Quit pygame
core.quit()
sys.exit()


# from EyeLinkCoreGraphicsPsychoPy import EyeLinkCoreGraphicsPsychoPy

# pylink.closeGraphics()

# Eyelink に接続
# tracker = pylink.EyeLink()

# # EDFファイル名
# edf_file = "demo.edf"
# tracker.openDataFile(edf_file)
# tracker.sendCommand("file_event_filter = LEFT,RIGHT,FIXATION,SACCADE,BLINK,MESSAGE,BUTTON")
# tracker.sendCommand("file_sample_data = LEFT,RIGHT,GAZE,AREA,GAZERES,STATUS")

# # PsychoPy Window
# win = visual.Window([1024, 768], fullscr=False, monitor='testMonitor', units='pix')

# # Eyelink Display に対応させる
# scn_width, scn_height = win.size
# tracker.sendCommand(f"screen_pixel_coords = 0 0 {scn_width-1} {scn_height-1}")
# tracker.sendMessage(f"DISPLAY_COORDS 0 0 {scn_width-1} {scn_height-1}")
# # pylink.openGraphicsEx(pylink.EyeLinkCustomDisplay())
# genv = EyeLinkCoreGraphicsPsychoPy(tracker, win)

# キャリブレーション
# tracker.doTrackerSetup()

# # 終了処理
# tracker.closeDataFile()
# tracker.receiveDataFile(edf_file, edf_file)
# tracker.close()
