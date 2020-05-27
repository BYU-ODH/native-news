#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 27 09:37:20 2020

@author: briancroxall
"""

from glob import glob
import re
from datetime import datetime


startTime = datetime.now()


# Corpus
corpus = sorted(glob('combined-ocr/*.txt'))
test = ['combined-ocr/abilene-weekly-reflector_1890-11-06.txt',
        'combined-ocr/alexandria-gazette_1891-02-18.txt']

# Output file
with open('search-wounded.tsv', 'w') as output:
    print('filename', 'newspaper', 'date',
          '# wk hits', 'wk strings', 
          '# hostile hits', 'hostile strings',
          '# dakota hits', 'dakota strings',
          '# tibbles hits', 'tibbles strings',
          '# sioux hits', 'sioux strings',
          '# pr hits', 'pr strings',
          '# bf hits', 'bf strings',
          '# be hits', 'be strings',
          '# lf hits', 'lf strings',
          sep='\t', file=output)

# Regex
re_wk = r'(w[0o]und[@e3]d\skn[e@3][e@3])'
re_hostile = r'(h[o0]st[i1|]le)'
re_dakota = r'(d[a@]k[0o]t[a@])'
re_tibbles = r'(t[1|i]bbles)'
re_sioux = r'(s[1i|][o0]ux)'
re_pr = r'(p[1i]ne\sr[i1]dge)'
re_bf = r'(b[1i|]g\sf[o0][o0]t)'
re_be = r'(br[1|i]ght\seyes)'
re_lf = r'(l[a@]\sflesche)'

# Counters
wk_counter = 0
hostile_counter = 0
dakota_counter = 0
tibbles_counter = 0
sioux_counter = 0
pr_counter = 0
bf_counter = 0
be_counter = 0
lf_counter = 0

for counter, each in enumerate(corpus):
    if counter % 100 == 0:
        print('.', end='', flush=True)
    filename = each.split('/')[-1]
    no_ext = filename.split('.')[0]
    newspaper, date = no_ext.split('_')
    with open(each) as in_file:
        text = in_file.read()
    wk_results = re.findall(re_wk, text, flags=re.I)
    hostile_results = re.findall(re_hostile, text, flags=re.I)
    dakota_results = re.findall(re_dakota, text, flags=re.I)
    tibbles_results = re.findall(re_tibbles, text, flags=re.I)
    sioux_results = re.findall(re_sioux, text, flags=re.I)
    pr_results = re.findall(re_pr, text, flags=re.I)
    bf_results = re.findall(re_bf, text, flags=re.I)
    be_results = re.findall(re_be, text, flags=re.I)
    lf_results = re.findall(re_lf, text, flags=re.I)
    # if len(wk_results) >= 1:
    #     wk_counter += 1
    with open('search-wounded.tsv', 'a') as save_file:
        print(filename, newspaper, date,
              len(wk_results), wk_results,
              len(hostile_results), hostile_results,
              len(dakota_results), dakota_results,
              len(tibbles_results), tibbles_results,
              len(sioux_results), sioux_results,
              len(pr_results), pr_results,
              len(bf_results), bf_results,
              len(be_results), be_results,
              len(lf_results), lf_results,
              sep='\t', file=save_file)
    
print('\nTime elapsed: ', datetime.now() - startTime)    