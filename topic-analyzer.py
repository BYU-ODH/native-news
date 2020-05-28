#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 28 10:13:04 2020

@author: briancroxall
"""

def get_news_date(file):
    file = indices [1]
    filename = file.split('/')[-1]
    no_ext = filename.split('.')[0]
    newspaper, date = no_ext.split('_')
    return (newspaper, date)


def cast_date(date):
    #  This function casts the dates to ints
    year, month, day = date.split('-')
    year = int(year)
    month = int(month)
    day = int(day)
    return (year, month, day)


with open('topic-modeling/corp_stop_removed_100tops_comp.txt') as results:
    for line in results:
        indices = line.split('\t')
        newspaper, date = get_news_date(indices)
        year, month, day = cast_date(date)