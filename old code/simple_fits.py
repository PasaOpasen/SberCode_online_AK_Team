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
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import make_moons, make_circles, make_classification
from sklearn.neural_network import MLPClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.svm import LinearSVC
from sklearn.gaussian_process import GaussianProcessClassifier
from sklearn.gaussian_process.kernels import RBF
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis, LinearDiscriminantAnalysis
from sklearn.metrics import classification_report
from sklearn.linear_model import SGDClassifier
from sklearn import linear_model
from sklearn.metrics import f1_score
import sklearn
import numpy as np
from scipy import sparse


X = sparse.load_npz(f'X3955_train.npz')
y = sparse.load_npz(f'Y.npz')



models = [
    ("Nearest Neighbors", KNeighborsClassifier(5)),
    ("Linear SVM",LinearSVC(C=1,verbose=1)),
    ("RBF SVM",SVC(gamma=2, C=1,verbose=True)),
    ('poly svm',SVC(kernel='poly')),
    ('sigmoid svm',SVC(kernel='sigmoid')),
    ('sgd',SGDClassifier()),
    ("Decision Tree",DecisionTreeClassifier(max_depth=3)),
    ("Random Forest",RandomForestClassifier(max_depth=5, n_estimators=10, max_features=1,verbose=True)),
    ("Neural Net",MLPClassifier(alpha=1, max_iter=1000,verbose=True)),
    ("AdaBoost",AdaBoostClassifier()),
    ("Naive Bayes gau",GaussianNB()),
    ("LDA",LinearDiscriminantAnalysis()),
    ("QDA",QuadraticDiscriminantAnalysis()),
    ('logreg',LogisticRegression()),
    ('ridge', linear_model.RidgeClassifier(alpha=0.1)),
    ('Grad Boost',sklearn.ensemble.GradientBoostingClassifier())
    ]




X_train, X_test, y_train, y_test =  train_test_split(X.toarray(), y, test_size=.2, train_size=.01, shuffle = True )



for name, clf in models:
    print('Now: {}'.format(name))
    f1s = []
    for i in range(620):
        clf.fit(X_train, y_train[:,i].toarray().flatten())
        #score = clf.score(X_test, y_test[:,i])
        print(clf.score(X_test, y_test[:,i].toarray().flatten()))
        v = f1_score(y_test[:,i].toarray().flatten(), clf.predict(X_test))
        print(v)
        f1s.append(v)
        #print(classification_report(y_test, clf.predict(X_test), digits = 7))
    print("model = {}  score = {}".format(name,np.mean(f1s)))






sklearn_pipeline = Pipeline((('vect', TfidfVectorizer(tokenizer=tokenize_text_simple_regex,
                                                      max_df=MAX_DF,
                                                      min_df=MIN_COUNT)),
                             ('cls', LogisticRegression())))
sklearn_pipeline.fit(train_source['data'], train_source['target']);




