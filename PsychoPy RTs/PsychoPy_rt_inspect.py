# -*- coding: utf-8 -*-
"""
Created on Thu May  6 21:09:13 2021

@author: olehe
"""


import pandas as pd
import numpy as np
import seaborn as sns


rt = pd.read_csv('RT_test.csv')

# remove a few 'outliers'

rt = rt[rt['RT']<0.34]
rt = rt[rt['RT']>0.26]

sns.scatterplot(data=rt)

# then just check how "unique" the values are
# round to full milliseconds

toCheck = round(rt['RT'], 3)

numDup = len(toCheck) - len(np.unique(toCheck))

print('There are ' + str(numDup) + ' duplicates, out of ' + str(len(toCheck)) + ' RTs')


