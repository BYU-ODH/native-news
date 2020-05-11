#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 11 13:51:17 2020

@author: briancroxall

A script to extract the location of all the tar files from the Chronicling
America atom feed (https://chroniclingamerica.loc.gov/ocr/feed/).
"""

from bs4 import BeautifulSoup

"""
def make_soup(file):
    with open(file) as xml_file:
        soup = BeautifulSoup(xml_file, 'lxml-xml')
        return soup
"""


with open('tarfiles.txt', 'w') as file:
    pass

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