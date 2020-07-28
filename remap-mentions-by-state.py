#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  28 15:48:08 2020

@author: briancroxall

A script to find incidence of key terms on a per-state basis
"""

from collections import defaultdict as dd

state_set = set()

# terms = ['wk', 'pr', 'gd', 'wk+pr+gd']

# find all states in data set
with open('remap.tsv') as data:
    for counter, line in enumerate(data):
        if counter == 0:
            continue  # skip header line
        state = line.split('\t')[3]
        state_set.add(state)

# build empty dictionary
state_dict = dd(int)  # [state][count]

for state in state_set:
    state_dict[state] = 0

# fill dictionary
with open('remap.tsv') as data:
    for counter, line in enumerate(data):
        if counter == 0:
            continue  # skip header line
        state = line.split('\t')[3]
        issues_w_mentions = int(line.split('\t')[4])
        state_dict[state] += issues_w_mentions


# create save file
with open('re-map-mentions-by-state.tsv', 'w') as savefile:
    print('state', 'issues mentioning wk OR pr OR gd', sep='\t', file=savefile)

# print results to save file
for state, results in state_dict.items():
    with open('remap-mentions-by-state.tsv', 'a') as savefile:
        print(state, results, sep='\t', file=savefile)
