#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 13:34:04 2020

@author: briancroxall

A script to count the number of newspapers in each state
"""

from collections import Counter
from pprint import pprint

states = set()

with open('map_states.tsv') as data:
    for counter, line in enumerate(data):
        if counter == 0:
            continue
        state = line.split('\t')[3]
        states.add(state)
        # if state == '':
        #     print(line)
        
state_dict = {}

for state in states:
    state_dict[state] = 0
    
with open('map_states.tsv') as data:
    for counter, line in enumerate(data):
        if counter == 0:
            continue
        state = line.split('\t')[3]
        state_dict[state] += 1
        

state_freqs = Counter(state_dict)
with open('state-freqs.txt', 'w') as output:
    pprint(state_freqs, stream=output)

