# -*- coding: utf-8 -*-
"""
Created on Thu May  6 20:27:55 2021

@author: olehe
"""

# General imports
from psychopy.hardware import keyboard, forp
from psychopy import core, data, gui, visual, event, sound, logging
import numpy as np
import pandas as pd





kb = keyboard.Keyboard(bufferSize=5) 

rt_list = []


win = visual.Window(
		size = [800,800],
		#size = [1920,1080],
		screen = 1,
		color='AliceBlue',
		fullScr=False,
		waitBlanking=False)

fixCrossOne = visual.TextStim(
		win = win,
		text = '+',
		font = 'Arial',
		pos=[0,0],
		height=0.7,
		color='Black')


textWinOne = visual.TextStim(
		win = win,
		text='',
		font='Arial',
		pos=[0,0],
		height=0.1,
		color='Black')


def intro():
		# this function shows introduction text
		print('Running Introduction for active part')
		textWinOne.text = 'Press B AFTER the fixation cross disappear'
		textWinOne.draw()
		win.flip()
		running = True
		timer = core.Clock()
		startTime = timer.getTime()
		while running:
			currTime = timer.getTime()
			textWinOne.draw()
			win.flip()
			if currTime - startTime >= 5:
				running = False
		return

def getReady():
		# this function shows introduction text
		print('Running Introduction for active part')
		textWinOne.text = 'Get ready'
		textWinOne.draw()
		win.flip()
		running = True
		timer = core.Clock()
		startTime = timer.getTime()
		while running:
			currTime = timer.getTime()
			textWinOne.draw()
			win.flip()
			if currTime - startTime >= 1:
				running = False
		return

def trial():
	print('Running trial')
	# uncomment this if want random wait
	thisWaitMs = np.random.randint(300, 700)
	
	# set wait at 500 ms now, just to get a rhythm going
	#thisWaitMs = 500
	
	timer = core.Clock()
	startTime = timer.getTime()
	
	waiting = True
	responding = True
	while waiting:
		currTime = timer.getTime()
		fixCrossOne.draw()
		win.flip()
		if currTime - startTime >= thisWaitMs * 0.001:
			waiting = False
			
	
	kb.clearEvents()
	win.callOnFlip(kb.clock.reset)
	win.flip()
	while responding:
		keys = kb.getKeys(['b'], waitRelease=False, clear=True)
		if keys:
			key = keys[0]
			thisRT = key.rt
			print(thisRT)
			responding = False
	
	
	return thisRT



#%% Run experiment

n_trials = 100

intro()
for thisTrial in range(n_trials):
	getReady()
	thisRT = trial()
	rt_list.append(thisRT)
	

print(rt_list)
pd.DataFrame(rt_list, columns=['RT']).to_csv('RT_test.csv', index=False)	
win.close()
core.quit()
	
	
	
			
			
	
	