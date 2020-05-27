#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 27 09:37:20 2020

@author: briancroxall
"""

from glob import glob
import re


# Corpus
corpus = sorted(glob('combined-ocr/*.txt'))
test = ['combined-ocr/abilene-weekly-reflector_1890-11-06.txt',
        'combined-ocr/alexandria-gazette_1891-02-18.txt']

# Output file
with open('search-wounded.tsv', 'w') as output:
    print('filename', 'newspaper', 'date', '# hits', 'strings', sep='\t',
          file=output)

# Regex
re_wk = r'(w[0o]und[@e3]d kn[e@3][e@3])'

# Counters
wk_counter = 0

for counter, each in enumerate(corpus):
    if counter % 100 == 0:
        print('.', end='', flush=True)
    filename = each.split('/')[-1]
    no_ext = filename.split('.')[0]
    newspaper, date = no_ext.split('_')
    with open(each) as in_file:
        text = in_file.read()
    results = re.findall(re_wk, text, flags=re.I)
    if len(results) >= 1:
        wk_counter += 1
    with open('search-wounded.tsv', 'a') as save_file:
        print(filename, newspaper, date, len(results), results, sep='\t',
              file=save_file)
    
    