# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 21:40:16 2020

@author: qtckp
"""


import re

import Stemmer
stemmer = Stemmer.Stemmer('russian')

TOKEN_RE = re.compile(r'[\w\d-]+')

rep_symb = [('ё', 'е')]

def replacor(txt):
    return txt.replace(rep_symb[0][0], rep_symb[0][1])


def tokenize_text_simple_regex(txt, min_token_size = 2):
    all_tokens = TOKEN_RE.findall(txt.lower())
    return [token for token in all_tokens if len(token) >= min_token_size]


def tokenize_text_simple_regex_stemming(txt, min_token_size = 2):
    all_tokens = TOKEN_RE.findall(replacor(txt.lower()))
    return [stemmer.stemWord(token) for token in all_tokens if len(token) >= min_token_size]


def delete_bad_words(txt, words):
    return ' '.join([word for word in txt.split() if word not in words])


# clean text

with open('Том 5.txt','r') as f:
    lines = f.readlines()


with open('cleaned.txt', 'w') as f:
    tocs = [' '.join(tokenize_text_simple_regex_stemming(line)) for line in lines]
    f.writelines([toc + '\n' for toc in tocs if toc])


# replace with ngrams

with open('cleaned.txt','r') as f:
    lines = f.readlines()

with open('grams.txt','r') as f:
    grams = [line.rstrip() for line in f.readlines()]
    grams = {' '.join(g.split('_')): ''.join(g.split('_')) for g in grams}

def rep_grams(txt):
    for k in grams.keys():
        txt = txt.replace(k, grams[k])
    return txt

    
with open('cleaned_grams.txt', 'w') as f:
    for line in lines:
        f.write(rep_grams(line))
    
    
    


# delete some words

with open("total_voc.json", "r") as read_file:
    total_voc = json.load(read_file)        
        
        
    
    
    
    
    
    
    
    
    
    
    

