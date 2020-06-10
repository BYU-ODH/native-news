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


if not os.path.isdir('images'):
    os.mkdir('images')


hits_dict = dd(dict)  # [newspaper][date][wk, pr, gd]


dates = set()

with open('search-results.tsv') as file:
    for counter, line in enumerate(file):
        if counter == 0:  # skips the header in the TSV
            continue
        else:
        # filename = line.split('\t')[0]
            newspaper = line.split('\t')[1]
            location = line.split('\t')[2]
            date = line.split('\t')[3]
            wk_hits = line.split('\t')[4]
            pr_hits = line.split('\t')[14]
            gd_hits = line.split('\t')[22]
            hits_dict[newspaper][date] = (wk_hits, pr_hits, gd_hits)
            dates.add(date)
