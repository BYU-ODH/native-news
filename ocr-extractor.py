#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 15 12:43:56 2020

@author: briancroxall

This script extracts the OCR text from the HTML from Chronicling America.
"""

from glob import glob
from bs4 import BeautifulSoup


def make_soup(xml):
    soup = BeautifulSoup(xml, 'lxml-xml')
    return soup

corpus = sorted(glob('ocr-html/*.html'))
test = ['ocr-html/the-republican-journal_1890-12-04_p2.html',
        'ocr-html/st_1891-03-19_p8.html',
        'ocr-html/the-state-republican_1891-02-26_p3.html']


