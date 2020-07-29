# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 21:48:41 2020

@author: qtckp
"""





from sklearn.linear_model import LogisticRegression

with open('cleaned.txt','r') as f:
    #lines = [line.split() for line in f.readlines()]
    lines = [line.strip() for line in f.readlines()]





from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression

sklearn_pipeline = Pipeline((('vect', TfidfVectorizer(tokenizer=tokenize_text_simple_regex,
                                                      max_df=MAX_DF,
                                                      min_df=MIN_COUNT)),
                             ('cls', LogisticRegression())))
sklearn_pipeline.fit(train_source['data'], train_source['target']);




