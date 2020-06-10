#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 13:39:44 2020

@author: briancroxall

Script to visualize search results from native news.
"""

import os

if not os.path.isdir('images'):
    os.mkdir('images')

with open('search-results.tsv') as file:
    for line in file:
        
