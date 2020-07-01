#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 15:48:08 2020

@author: briancroxall

A script to find incidence of key terms on a per-state basis
"""

state_set = set()

with open('map_states.tsv') as data:
    for counter, line in enumerate(data):
        if counter == 0:
            continue  # skip header line
        state = line.split('\t')[3]
        
