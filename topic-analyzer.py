#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 28 10:13:04 2020

@author: briancroxall
"""

# from collections import defaultdict as dd
from shutil import copyfile
import os

def get_news_date(file):
    file = indices [1]
    filename = file.split('/')[-1]
    no_ext = filename.split('.')[0]
    newspaper, date = no_ext.split('_')
    return (newspaper, date, filename)


def cast_date(date):
    #  This function casts the dates to ints
    year, month, day = date.split('-')
    year = int(year)
    month = int(month)
    day = int(day)
    return (year, month, day)


# Directories
if not os.path.isdir('tm-subset'):
    os.mkdir('tm-subset')

# Dictionaries
# wk_dict = dd(dict)

with open('tm_wk_results.tsv', 'w') as output:
    print('newspaper', 'date', 'wk', sep='\t', file=output)

with open('topic-modeling/corp_stop_removed_100tops_comp.txt') as results:
    for line in results:
        indices = line.split('\t')
        file_list = indices[1].split('/')[6:]
        file = '/'.join(file_list)
        newspaper, date, filename = get_news_date(indices)
        year, month, day = cast_date(date)
        wk_topic = float(indices[72])
        if wk_topic < 0.01:
            wk_topic = 0
        if wk_topic > 0:
            copyfile(file, f'tm-subset/{filename}')
        with open('tm_wk_results.tsv', 'a') as output:
            print(newspaper, date, round(wk_topic, 4), sep='\t', file=output)
        # try:
        #     wk_dict[newspaper][year][month][day] = wk_topic
        # except KeyError:
        #     wk_dict[newspaper] = str(year)
        #     wk_dict[newspaper][year] = str(month)
        #     wk_dict[newspaper][year][month] = str(day)
        #     wk_dict[newspaper][year][month][day] = wk_topic