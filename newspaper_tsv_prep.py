#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 28 12:28:37 2020

@author: briancroxall

A quick script to create a TSV of newspapers in the data set.
"""

with open('newspaper_locations.tsv', 'w') as save_file:
    print('newspaper', 'city', 'state', sep='\t', file=save_file)

with open('newspapers.txt') as data:
    for line in data:
        string = line.lstrip().rstrip()
        newspaper = string.replace('\'', '')
        newspaper = newspaper.replace('{', '')
        newspaper = newspaper.replace('}', '')
        newspaper = newspaper.replace(',', '')
        with open('newspaper_locations.tsv', 'a') as save_file:
            print(newspaper, file=save_file)