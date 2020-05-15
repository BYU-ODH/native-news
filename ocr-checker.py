#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 15 10:12:51 2020

@author: briancroxall
This script will check which objects have been downloaded and which haven't.
"""

from glob import glob


# Corpus 
expected = set()
downloaded = set(glob('ocr-html/*.html'))

# File creation
with open('ocr-checker.txt', 'w'):
    pass

# Counters
duplicates = 0
duplicatesB = 0


with open('data-dictionary.tsv') as data_file:
    for counter, line in enumerate(data_file):
        if counter % 100 == 0:
            print('.', end='', flush=True)
        newspaper, location, date, img_num, link, ocr_link = line.split('\t')
        newspaper = newspaper.lower().replace(' ', '-')
        img_num = img_num.replace('seq-', '')  # remove seq- from each page number
        filename = f'ocr-html/{newspaper}_{date}_p{img_num}.html'
        if filename in expected:
            duplicates += 1
            with open('ocr-checker.txt', 'a') as output:
                print(filename, file=output)
        else:
            expected.add(filename)
        expected.add(filename)
    
print()
print('Results of comparing sets: ', expected.difference(downloaded))
print('Number of expected files: ', len(expected))
print('Number of downloaded files: ', len(downloaded))


print('Number of duplicates from set creation:', duplicates)

with open('ocr-checker.txt') as file:
    for line in file:
        duplicatesB += 1

print('Number of duplicates in ocr-checker.txt:', duplicatesB)
