#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 15:48:08 2020

@author: briancroxall

A script to find incidence of key terms on a per-state basis
"""

from collections import defaultdict as dd

state_set = set()

terms = ['wk', 'pr', 'gd']

# find all states in data set
with open('map_states.tsv') as data:
    for counter, line in enumerate(data):
        if counter == 0:
            continue  # skip header line
        state = line.split('\t')[3]
        state_set.add(state)

# build empty dictionary
state_dict = dd(dict)  # [state][term][count]

for state in state_set:
    for term in terms:
        state_dict[state][term] = 0

# fill dictionary
with open('map_states.tsv') as data:
    for counter, line in enumerate(data):
        if counter == 0:
            continue  # skip header line
        state = line.split('\t')[3]
        wk_mentions = int(line.split('\t')[4])
        pr_mentions = int(line.split('\t')[5])
        gd_mentions = int(line.split('\t')[6])
        state_dict[state]['wk'] += wk_mentions
        state_dict[state]['pr'] += pr_mentions
        state_dict[state]['gd'] += gd_mentions

# create save file
with open('map-mentions-by-state.tsv', 'w') as savefile:
    print('state', 'issues mentioning wk', 'issues mentioning pr',
          'issues mentioning gd', sep='\t', file=savefile)

# print results to save file
for state, results in state_dict.items():
    wk_total = results['wk']
    pr_total = results['pr']
    gd_total = results['gd']
    with open('map-mentions-by-state.tsv', 'a') as savefile:
        print(state, wk_total, pr_total, gd_total, sep='\t', file=savefile)
