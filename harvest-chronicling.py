#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 13 14:26:28 2020

@author: briancroxall

Script to harvest targeted data from Chronicling America website,
https://chroniclingamerica.loc.gov/about/api/#search.
"""
import os
import requests as r
from bs4 import BeautifulSoup 
import re


def make_soup(xml):
    soup = BeautifulSoup(xml, 'lxml-xml')
    return soup


# Create directories
if not os.path.isdir('data'):
    os.mkdir('data')

# Create list of all pages needed
stem_url = 'https://chroniclingamerica.loc.gov/search/pages/results/?dateFilterType=range&date1=11%2F01%2F1890&date2=03%2F31%2F1891&format=atom&page='  # noqa E501
pages = range(1, 3839)

indices = []

for each in pages:
    indices.append(stem_url + str(each))


test = 'https://chroniclingamerica.loc.gov/search/pages/results/?dateFilterType=range&date1=11%2F01%2F1890&date2=03%2F31%2F1891&format=atom&page1'  #noqa: E501

# Download and save test data
print('Starting atom file download...')
headers1 = {'user-agent': 'Brian Croxall (brian.croxall@byu.edu)'}  # noqa: E501 identify self
data = r.get(test, headers=headers1)
with open('data/test.xml', 'w') as data_file:
    print(data.text, file=data_file)
print('Atom files downloaded.\n')


# Create output file for test data
with open('data-dictionary.tsv', 'w') as save_file:
    pass

# Process test data
with open('data/test.xml') as data_file:
    soup = make_soup(data_file)
    entries = []
    for each in soup.find_all('entry'):
        entries.append(each)
    for entry in entries:
        link = entry.find('link').get('href')
        date = link.split('/')[5]
        img_num = link.split('/')[7]
        title_tag = entry.find('title').get_text()
        location = re.findall(r'\((.*?)\)', title_tag, flags=re.I)[0]  # https://regex101.com/r/e5WQw8/1
        newspaper = re.findall(r'(.*?)\.\s', title_tag, flags=re.I)[0]  # https://regex101.com/r/e5WQw8/2
        with open('data-dictionary.tsv', 'a') as save_file:
            print(newspaper, date, img_num, link, sep='\t', file=save_file)