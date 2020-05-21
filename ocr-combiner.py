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
    no_ext = no_dir.split('.')[0]
    return no_ext


# Corpus
corpus = sorted(glob('ocr-txt/*.txt'))
test = ['/Users/briancroxall/Documents/github/native-news/ocr-txt/deseret-evening-news_1890-11-28_p1.txt',
        '/Users/briancroxall/Documents/github/native-news/ocr-txt/deseret-evening-news_1890-11-28_p2.txt',
        '/Users/briancroxall/Documents/github/native-news/ocr-txt/deseret-evening-news_1890-11-28_p3.txt',
        '/Users/briancroxall/Documents/github/native-news/ocr-txt/deseret-evening-news_1890-11-28_p4.txt']
test2 = ['/Users/briancroxall/Documents/github/native-news/ocr-txt/deseret-evening-news_1890-11-28_p1.txt',
        '/Users/briancroxall/Documents/github/native-news/ocr-txt/deseret-evening-news_1890-11-28_p2.txt',
        '/Users/briancroxall/Documents/github/native-news/ocr-txt/deseret-evening-news_1890-11-28_p3.txt',
        '/Users/briancroxall/Documents/github/native-news/ocr-txt/deseret-evening-news_1890-11-28_p4.txt',
        '/Users/briancroxall/Documents/github/native-news/ocr-txt/the-comet_1891-03-12_p1.txt',
        '/Users/briancroxall/Documents/github/native-news/ocr-txt/the-comet_1891-03-12_p2.txt',
        '/Users/briancroxall/Documents/github/native-news/ocr-txt/the-comet_1891-03-12_p3.txt',
        '/Users/briancroxall/Documents/github/native-news/ocr-txt/the-comet_1891-03-12_p4.txt']

# Directories
if not os.path.isdir('combined-ocr'):
    os.mkdir('combined-ocr')

# Dictionaries
newsdict = defaultdict(list)


# Build dictionary
for each in corpus:
    filename = get_filename(each)
    newspaper, date, page = filename.split('_')
    try:
        newsdict[(newspaper, date)].append(page)
    except KeyError:
        newsdict[(newspaper, date)] = []
        
print('Dictionary built')
print('Expected number of newspaper issues: ', len(newsdict))

print('\nStarting to combine texts')
for (newspaper, date), pages in newsdict.items():
    for page in pages:
        with open(f'ocr-txt/{newspaper}_{date}_{page}.txt') as ocr:
            text = ocr.read()
        if page == 'p1':
            with open(f'combined-ocr/{newspaper}_{date}.txt', 'w') as save_file:
                print(text, file=save_file)
        else:
            with open(f'combined-ocr/{newspaper}_{date}.txt', 'a') as save_file:
                print(text, file=save_file)
                
num_issues = len(glob('combined-ocr/*.txt'))
print('\nTotal number of newspaper issues combined: ', num_issues)
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
