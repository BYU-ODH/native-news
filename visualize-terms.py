#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 13:39:44 2020

@author: briancroxall

Script to visualize search results from native news.
"""

import os
from matplotlib import pyplot as plt
from collections import defaultdict as dd


# Directories
if not os.path.isdir('images'):
    os.mkdir('images')

# Lists
dates = ['1890-11-01', '1890-11-08', '1890-11-15', '1890-11-22', '1890-11-29',
         '1890-12-06', '1890-12-13', '1890-12-20', '1890-12-27', '1891-01-03',
         '1891-01-10', '1891-01-17', '1891-01-24', '1891-01-31', '1891-02-07',
         '1891-02-14', '1891-02-21', '1891-02-28', '1891-03-07', '1891-03-14',
         '1891-03-21', '1891-03-28']
terms = ['wk', 'pr', 'gd']
weeks = ['1 Nov.', '8 Nov.', '15 Nov.', '22 Nov.', '29 Nov.', '6 Dec.',
         '13 Dec.', '20 Dec.', '27 Dec.', '3 Jan.', '10 Jan.', '17 Jan.',
         '24 Jan.', '31 Jan.', '7 Feb.', '14 Feb.', '21 Feb.', '28 Feb.',
         '7 Mar.', '14 Mar.', '21 Mar.', '28 Mar.']

# Sets
newspapers = set()

# Dictionaries
hits_dict = dd(dict)  # [term][date][count]
newspaper_dict = dd(dict)  # [newspaper][date][term][count]
terms_dict = {'wk': 'Wounded Knee',
              'pr': 'Pine Ridge',
              'gd': 'ghost dance'}
week_dict = {'1890-11-01': '1 Nov.', 
             '1890-11-08': '8 Nov.',
             '1890-11-15': '15 Nov.',
             '1890-11-22': '22 Nov.',
             '1890-11-29': '29 Nov.',
             '1890-12-06': '6 Dec.',
             '1890-12-13': '13 Dec.',
             '1890-12-20': '20 Dec.',
             '1890-12-27': '27 Dec.',
             '1891-01-03': '3 Jan.',
             '1891-01-10': '10 Jan.',
             '1891-01-17': '17 Jan.',
             '1891-01-24': '24 Jan.',
             '1891-01-31': '31 Jan.',
             '1891-02-07': '7 Feb.',
             '1891-02-14': '14 Feb.',
             '1891-02-21': '21 Feb.',
             '1891-02-28': '28 Feb.',
             '1891-03-07': '7 Mar.',
             '1891-03-14': '14 Mar.',
             '1891-03-21': '21 Mar.',
             '1891-03-28': '28 Mar.'}

y_dict = {'wk': 450,
          'pr': 700,
          'gd': 300}

# Create dates in dict in the right order.
for term in terms:
    for date in dates:
        hits_dict[term][date] = 0
    """
    use this if I want to number weeks rather than have their full dates
    for each in range(1,23):
        hits_dict[term][each] = 0
    """

with open('search-results.tsv') as file:
    for counter, line in enumerate(file):
        if counter % 100 == 0:
            print('.', end='', flush=True)
        if counter == 0:  # skips the header in the TSV
            continue
        else:
            # filename = line.split('\t')[0]
            newspaper = line.split('\t')[1]
            newspapers.add(newspaper)
            location = line.split('\t')[2]
            date = line.split('\t')[3]
            for date1, date2 in zip(dates, dates[1:]):  # Rob's clever hack
                if date1 <= date < date2:
                    week_date = date1
                    # week_date = int(week_dict[week_date])  # use this if I want to number weeks rather than have their full dates
            wk_hits = int(line.split('\t')[4])
            pr_hits = int(line.split('\t')[14])
            gd_hits = int(line.split('\t')[22])
            hits_dict['wk'][week_date] += wk_hits
            hits_dict['pr'][week_date] += pr_hits
            hits_dict['gd'][week_date] += gd_hits

for term in terms:
    term_counts = hits_dict[term].items()
    # for year, counts in term_counts:
    plt.figure(figsize=(22,12))  # set the size of the graph (width by height)
    plt.plot(*zip(*term_counts), marker='o', markersize='15', linewidth=4)  # get the data from the dictionary; marker specifies round points, markersize adjust size of marker
    ylim = plt.ylim()  # find the min and max of y on the graph
    vert_y = ylim  # use the min and max as a range for the vertical line
    vert_x = (8,8)  # place the vertical line where I want it. 0-indexed
    plt.plot(vert_x, vert_y, linestyle=':', linewidth=2, color='orange')  # draw the dashed, vertical line
    """
    # make the tick labels on the x axis rotate; could use "vertical" or an int
    The list comprehension simply tells it to plot the right number of ticks
    and then it labels them based on the list
    """
    plt.xticks(range(22), weeks, rotation=45)  
    plt.xlabel('\nWeeks', fontweight='bold', fontsize=18)
    plt.ylabel(f'Number of times \'{terms_dict[term]}\' appears per week\n', fontweight='bold', fontsize=18)
    plt.suptitle(f'Total appearances of \'{terms_dict[term]}\' from 1 November 1890 - 31 March 1891', fontsize=24)
    plt.title(f'in the {len(newspapers)} newspapers in the $\itChronicling$ $\itAmerica$ data set\n\n', fontsize=16)
    plt.text(7.7, y_dict[term], 'Wound Knee Massacre', rotation=90, color='orange', fontsize='20')
    plt.savefig(f'images/week_count_{term}.png')
    plt.clf()




# import matplotlib.pyplot as plt
# import numpy as np

# plt.clf()

# # using some dummy data for this example
# xs = np.arange(0,10,1)
# ys = np.random.normal(loc=3, scale=0.4, size=10)

# # 'bo-' means blue color, round points, solid lines
# plt.plot(xs,ys,'bo-')

# # zip joins x and y coordinates in pairs
# for x,y in zip(xs,ys):

#     label = "{:.2f}".format(y)

#     plt.annotate(label, # this is the text
#                  (x,y), # this is the point to label
#                  textcoords="offset points", # how to position the text
#                  xytext=(0,10), # distance from text to points (x,y)
#                  ha='center') # horizontal alignment can be left, right or center

# plt.xticks(np.arange(0,10,1))
# plt.yticks(np.arange(0,7,0.5))

# plt.show()

""" 
            try:
                newspaper_dict[newspaper][week_date]['wk'] = wk_hits
            except KeyError:
                newspaper_dict[newspaper] = week_date
                newspaper_dict[newspaper][week_date]['wk'] = wk_hits
"""
            # hits_dict[newspaper][week_date]['pr'] = pr_hits
            # hits_dict[newspaper][week_date]['gd'] = gd_hits
