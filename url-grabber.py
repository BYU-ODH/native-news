#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 11 13:51:17 2020

@author: briancroxall

A script to extract the location of all the tar files from the Chronicling
America atom feed (https://chroniclingamerica.loc.gov/ocr/feed/). 

The firstversion of the script relied on an already downloaded copy of the atom
file.

The current version grabs the file from the CA website to ensure we are always
working with the most up-to-date information.
"""

from bs4 import BeautifulSoup
import requests as r

# Download and save data
headers1 = {'user-agent': 'Brian Croxall (brian.croxall@byu.edu)'}  # noqa: E501 identify self
data = r.get('https://chroniclingamerica.loc.gov/ocr/feed/', headers=headers1)
with open('chronicling-atom.txt', 'w') as data_file:
    print(data.text, file=data_file)

# create output file
with open('tarfiles.txt', 'w') as file:
    pass

# Counters
counter = 0
skip_counter = 0

with open('chronicling-atom.txt') as file:
    soup = BeautifulSoup(file, 'lxml-xml')
    for link in soup.find_all('link'):
        url = link.get('href')
        if url.endswith('bz2'):
            counter += 1
            with open('tarfiles.txt', 'a') as output:
                print(link.get('href'), file=output)
        else:
            skip_counter += 1
            continue

print('Number of tar files: ', counter)
print('Number of skipped links: ', skip_counter)

"""
    ids = soup.find_all('link')
    for counter, each in enumerate(ids):
        if counter < 6:
            print(each)
"""