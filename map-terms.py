#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 10:32:11 2020

@author: briancroxall

Script to compile the information we need for mapping appearances of terms.
"""

from collections import defaultdict as dd

hits_dict = dd(dict)  #[newsloc][term][count]
newsloc_set = set()

with open('map.tsv', 'w') as savefile:
    print('newsloc', 'newspaper', 'location', 'state', 'issues mentioning wk',
          'issues mentioning pr', 'issues mentioning gd', sep='\t',
          file=savefile)

terms = ['wk', 'pr', 'gd']

print('Building empty dictionary')
with open('search-results.tsv') as data:
    for counter, line in enumerate(data):
        if counter % 100 == 0:
            print('.', end='', flush=True)
        if counter == 0:  # skips the header in the TSV
            continue
        # filename = line.split('\t')[0]
        newspaper = line.split('\t')[1]
        location = line.split('\t')[2]
        newsloc = f'{newspaper}_{location}'
        newsloc_set.add(newsloc)

# build empty dictionary        
for each in newsloc_set:
    for term in terms:
        hits_dict[each][term] = 0

print('\nFilling dictionary')
with open('search-results.tsv') as data:
    for counter, line in enumerate(data):
        if counter % 100 == 0:
            print('.', end='', flush=True)
        if counter == 0:  # skips the header in the TSV
            continue
        newspaper = line.split('\t')[1]
        location = line.split('\t')[2]
        newsloc = f'{newspaper}_{location}'
        # date = line.split('\t')[3]
        wk_hits = int(line.split('\t')[4])
        if wk_hits >= 1:  # find hits per issue rather than total hits
            wk_hits = 1
            hits_dict[newsloc]['wk'] += wk_hits
        pr_hits = int(line.split('\t')[14])
        if pr_hits >= 1:
            pr_hits = 1
            hits_dict[newsloc]['pr'] += pr_hits
        gd_hits = int(line.split('\t')[22])
        if gd_hits >= 1:
            gd_hits = 1
            hits_dict[newsloc]['gd'] += gd_hits

for newsloc, results in hits_dict.items():
    newspaper, location = newsloc.split('_')
    wk_total = results['wk']
    pr_total = results['pr']
    gd_total = results['gd']
    with open('map.tsv', 'a') as output:
        print(newsloc, newspaper, location, '', wk_total, pr_total, gd_total,
              sep='\t', file=output)
