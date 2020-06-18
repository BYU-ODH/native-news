#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 13:26:12 2020

@author: briancroxall

Find newspaper issues from 2 January 1891
"""

from glob import glob
from shutil import copyfile
import os

if not os.path.isdir('2-jan-issues'):
    os.mkdir('2-jan-issues')

corpus = glob('combined-ocr/*.txt')

jan2_counter = 0

for counter, each in enumerate(corpus):
    if counter % 100 == 0:
        print('.', end='', flush=True)
    filename = each.split('/')[-1]
    no_ext = filename.split('.')[:-1]
    rejoin = '.'.join(no_ext)
    date = rejoin.split('_')[-1]
    if date == '1891-01-02':
        jan2_counter += 1
        copyfile(each, f'2-jan-issues/{filename}')
print(jan2_counter)

