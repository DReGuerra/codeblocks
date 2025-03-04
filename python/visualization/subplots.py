"""This script contains an example for making subploit in matplotlib.

Contents:
Visualization
1. Visualization constants
2. Adaptable subplots structure (NORWS x NCOLS, and standard figure size)
3. Text annotation on the plot
4. Save fgiure in different file formats
5. Dynamic zooming in plots

Data handling:
1. Read in data using Pandas DataFrame
2. Find indices of columns in the DataFrame
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def zoomLims(data,i,f):
    """
    Adaptive zoom in plots.

        Parameters:
        data: pd.DataFrame
            Data to be plotted
        i   : int
            Index of the column in the DataFrameto be plotted
        f   : int
            Zoom in/out factor

        Returns:
        lims: 
            Low and high limits to achieve the desired zoom
    """ 
    mean = data.iloc[:,i].mean()
    std = data.iloc[:,i].std()
    loLim = mean - f*std
    hiLim = mean + f*std
    lims = [loLim,hiLim]
    return lims

# ==============================================================
# read in data
thermo = pd.read_csv('data/thermotable_nvt.csv')
# get indices
t = thermo.columns.get_loc("Step")
temp = thermo.columns.get_loc("Temp")
# rolling mean
ROLLWINDOW = 25
aveT = thermo.iloc[:,temp].rolling(window=ROLLWINDOW).mean()

# ==============================================================
# Visualization
figTypes = ['.jpg','.png']
# sizing factors
TICKSFONT = 13; TITLEFONT = 15; TEXTFONT = 15
FIGWIDTH = 6.4; FIGHEIGHT = 4.8; LINEWIDTH = 3
# zoom factors
ZOOMIN = 1.5; ZOOMOUT = 8

# ==============================================================
# Temperature
NROWS = 1; NCOLS = 2
f, axs = plt.subplots(nrows=NROWS,ncols=NCOLS,
                      figsize=(NCOLS*FIGWIDTH,NROWS*FIGHEIGHT))

axs[0].plot(thermo.iloc[:,t],thermo.iloc[:,temp])
axs[0].plot(thermo.iloc[:,t],aveT)
axs[0].hlines(y=thermo.iloc[:,temp].mean(),xmin=0,xmax=thermo.iloc[:,t].iloc[-1],
              linewidth=LINEWIDTH,color='k',zorder=3)
axs[0].set_xlabel('Time',fontsize=TITLEFONT)
axs[0].set_ylabel('Temperature',fontsize=TITLEFONT)
axs[0].tick_params(axis='x',labelsize=TICKSFONT)
axs[0].tick_params(axis='y',labelsize=TICKSFONT)
axs[0].set_ylim(zoomLims(thermo,temp,ZOOMOUT))
axs[0].annotate('T$_{avg}$ = ' + str(np.around(thermo.iloc[:,temp].mean(),decimals=2)),
                xy=(0.45,0.2), xycoords='axes fraction', fontsize=TEXTFONT)

axs[1].plot(thermo.iloc[:,t],thermo.iloc[:,temp])
axs[1].plot(thermo.iloc[:,t],aveT)
axs[1].hlines(y=thermo.iloc[:,temp].mean(),xmin=0,xmax=thermo.iloc[:,t].iloc[-1],
              linewidth=LINEWIDTH,color='k',zorder=3)
axs[1].set_xlabel('Time',fontsize=TITLEFONT)
axs[1].set_ylabel('Temperature',fontsize=TITLEFONT)
axs[1].tick_params(axis='x',labelsize=TICKSFONT)
axs[1].tick_params(axis='y',labelsize=TICKSFONT)
axs[1].set_ylim(zoomLims(thermo,temp,ZOOMIN))

for type in figTypes:
    f.savefig('figures/temp_env' + type, bbox_inches='tight')