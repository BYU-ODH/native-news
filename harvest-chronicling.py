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



# Create list of all pages needed
stem_url = 'https://chroniclingamerica.loc.gov/search/pages/results/?dateFilterType=range&date1=11%2F01%2F1890&date2=03%2F31%2F1891&format=atom&page='  # noqa E501
pages = range(1, 3839)

indices = []

for each in pages:
    indices.append(stem_url + str(each))


test = 'https://chroniclingamerica.loc.gov/search/pages/results/?dateFilterType=range&date1=11%2F01%2F1890&date2=03%2F31%2F1891&format=atom&page1'

