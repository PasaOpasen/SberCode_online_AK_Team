# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 22:42:14 2020

@author: qtckp
"""




with open('cleaned_grams.txt','r') as f:
    #lines = [line.split() for line in f.readlines()]
    lines = [line.strip() for line in f.readlines()]



# https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.CountVectorizer.html
from sklearn.feature_extraction.text import CountVectorizer

vectorizer = CountVectorizer()

X = vectorizer.fit_transform(lines)

vectorizer.get_feature_names()


# most popular words

d = dict(zip(vectorizer.get_feature_names(), X.sum(axis=0).tolist()[0]))

d = {k:v for k, v in sorted(d.items(), key=lambda item: item[1], reverse = True)}

k = 0

for word, count in d.items():
    print(f'{word}: {count}')
    k += 1
    if k == 20:
        break
    
print(f'total words: {sum(d.values())}, unique: {len(d)}') 


import matplotlib.pyplot as plt

plt.hist(d.values(), log = True, bins = 150, color = 'green')
plt.title('Histogram of word counts')

plt.show()    
    


with open('not deleted words.txt','r', encoding = 'utf-8') as f:
    not_del = [line.rstrip() for line in f if len(line) > 1]
    not_del = set(not_del)


total_vocab = {k: v for k, v in d.items() if (v > 100 and v < 1500) or k in not_del }
print(f'total words: {sum(total_vocab.values())}, unique: {len(total_vocab)}') 



import json

with open('total_voc.json','w') as f:
    json.dump(total_vocab,f, indent = 4)









