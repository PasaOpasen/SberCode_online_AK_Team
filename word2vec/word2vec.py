# -*- coding: utf-8 -*-
"""
Created on Sat Aug  1 01:44:33 2020

@author: qtckp
"""

from gensim.models import Word2Vec

with open('cleaned2984.txt', 'r', encoding = 'utf16') as f:
    lines = [line.rstrip().split() for line in f]


model = Word2Vec(lines, size=32, window=5, min_count=1, workers=8, iter = 10)

model.save("word2vec 32 5 10.model")



from sklearn.manifold import TSNE
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


vocab = list(model.wv.vocab)
X = model.wv[vocab]


tsne = TSNE(n_components = 2)
X_tsne = tsne.fit_transform(X)

df = pd.DataFrame(X_tsne, index=vocab, columns=['x', 'y'])


smpl = 150
t = np.random.choice(range(len(vocab)), smpl)
ddf = df.iloc[t]

fig = plt.figure(figsize=(6,6))
ax = fig.add_subplot(1, 1, 1)

ax.scatter(ddf['x'], ddf['y'])

for word, pos in ddf.iterrows():
    ax.annotate(word, pos)

plt.savefig('tsne.png', dpi = 350)
plt.show()



def display_pca_scatterplot(model, words=None, sample=0):
    if sample > 0:
        words = np.random.choice(words, sample)
        
    word_vectors = np.array([model.wv[w] for w in words])

    twodim = PCA().fit_transform(word_vectors)[:,:2]
    
    plt.figure(figsize=(6,6))
    plt.scatter(twodim[:,0], twodim[:,1], edgecolors='k', c='r')
    for word, (x,y) in zip(words, twodim):
        plt.text(x+0.05, y+0.05, word)
    plt.savefig('pca.png', dpi = 350)
    plt.show()


display_pca_scatterplot(model, vocab, 100)

