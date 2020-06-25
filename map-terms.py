#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 10:32:11 2020

@author: briancroxall

Script to compile the information we need for mapping appearances of terms.
"""

with open('search-results.tsv') as data:
    for counter, line in enumerate(data):
        if counter % 100 == 0:
            print('.', end='', flush=True)
        if counter == 0:  # skips the header in the TSV
            continue
        filename = line.split('\t')[0]
        newspaper = line.split('\t')[1]
        location = line.split('\t')[2]
        newsloc = f'{newspaper}_{location}'
        date = line.split('\t')[3]
        wk_hits = int(line.split('\t')[4])
        if wk_hits >= 1:  # find hits per issue rather than total hits
            wk_hits = 1
        pr_hits = int(line.split('\t')[14])
        if pr_hits >= 1:
            pr_hits = 1
        gd_hits = int(line.split('\t')[22])
        if gd_hits >= 1:
            gd_hits = 1