# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 19:50:06 2020

@author: olehe

Just an example of how to make windows visible/hidden using 
PsychoPy3 with the pygame backend

This is useful if you're going to run a tight loop 
and don't want Windows 10 to think your windows have become unresponsive
and therefore try to kill the process
"""


from psychopy import core, visual

# Make two windows
winOne = visual.Window(
		size = [500,500],
		#size = [1920,1080],
		screen = 1,
		color='AliceBlue',
		fullScr=True)

winTwo = visual.Window(
		size = [500,500],
		#size = [1920,1080],
		screen = 2,
		color='AliceBlue',
		fullScr=True)

# wait a bit
core.wait(0.1)


# flip the windows
winOne.flip()
winTwo.flip()

# wait a bit
core.wait(0.5)

# hide window 1 first
winOne.winHandle.set_visible(False)
winOne.flip()

# hide window 2 second
winTwo.winHandle.set_visible(False)
winTwo.flip()

# wait a bit
core.wait(0.5)

# run other stuff around here.

# get windows visible again
# NEEDS to be done one by one
winOne.winHandle.set_visible(True)
winOne.winHandle.activate()
winOne.flip()

winTwo.winHandle.set_visible(True)
winTwo.winHandle.activate()
winTwo.flip()

# wait and close
core.wait(2)
winOne.close()
winTwo.close()
core.quit()