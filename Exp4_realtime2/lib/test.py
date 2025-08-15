#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 18 14:53:26 2025

@author: yutasuzuki
"""

from psychopy import visual, core
import pylink
from EyeLinkCoreGraphicsPsychoPy import EyeLinkCoreGraphicsPsychoPy
import time

def main():
    el_tracker = pylink.EyeLink()  # dummy mode
    el_tracker.setOfflineMode()
    # pylink.pumpDelay(50)

    file_event_flags = 'LEFT,RIGHT,FIXATION,SACCADE,BLINK,MESSAGE,BUTTON,INPUT'
    link_event_flags = 'LEFT,RIGHT,FIXATION,SACCADE,BLINK,BUTTON,FIXUPDATE,INPUT'

    # file_sample_flags = 'LEFT,RIGHT,GAZE,HREF,RAW,AREA,GAZERES,BUTTON,STATUS,INPUT'
    file_sample_flags = 'LEFT,RIGHT,GAZE,HREF,RAW,AREA'
    link_sample_flags = 'LEFT,RIGHT,GAZE,HREF,RAW,AREA'
    # link_sample_flags = 'LEFT,RIGHT,GAZE,GAZERES,AREA,STATUS,INPUT'

    # el_tracker.sendCommand("file_event_filter = %s" % file_event_flags)
    el_tracker.sendCommand("file_sample_data = %s" % file_sample_flags)
    # el_tracker.sendCommand("link_event_filter = %s" % link_event_flags)
    el_tracker.sendCommand("link_sample_data = %s" % link_sample_flags)


    # el_tracker.sendCommand("sample_data = LEFT,RIGHT,GAZE,AREA")
    # el_tracker.sendCommand("event_data = LEFT,RIGHT,FIXATION,SACCADE,BLINK")
    
    el_tracker.startRecording(1, 1,1,1)
    # pylink.pumpDelay(100)
    win = visual.Window((1920/2, 1080/2), 
                        fullscr=False,
                        # fullscr=True,
                        units='pix',
                        winType='pyglet', 
                        allowStencil=True
                        )
    
    # calib_instruction = 'Enter: Show/Hide camera image\n' + \
    #                     'Left/Right: Switch camera view\n' + \
    #                     'C: Calibration\n' + \
    #                     'V: Validation\n' + \
    #                     'O: Start Recording\n' + \
    #                     '+=/-: CR threshold\n' + \
    #                     'Up/Down: Pupil threshold\n' + \
    #                     'Alt+arrows: Search limit'
    # __calibInst_pos__ = (0,0)
    # visual.TextStim(win,
    #                height=600,
    #                color=[0, 1, 1],
    #                pos=__calibInst_pos__,
    #                units='pix',
    #                text=calib_instruction)
    # win.flip()
    genv = EyeLinkCoreGraphicsPsychoPy(el_tracker, win)
    genv.setCalibrationColors((-1, -1, -1), win.color)
    genv.setTargetType('circle')
    genv.setTargetSize(24)
    pylink.openGraphicsEx(genv)
    print("Calling doTrackerSetup()...")
    el_tracker.doTrackerSetup()
    print("Calibration finished.")
    
    print("Getting pupil size in real-time...")
    for _ in range(1000):
        sample = el_tracker.getNewestSample()
        if sample is not None:
            eye = sample.getRightEye()
            if eye is not None:
                pupil = eye.getPupilSize()
                print(f"Pupil: {pupil:.2f}")
                
        time.sleep(0.01)  # 約100Hz
    
    # print(f"Receiving {edf_filename}...")
    # el_tracker.receiveDataFile(edf_filename, os.path.join(output_path, edf_filename))
    # print("Transfer complete.")

    win.close()
    core.quit()

main()
