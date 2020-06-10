#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 13:39:44 2020

@author: briancroxall

Script to visualize search results from native news.
"""

import os
# from matplotlib import pyplot as plt

if not os.path.isdir('images'):
    os.mkdir('images')

with open('search-results.tsv') as file:
    for line in file:
        filename = line.split('\t')[0]
        newspaper = line.split('\t')[1]
        location = line.split('\t')[2]
        date = line.split('\t')[3]
        wk_hits = line.split('\t')[4]
        pr_hits = line.split('\t')[14]
        gd_hits = line.split('\t')[22]
        
