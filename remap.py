#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 16:29:49 2020

@author: briancroxall

Script to re-compile results of key terms by location so that issues don't get
counted multiple times.
"""

from collections import defaultdict as dd


hits_dict = dd(dict)  #[newsloc][term][count]
newsloc_set = set()


with open('remap.tsv', 'w') as savefile:
    print('newsloc', 'newspaper', 'location', 'state',
          'issues mentioning wk OR pr OR gd', sep='\t', file=savefile)


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
    hits_dict[each] = 0
    
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
            hits_dict[newsloc] += 1
            continue
        elif wk_hits == 0:
            pr_hits = int(line.split('\t')[14])
            if pr_hits >= 1:
                hits_dict[newsloc] += 1
                continue
            elif pr_hits == 0:
                gd_hits = int(line.split('\t')[22])
                if gd_hits >= 1:
                    hits_dict[newsloc] += 1

for newsloc, results in hits_dict.items():
    newspaper, location = newsloc.split('_')
    with open('remap.tsv', 'a') as output:
        print(newsloc, newspaper, location, '', results, sep='\t', file=output)
