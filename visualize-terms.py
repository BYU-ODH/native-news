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
    plt.figure(figsize=(20,12))  # set the size of the graph
    plt.plot(*zip(*term_counts), linewidth=4)  # get the data from the dictionary
    ylim = plt.ylim()  # find the min and max of y on the graph
    vert_y = ylim  # use the min and max as a range for the vertical line
    vert_x = (8,8)  # place the vertical line where I want it. 0-indexed
    plt.plot(vert_x, vert_y, linestyle=':', linewidth=2)  # draw the dashed, vertical line
    plt.xticks(rotation='vertical')  # make the tick labels on the x axis rotate
    plt.xlabel('Weeks', fontweight='bold')
    plt.ylabel('Counts', fontweight='bold')
    plt.suptitle(f'Total appearances of \'{terms_dict[term]}\'', fontsize=24)
    plt.title('from 1 Nov 1890 - 31 Mar 1891', fontsize=16)
    plt.savefig(f'images/week_count_{term}.png')
    plt.clf()

    
""" 
            try:
                newspaper_dict[newspaper][week_date]['wk'] = wk_hits
            except KeyError:
                newspaper_dict[newspaper] = week_date
                newspaper_dict[newspaper][week_date]['wk'] = wk_hits
"""
            # hits_dict[newspaper][week_date]['pr'] = pr_hits
            # hits_dict[newspaper][week_date]['gd'] = gd_hits
