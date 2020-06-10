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
from collections import Counter
    

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


if not os.path.isdir('images'):
    os.mkdir('images')


hits_dict = dd(dict)  # [newspaper][date][wk, pr, gd]


dates = []

dates_dict = {'1890-'}


with open('search-results.tsv') as file:
    for counter, line in enumerate(file):
        if counter == 0:  # skips the header in the TSV
            continue
        else:
        # filename = line.split('\t')[0]
            newspaper = line.split('\t')[1]
            location = line.split('\t')[2]
            date = line.split('\t')[3]
            year_s, month_s, day_s = date.split('-')
            day = int(day_s)
            week_s = find_week(day)
            new_date = f'{year_s}-{month_s}-{week_s}'
            wk_hits = line.split('\t')[4]
            pr_hits = line.split('\t')[14]
            gd_hits = line.split('\t')[22]
            hits_dict[newspaper][new_date] = (wk_hits, pr_hits, gd_hits)
            dates.append(date)

freqs_dates = Counter(dates)

