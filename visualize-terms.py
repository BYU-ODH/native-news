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
weeks = ['Nov. 1', 'Nov. 8', 'Nov. 15', 'Nov. 22', 'Nov. 29', 'Dec. 6',
         'Dec. 13', 'Dec. 20', 'Dec. 27', 'Jan. 3', 'Jan. 10', 'Jan. 17',
         'Jan. 24', 'Jan. 31', 'Feb. 7', 'Feb. 14', 'Feb. 21', 'Feb. 28',
         'Mar. 7', 'Mar. 14', 'Mar. 21', 'Mar. 28']

gd_count = 0

# Sets
newspapers = set()
gd_newspapers = set()

# Dictionaries
hits_dict = dd(dict)  # [term][date][count]
newspaper_dict = dd(dict)  # [newspaper][date][term][count]
terms_dict = {'wk': 'Wounded Knee',
              'pr': 'Pine Ridge',
              'gd': 'ghost dance'}
# week_dict = {'1890-11-01': '1 Nov.', 
#              '1890-11-08': '8 Nov.',
#              '1890-11-15': '15 Nov.',
#              '1890-11-22': '22 Nov.',
#              '1890-11-29': '29 Nov.',
#              '1890-12-06': '6 Dec.',
#              '1890-12-13': '13 Dec.',
#              '1890-12-20': '20 Dec.',
#              '1890-12-27': '27 Dec.',
#              '1891-01-03': '3 Jan.',
#              '1891-01-10': '10 Jan.',
#              '1891-01-17': '17 Jan.',
#              '1891-01-24': '24 Jan.',
#              '1891-01-31': '31 Jan.',
#              '1891-02-07': '7 Feb.',
#              '1891-02-14': '14 Feb.',
#              '1891-02-21': '21 Feb.',
#              '1891-02-28': '28 Feb.',
#              '1891-03-07': '7 Mar.',
#              '1891-03-14': '14 Mar.',
#              '1891-03-21': '21 Mar.',
#              '1891-03-28': '28 Mar.'}
y_dict = {'wk': -10,  # this dictionary helps plot the label on the orange line
          'pr': -10,
          'gd': 105}

# Create dates in dict in the right order.
for term in terms:
    for date in dates:
        hits_dict[term][date] = 0
    """
    use the following if I want to number weeks rather than have their full 
    dates 
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
            if wk_hits >= 1:
                wk_yn = 1
            else:
                wk_yn = 0
            pr_hits = int(line.split('\t')[14])
            if pr_hits >= 1:
                pr_yn = 1
            else:
                pr_yn = 0
            gd_hits = int(line.split('\t')[22])
            if gd_hits >= 1:
                gd_yn = 1
                gd_newspapers.add(newspaper)
            else:
                gd_yn = 0
            gd_count += gd_yn
            # hits_dict['wk'][week_date] += wk_hits
            # hits_dict['pr'][week_date] += pr_hits
            # hits_dict['gd'][week_date] += gd_hits
            hits_dict['wk'][week_date] += wk_yn
            hits_dict['pr'][week_date] += pr_yn
            hits_dict['gd'][week_date] += gd_yn

for term in terms:
    term_counts = hits_dict[term].items()
    plt.figure(figsize=(22,12))  # set the size of the graph (width by height)
    """
    # get the data from the dictionary; marker specifies round points,
    markersize adjust size of marker
    """
    dates, counts = zip(*term_counts)
    plt.plot(dates, counts, marker='o', markersize='15', linewidth=4)  
    ylim = plt.ylim()  # find the min and max of y on the graph
    vert_y = ylim  # use the min and max as a range for the vertical line
    vert_x = (8,8)  # place the vertical line where I want it. 0-indexed
    plt.plot(vert_x, vert_y, linestyle=':', linewidth=2, color='red')  # draw the dashed, vertical line
    """
    # make the tick labels on the x axis rotate; could use "vertical" or an int
    The list comprehension simply tells it to plot the right number of ticks
    and then it labels them based on the list
    """
    plt.xticks(range(22), weeks, rotation=45, fontsize=14)
    plt.yticks(fontsize=14)
    plt.xlabel('\nWeek starting on', fontweight='bold', fontsize=18)
    plt.ylabel(f'Number of newspaper issues \'{terms_dict[term]}\' appears in per week\n',
               fontweight='bold', fontsize=18)
    # plt.suptitle(f'Weekly appearances of \'{terms_dict[term]}\' from 1 November 1890 - 31 March 1891', fontsize=24)
    # plt.title(f'in the {len(newspapers)} newspapers in the $\itChronicling$ $\itAmerica$ data set\n', fontsize=18)
    plt.text(7.7, y_dict[term], 'Wounded Knee Massacre, 29 Dec.', rotation=90, 
             color='red', fontsize=18, fontweight='bold')
    for date, counts in term_counts:
        label = '{:}'.format(counts)
        plt.annotate(label,
                      (date, counts),
                      textcoords='offset points',
                      xytext=(21,16),  # this adjusts the x,y of label placement
                      ha='center',
                      fontsize=18,
                      fontweight='bold')
    plt.savefig(f'images/week_count_{term}.png')
    plt.clf()

# %%

with open('gd.tsv', 'w') as savefile:
    print('Week starting on', 'Number of newspaper issues \'ghost dance\' appears in per week',
          sep='\t', file=savefile)

for week, count in hits_dict['wk'].items():
    with open('gd.tsv', 'a') as output:
        print(week, count, sep='\t', file=output)

