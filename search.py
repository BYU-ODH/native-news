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
test = ['combined-ocr/asheville-daily-citizen_asheville,-n.c._1891-03-17.txt',
        'combined-ocr/abilene-weekly-reflector_abilene,-kan._1890-12-04.txt']

# Output file
with open('search-results.tsv', 'w') as output:
    print('filename', 'newspaper', 'location', 'date',
          '# wk hits', 'wk strings', 
          '# hostile hits', 'hostile strings',
          '# dakota hits', 'dakota strings',
          '# tibbles hits', 'tibbles strings',
          '# sioux hits', 'sioux strings',
          '# pr hits', 'pr strings',
          '# bf hits', 'bf strings',
          '# be hits', 'be strings',
          '# lf hits', 'lf strings',
          '# gd hits', 'gd strings',
          sep='\t', file=output)

# Regex
re_wk = r'(w[0o]und[@e3]d\skn[e@3][e@3])'  # https://regex101.com/r/2DotPH/1
re_hostile = r'(h[o0]st[i1|]le)'
re_dakota = r'(d[a@]k[0o]t[a@])'
re_tibbles = r'(t[1|i]bbles)'
re_sioux = r'(s[1i|][o0]ux)'
re_pr = r'(p[1i|]ne\sr[i1|]dge)'
re_bf = r'(b[1i|]g\sf[o0][o0]t)'
re_be = r'(br[1|i]ght\seyes)'
re_lf = r'(l[a@]\sflesche)'
re_gd = r'(gh[o0]s[\+t]\sd[@a]nc[e@3])'

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
gd_counter = 0

for counter, each in enumerate(corpus):
    if counter % 100 == 0:
        print('.', end='', flush=True)
    filename = each.split('/')[-1]
    no_ext = filename.split('.')[:-1]
    joined = '.'.join(no_ext)
    newspaper, location, date = joined.split('_')
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
    gd_results = re.findall(re_gd, text, flags=re.I)
    if len(wk_results) >= 1:
        wk_counter += 1
    if len(hostile_results) >= 1:
        hostile_counter += 1
    if len(dakota_results) >= 1:
        dakota_counter += 1
    if len(tibbles_results) >= 1:
        tibbles_counter += 1
    if len(sioux_results) >= 1:
        sioux_counter += 1
    if len(pr_results) >= 1:
        pr_counter += 1
    if len(bf_results) >= 1:
        bf_counter += 1
    if len(be_results) >= 1:
        be_counter += 1
    if len(lf_results) >= 1:
        lf_counter += 1
    if len(gd_results) >= 1:
        gd_counter += 1
    with open('search-results.tsv', 'a') as save_file:
        print(filename, newspaper, location, date,
              len(wk_results), wk_results,
              len(hostile_results), hostile_results,
              len(dakota_results), dakota_results,
              len(tibbles_results), tibbles_results,
              len(sioux_results), sioux_results,
              len(pr_results), pr_results,
              len(bf_results), bf_results,
              len(be_results), be_results,
              len(lf_results), lf_results,
              len(gd_results), gd_results,
              sep='\t', file=save_file)

with open('search-counters.txt', 'w') as new_file:
    print('Number of results in wk_counter: ', wk_counter,
          '\nNumber of results in hostile_counter: ', hostile_counter,
          '\nNumber of results in dakota_counter: ', dakota_counter,
          '\nNumber of results in tibbles_counter: ', tibbles_counter,
          '\nNumber of results in sioux_counter: ', sioux_counter,
          '\nNumber of results in pr_counter: ', pr_counter,
          '\nNumber of results in bf_counter: ', bf_counter,
          '\nNumber of results in be_counter: ', be_counter,
          '\nNumber of results in lf_counter: ', lf_counter,
          '\nNumber of results in gd_counter: ', gd_counter,
          file=new_file)
    
print('\nTime elapsed: ', datetime.now() - startTime)    