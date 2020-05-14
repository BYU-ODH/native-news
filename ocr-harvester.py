#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 14 14:00:51 2020

@author: briancroxall

This script reads data-dictionary.tsv and uses its content to harvest OCR for
each newspaper page in our data set and saves it to the XXX directory.
"""

import requests as r
import time
from datetime import datetime
import os
from pprint import pprint


startTime = datetime.now()

# Declare identity
headers1 = {'user-agent': 'Brian Croxall (brian.croxall@byu.edu)'}

# Directories
if not os.path.isdir('ocr-data'):
    os.mkdir('ocr-data')

# Sets
newspapers = set()

with open('data-dictionary.tsv') as data_file:
    for counter, line in enumerate(data_file):
        if counter % 100 == 0:
            print('.', end='', flush=True)
        if counter > 4:
            continue
        else:
            newspaper, location, date, img_num, link, ocr_link = line.split('\t')
            newspapers.add(newspaper)  # add newspaper title to set before I lower and kebab case it
            newspaper = newspaper.lower().replace(' ', '-')
            img_num = img_num.replace('seq-', '')  # remove seq- from each page number
            time.sleep(0.25)
            ocr_data = r.get(ocr_link, headers=headers1)
            filename = f'{newspaper}_{date}_p{img_num}.html'
            with open(f'ocr-data/{filename}', 'w') as new_file:
                print(ocr_data.text, file=new_file)
        

with open('newspapers.txt', 'w') as file:
    pprint(newspapers, stream=file)

print('\nTime elapsed: ', datetime.now() - startTime)
