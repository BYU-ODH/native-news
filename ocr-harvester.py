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

# Directories
if not os.path.isdir('ocr-data'):
    os.mkdir('ocr-data')

newspapers = set()

with open('data-dictionary.tsv') as data_file:
    for counter, line in enumerate(data_file):
        if counter % 100 == 0:
            print('.', end='', flush=True)
        # if counter > 4:
        #     continue
        # else:
        newspaper, date, img_num, link, ocr_link = line.split('\t')
        newspapers.add(newspaper)

with open('newspapers.txt', 'w') as file:
    pprint(newspapers, stream=file)
        



print('Time elapsed: ', datetime.now() - startTime)