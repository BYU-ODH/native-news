#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 13:39:44 2020

@author: briancroxall

Script to visualize search results from native news.
"""

import os
# from matplotlib import pyplot as plt
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
hits_dict = dd(dict)  # [date][term][count]
newspaper_dict = dd(dict)  # [newspaper][date][term][count]
terms_dict = {'wk': 'Wounded Knee',
              'pr': 'Pine Ridge',
              'gd': 'ghost dance'}

# Create dates in dict in the right order.
for date in dates:
    for term in terms:
        hits_dict[date][term] = 0


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
            wk_hits = int(line.split('\t')[4])
            pr_hits = int(line.split('\t')[14])
            gd_hits = int(line.split('\t')[22])
            hits_dict[week_date]['wk'] += wk_hits
            hits_dict[week_date]['pr'] += pr_hits
            hits_dict[week_date]['gd'] += gd_hits

"""
            try:
                newspaper_dict[newspaper][week_date]['wk'] = wk_hits
            except KeyError:
                newspaper_dict[newspaper] = week_date
                newspaper_dict[newspaper][week_date]['wk'] = wk_hits
"""
            # hits_dict[newspaper][week_date]['pr'] = pr_hits
            # hits_dict[newspaper][week_date]['gd'] = gd_hits
