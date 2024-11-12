#!/usr/bin/env python

import matplotlib.patches as mpatches
import matplotlib.pylab as plt
import os

daylist = ['Mon','Tue', 'Wed', 'Thu', 'Fri']
colors  = {'Lecture': 'pink', 'Exercise':'lightgreen', 'Project': 'lightblue', 'Lunch':'white', 'PyQuiz':'wheat', 'break': 'white'}

#colors = ['pink', 'lightgreen', 'lightblue', 'wheat', 'salmon']

script_dir = os.path.dirname(os.path.abspath(__file__))
input_file = os.path.join(script_dir, '../files/schedule.csv')
output_file = os.path.join(script_dir, '../schedule.png')
day_label  = 'Schedule'

fig = plt.figure(figsize=(15,9.89))

# Set Axis
ax = fig.add_subplot(111)
ax.yaxis.grid(color = 'lightgrey')
ax.set_xlim(0.5,len(daylist)+0.5)
ax.set_ylim(17.1, 8.9)
ax.set_xticks(range(1,len(daylist)+1))
ax.set_xticklabels(daylist, size = 15)
ax.set_ylabel('Time', size = 15)

     # Set Second Axis
ax2 = ax.twiny().twinx()
ax2.set_xlim(ax.get_xlim())
ax2.set_ylim(ax.get_ylim())
ax2.set_xticks(ax.get_xticks())
ax2.set_xticklabels(daylist, size = 15)
ax2.set_ylabel('Time', size = 15)

fh  = open(input_file, 'r')
fh.readline()


for line in fh:
    data  = line.split(',')
    event = data[-1].strip()
    etype = data[-2]
    data  = list(map(float, data[:4]))
    day   = data[0]-0.48
    start = data[1]+data[2]/60
    end   = start+data[3]/60

    plt.fill_between([day, day+0.96], [start, start], [end,end], color=colors[etype], edgecolor='k', linewidth=0.5)
    # plot beginning time
    plt.text(day+0.02, start+0.05 ,'{0}:{1:0>2}'.format(int(data[1]),int(data[2])), va='top', fontsize=7)
    # plot event name
    plt.text(day+0.48, (start+end)*0.5, event, ha='center', va='center', fontsize=11)
    


plt.title(day_label,y=1.07)

handles = [mpatches.Patch(color=c, label=l) for l,c in colors.items() if c != 'white']
plt.legend(handles=handles, bbox_to_anchor=(1.05, 1), loc='upper left')

plt.savefig(output_file, bbox_inches='tight')
