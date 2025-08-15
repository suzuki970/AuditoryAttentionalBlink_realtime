# -*- coding: utf-8 -*-
"""
Created on Fri Aug  8 09:08:04 2025

@author: suzuki
"""

# from psychopy.hardware import keyboard
# kb = keyboard.Keyboard()

# while True:
#     keys = kb.getKeys(waitRelease=False,clear=False)
    
#     # if keys:
#     #     for key in keys:
#     print(keys)
#     # else:
#     #     print("No key press")
            
# from psychopy import core

from psychopy.hardware import keyboard
from psychopy import visual,core, event, iohub
import config as config


kb = keyboard.Keyboard()

win = visual.Window(
    size=config.screenSize[config.SCREEN_NUM],
    screen=config.SCREEN_NUM, 
    color=config.LUMINANCE_BACKGROUND,
    units='pix', 
    # units='norm', 
    fullscr=config.FULL_SCREEN
    )

# io = iohub.launchHubServer()
# kb = io.devices.keyboard

print("Press keys (ESC to quit)")

while True:
    
    # keys = event.getKeys()
    keys = kb.getKeys(waitRelease=False)
    # keys = kb.getEvents(waitRelease=False)

    for key in keys:
        # print(key)
        print(key.name)
        if key == 'escape':
            core.quit()
            
    core.wait(0.001)

