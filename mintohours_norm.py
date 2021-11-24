# -*- coding: utf-8 -*-
"""
Created on Fri Sep  10 10:18:55 2021
@author: giaco
"""

#code useful to shift from min resolution to hourly, such that the csv load demand can be fed as input to MicrogridsPy
#yearly profile is required

import numpy as np
import pandas as pd

#minute and hour indexes
minute_index = pd.date_range("2021-01-01 00:00:00", "2021-12-31 23:59:00", freq="1min")
hour_index = np.linspace(1,8760,8760,dtype=int)

#from load to loadH 
load=pd.read_csv('#INSERT THE PATH TO THE .csv FILE FROM RAMP OUTPUT#',usecols=['0'])
load.index = minute_index
loadH = load.resample('H').mean() 
loadH.index = hour_index

#export in .csv 
loadH.to_csv('#XXX.csv TO NAME THE FILE OF OUTPUT IN HOURLY RESOLUTION#')


