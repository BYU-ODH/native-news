#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 27 09:37:20 2020

@author: briancroxall
"""

from glob import glob


corpus = glob('combined-ocr/*.txt')
test = ['combined-ocr/abilene-weekly-reflector_1890-11-06.txt',
        'combined-ocr/alexandria-gazette_1891-02-18.txt']


for counter, each in enumerate(test):
    if counter % 100 == 0:
        print('.', end='', flush=True)
    filename = each.split('/')[-1]
    no_ext = filename.split('.')[0]
    newspaper, date = no_ext.split('_')
    
    