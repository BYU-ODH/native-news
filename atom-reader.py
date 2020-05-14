#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 14 13:19:20 2020

@author: briancroxall

Script to manage the second portion of the data processing. This script will
open each result from harvesting-chronicling.py and compile its data into one
data dictionary.
"""
from datetime import datetime
from glob import glob
from bs4 import BeautifulSoup
import re

startTime = datetime.now()


def make_soup(xml):
    soup = BeautifulSoup(xml, 'lxml-xml')
    return soup


# Create output files
with open('data-dictionary.tsv', 'w') as save_file:
    pass

# Corpus
data = glob('atom-data/*.xml')

# Process data
for counter, each in enumerate(data):
    if counter % 100 == 0:
        print('.', end='', flush=True)
    with open(each) as data_file:
        soup = make_soup(data_file)
        entries = []
        for each in soup.find_all('entry'):
            entries.append(each)
        for entry in entries:
            link = entry.find('link').get('href')
            ocr = link + 'ocr/'
            date = link.split('/')[5]
            img_num = link.split('/')[7]
            title_tag = entry.find('title').get_text()
            location = re.findall(r'\((.*?)\)', title_tag, flags=re.I)[0]  # https://regex101.com/r/e5WQw8/1
            newspaper = re.findall(r'(.*?)\.\s', title_tag, flags=re.I)[0]  # https://regex101.com/r/e5WQw8/2
            with open('data-dictionary.tsv', 'a') as save_file:
                print(newspaper, date, img_num, link, ocr, sep='\t',
                      file=save_file)

print('Time elapsed: ', datetime.now() - startTime)
