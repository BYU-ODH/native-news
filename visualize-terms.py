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
# from collections import Counter
# from pprint import pprint
    
"""
def find_week(day):
    if day in range(1, 8):
        return 'week1'
    elif day in range(8, 15):
        return 'week2'
    elif day in range(15, 21):
        return 'week3'
    elif day in range(21, 29):
        return 'week4'
    else:
        return 'week5'
"""

if not os.path.isdir('images'):
    os.mkdir('images')


hits_dict = dd(dict)  # [newspaper][date][wk, pr, gd]


dates = ['1890-11-01', '1890-11-08', '1890-11-15', '1890-11-22', '1890-11-29',
         '1890-12-06', '1890-12-13', '1890-12-20', '1890-12-27', '1891-01-03',
         '1891-01-10', '1891-01-17', '1891-01-24', '1891-01-31', '1891-02-07',
         '1891-02-14', '1891-02-21', '1891-02-28', '1891-03-07', '1891-03-14',
         '1891-03-21', '1891-03-28']

newspapers = set()


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
            for date1, date2 in zip(dates, dates[1:]):
                if date1 <= date < date2:
                    week_date = date1
            # year_s, month_s, day_s = date.split('-')
            # day = int(day_s)
            # week_s = find_week(day)
            # new_date = f'{year_s}-{month_s}-{week_s}'
            wk_hits = line.split('\t')[4]
            pr_hits = line.split('\t')[14]
            gd_hits = line.split('\t')[22]
            hits_dict[newspaper][week_date] = (wk_hits, pr_hits, gd_hits)
            dates.append(date)

# freqs_dates = Counter(dates)
# with open('date_freqs.txt', 'w') as output:
#     pprint(freqs_dates, stream=output)
