#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 18 17:21:22 2020

@author: briancroxall

This script will combine the different pages of an issue of a newspaper into
a single document.
"""

from glob import glob
import os
from collections import defaultdict
from datetime import datetime


startTime = datetime.now()


def get_filename(file):
    no_dir = file.split('/')[-1]
    no_ext = no_dir.split('.')[:-1]
    joined = '.'.join(no_ext)
    return joined


# Corpus
corpus = sorted(glob('ocr-txt/*.txt'))
test = ['ocr-txt/the-newberry-herald-and-news_newberry,-s.c._1890-12-18_p1.txt',
        'ocr-txt/the-newberry-herald-and-news_newberry,-s.c._1890-12-18_p2.txt',
        'ocr-txt/the-newberry-herald-and-news_newberry,-s.c._1890-12-18_p3.txt',
        'ocr-txt/the-newberry-herald-and-news_newberry,-s.c._1890-12-18_p4.txt']
test2 = ['ocr-txt/the-morning-news_savannah,-ga._1891-02-25_p1.txt',
         'ocr-txt/the-morning-news_savannah,-ga._1891-02-25_p2.txt',
         'ocr-txt/the-morning-news_savannah,-ga._1891-02-25_p3.txt',
         'ocr-txt/the-morning-news_savannah,-ga._1891-02-25_p4.txt',
         'ocr-txt/the-morning-news_savannah,-ga._1891-02-25_p5.txt',
         'ocr-txt/the-morning-news_savannah,-ga._1891-02-25_p6.txt',
         'ocr-txt/the-morning-news_savannah,-ga._1891-02-25_p7.txt',
         'ocr-txt/the-morning-news_savannah,-ga._1891-02-25_p8.txt',
         'ocr-txt/the-newberry-herald-and-news_newberry,-s.c._1890-12-18_p1.txt',
         'ocr-txt/the-newberry-herald-and-news_newberry,-s.c._1890-12-18_p2.txt',
         'ocr-txt/the-newberry-herald-and-news_newberry,-s.c._1890-12-18_p3.txt',
         'ocr-txt/the-newberry-herald-and-news_newberry,-s.c._1890-12-18_p4.txt']

# Directories
if not os.path.isdir('combined-ocr'):
    os.mkdir('combined-ocr')

# Dictionaries
newsdict = defaultdict(list)


# Build dictionary
for counter, each in enumerate(corpus):
    if counter % 100 == 0:
        print('.', end='', flush=True)
    filename = get_filename(each)
    newspaper, location, date, page = filename.split('_')
    try:
        newsdict[(newspaper, location, date)].append(page)
    except KeyError:
        newsdict[(newspaper, location, date)] = []
        
print('\nDictionary built')
print('Expected number of newspaper issues: ', len(newsdict))

print('\nStarting to combine texts')
for (newspaper, location, date), pages in newsdict.items():
    for page in pages:
        with open(f'ocr-txt/{newspaper}_{location}_{date}_{page}.txt') as ocr:
            text = ocr.read()
        if page == 'p1':
            with open(f'combined-ocr/{newspaper}_{location}_{date}.txt', 'w') as save_file:
                print(text, file=save_file)
        else:
            with open(f'combined-ocr/{newspaper}_{location}_{date}.txt', 'a') as save_file:
                print(text, file=save_file)
                
num_issues = len(glob('combined-ocr/*.txt'))
print('\nTotal number of combined newspaper issues: ', num_issues)
if len(newsdict) == num_issues:
    print('Everything looks okay!')
else: 
    print('Brian, we have a problem!')
print('\nTime elapsed: ', datetime.now() - startTime)    


"""
for each in test:
    filename = get_filename(each)
    newspaper, date, page = filename.split('_')
    with open(each) as read_file:
        text = read_file.read()
        if page == 'p1':
            with open(f'combined-ocr/{newspaper}_{date}.txt', 'w') as save_file:
                print(text, file=save_file)
        else:
            with open(f'combined-ocr/{newspaper}_{date}.txt', 'a') as save_file:
                print(text, file=save_file)
"""
