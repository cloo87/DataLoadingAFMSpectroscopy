import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os 
from matplotlib.ticker import MultipleLocator, AutoMinorLocator


#%% Importing data 
filepath = r"C:\Users\xavie\OneDrive\Desktop\PhD_doc\DataLOO\project3\20-21April\PS210419"
os.chdir(filepath)

filename = "PnS_set2.csv"
df = pd.read_csv(filename)

# check for missing data, datatype, and whether number of columns is correct
df.info()

#%% Setting up global parameters of the figure

#Dimension of figure
#Width ; height ; sample name 
fig_width = 10 ; fig_height = 8 ; sample = "CH0577" 

#font type
fonttype = "Arial"

#font size 
plt.rcParams.update({"axes.titlesize":22})
plt.rcParams.update({"axes.labelsize":20})
plt.rcParams.update({"font.family":fonttype})
plt.rcParams['xtick.labelsize']=18
plt.rcParams['ytick.labelsize']=18

#tick direction
plt.rcParams["xtick.top"] = True 
plt.rcParams["ytick.right"] = True
plt.rcParams['xtick.direction'] = 'in'
plt.rcParams['ytick.direction'] = 'in'

#tick width
plt.rcParams['xtick.major.size'] = 6
plt.rcParams['xtick.major.width'] = 1
#plt.rcParams['xtick.minor.size'] = 10
#plt.rcParams['xtick.minor.width'] = 2

#Color palette used for plotting can be found here:https://matplotlib.org/3.5.0/gallery/color/named_colors.html

#%% Plotting single graph or to compare between 2 graphs

############################ Parameters ######################################
#Data point to be plotted
#Point 1; point 2; Labels of these points 
p = 0 ; Label_p = f"p{p}" 
q = p+1 ; Label_q = f"p{q}" # !comment this part if only a single plot is wanted

#Scale of axes 
#xlim ; ylim
xlimit = (-8,8) ; ylimit = (-5,90)

#Parameters of points and line
#markersize #linewidth
ms = 10 ; lw = 0.5

#%%%                            *** Plot phase curve ***

fig, ax = plt.subplots(figsize=(fig_width, fig_height))

ax.plot(df['V*%s' %p], df['Deg%s' %p], 'k.', markersize = ms, linewidth = lw, label=Label_p)
# !comment this part if only a single plot is wanted
ax.plot(df['V*%s' %q], df['Deg%s' %q], 'b.', markersize = ms , linewidth =lw, label=Label_q)
ax.set_xlim(xlimit)

# labelling x and y axes, setting title of the plot and including minor ticks in the plot
graphtitle = f'Phase curve of {sample}'
ax.set_xlabel('Applied bias V$_{DC}$ [V]') ; ax.set_ylabel('Phase [Deg]'); ax.set_title(graphtitle)
ax.yaxis.set_minor_locator(AutoMinorLocator(2))
ax.xaxis.set_minor_locator(AutoMinorLocator(2))

ax.legend(loc='best', fontsize=20)
ax.grid(color='lightgrey')

# saving figure ; for single plot, remove q in the naming
#plt.savefig(f'{graphtitle}_p{p}p{q}.png', bbox_inches='tight', dpi=128)

# if we do not want to use globally set axis parameters
#ax.set_xticklabels(x_ticks, rotation=0, fontsize=8)
#ax.set_yticklabels(y_ticks, rotation=0, fontsize=8)

#%%%                            *** Plot amplitude curve ***


fig, ax1 = plt.subplots(figsize=(fig_width, fig_height))

ax1.plot(df['V%s' %p], df['pm%s' %p], 'k.-', markersize = ms, linewidth = lw, label=f"Dark ({Label_p})")
# !comment this part if only a single plot is wanted
ax1.plot(df['V%s' %q], df['pm%s' %q], 'b.-', markersize = ms , linewidth =lw, label=f"405nm ({Label_q})")
ax1.set_xlim(xlimit)

# labelling x and y axes, setting title of the plot and including minor ticks in the plot
graphtitle = f'Amplitude curve of {sample}'
ax1.set_xlabel('Applied bias V$_{DC}$ [V]') ; ax1.set_ylabel('Amplitude [pm]'); ax1.set_title(graphtitle)
ax1.yaxis.set_minor_locator(AutoMinorLocator(2))
ax1.xaxis.set_minor_locator(AutoMinorLocator(2))

ax1.legend(loc='best', fontsize=20)
ax1.grid("lightgrey")

# saving figure ; for single plot, remove q in the naming
#plt.savefig(f'{graphtitle}_p{p}p{q}.png', bbox_inches='tight', dpi=128)


#%%%                        *** Plotting amplitude and phase curves ***

fig, ax = plt.subplots(figsize=(fig_width, fig_height))

ax.plot(df['V%s' %p], df['pm%s' %p], 'b.-', markersize = ms, linewidth = lw, label = Label_p)
# axis label
ax.set_xlabel('Applied bias V$_{DC}$ [V]') ; ax.set_ylabel('Amplitude [pm]', color='blue')
#set ticks parameters
ax.yaxis.set_minor_locator(AutoMinorLocator(2)) ; ax.xaxis.set_minor_locator(AutoMinorLocator(2))
ax.tick_params(axis='y', colors='blue', which='major')
ax.spines['left'].set_color('blue') 
ax.spines['left'].set_lw(1.7) ; ax.spines['top'].set_lw(1.7) ; ax.spines['bottom'].set_lw(1.7)
# insert grid
ax.grid(color='lightgrey')
# set x limit
ax.set_xlim(xlimit)
ax.set_title(f"Amplitude and phase curves \n of {sample} at point {p}")

ax2 = ax.twinx()
ax2.plot(df['V*%s' %p], df['Deg%s' %p], 'r.', markersize = ms, linewidth = lw, label=Label_p)
ax2.set_ylabel('Phase [Deg]', color='red')
ax2.tick_params(axis='y', colors='red', which='major')
ax2.spines['right'].set_color('red')
ax2.spines['right'].set_lw(1.7)


# saving figure 
#plt.savefig(f"Amp&phase_curves_{sample}_p{p}.png", bbox_inches='tight', dpi=128)


#%% Multiple plots for comparison

fig, ax = plt.subplots(2,2, figsize=(12,9))

ax[0,0].plot(df['V%s' %p], df['pm%s' %p], 'b.-', markersize = ms, linewidth = lw, label = Label_p)
ax[1,0].plot(df['V*%s' %p], df['Deg%s' %p], 'r.', markersize = ms, linewidth = lw, label=Label_p)
ax[0,1].plot(df['V%s' %q], df['pm%s' %q], 'b.-', markersize = ms, linewidth = lw, label = Label_q)
ax[1,1].plot(df['V*%s' %q], df['Deg%s' %q], 'r.', markersize = ms, linewidth = lw, label=Label_q)

ax[0,0].set_title(f"{sample} point{p}")
ax[0,1].set_title(f"{sample} point{q}")
ax[0,0].set_ylabel('Amplitude [pm]') ; ax[0,1].set_ylabel('Amplitude [pm]')
ax[1,0].set_xlabel('Applied bias V$_{DC}$ [V]') ; ax[1,0].set_ylabel('Phase [Deg]')
ax[1,1].set_xlabel('Applied bias V$_{DC}$ [V]') ; ax[1,1].set_ylabel('Phase [Deg]')

ax[0,0].set_xlim(xlimit)
ax[1,0].set_xlim(xlimit)
ax[0,1].set_xlim(xlimit)
ax[1,1].set_xlim(xlimit)