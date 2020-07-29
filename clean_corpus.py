# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 21:40:16 2020

@author: qtckp
"""


import re

import Stemmer
stemmer = Stemmer.Stemmer('russian')


TOKEN_RE = re.compile(r'[\w\d]+')


def tokenize_text_simple_regex(txt, min_token_size = 2):
    all_tokens = TOKEN_RE.findall(txt.lower())
    return [token for token in all_tokens if len(token) >= min_token_size]


def tokenize_text_simple_regex_stemming(txt, min_token_size = 2):
    all_tokens = TOKEN_RE.findall(txt.lower())
    return [stemmer.stemWord(token) for token in all_tokens if len(token) >= min_token_size]


def delete_bad_words(txt, words):
    return ' '.join([word for word in txt.split() if word not in words])


with open('Том 5.txt','r') as f:
    lines = f.readlines()


with open('cleaned.txt', 'w') as f:
    tocs = [' '.join(tokenize_text_simple_regex_stemming(line)) for line in lines]
    f.writelines([toc + '\n' for toc in tocs if toc])

