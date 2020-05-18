#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 15 12:43:56 2020

@author: briancroxall

This script extracts the OCR text from the HTML from Chronicling America.
"""

from glob import glob
from bs4 import BeautifulSoup
import os
from datetime import datetime


startTime = datetime.now()


def make_soup(xml):
    soup = BeautifulSoup(xml, 'lxml-xml')
    return soup


def get_name(filename):
    no_dir = filename.split('/')[-1]
    no_ext = no_dir.split('.')[0]
    return no_ext


if not os.path.isdir('ocr-txt'):
    os.mkdir('ocr-txt')

corpus = sorted(glob('ocr-html/*.html'))
test = ['ocr-html/the-republican-journal_1890-12-04_p2.html',
        'ocr-html/st_1891-03-19_p8.html',
        'ocr-html/the-state-republican_1891-02-26_p3.html']

for counter, each in enumerate(test):
    if counter % 100 == 0:
        print('.', end='', flush=True)
    with open(each) as input_file:
        soup = make_soup(input_file)
        ocr = soup.div.p.get_text(' ')
        """
        ocr_tag = soup.div.p
        ocr = ocr_tag.get_text()
        """
        filename = get_name(each)
        with open(f'ocr-txt/{filename}.txt', 'w') as ocr_data:
            print(ocr, file=ocr_data)
        
print('\nNumber of OCR files extracted: ', counter + 1)

print('\nTime elapsed: ', datetime.now() - startTime)        
