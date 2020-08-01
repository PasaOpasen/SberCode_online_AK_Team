# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 14:20:22 2020

@author: qtckp
"""


import sys, os, io
sys.path.append(os.path.dirname('../'))

from content_detector.create_graph_dictionary import Graph
from content_detector.detector import get_content_from_text
import content_detector.stemmer_rus# import update_dictionary
import numpy as np


from termcolor import colored
import colorama

voc = None

def update_graph():
    print('updating...')
    Graph.update_graph()
    #update_dictionary()
    global voc
    voc = content_detector.stemmer_rus.get_stem_dictionary()




files = [f"C:/Users/qtckp/OneDrive/Рабочий стол/SberHak/data/useful_data/google {i}.txt" for i in range (1,14)]
appstore = "C:/Users/qtckp/OneDrive/Рабочий стол/SberHak/data/useful_data/appstore.txt"
with open(appstore,'r', encoding = 'utf-16') as f:
    lines = f.readlines()


inds = np.arange(len(lines))
np.random.shuffle(inds)


i=0

while i < inds.size:
    indx = inds[i]
    l1 = lines[indx]
    res1 = get_content_from_text([l1], voc)
    
    print(colored(f'key = {l1}', on_color = 'on_blue'))
    print(colored(f'groups = {res1}', on_color = 'on_green'))
    print()
    
    
    tmp = input('press + for continue and something else for reload: ')
    print()
    if tmp == '+':
        i +=1
    else:
        update_graph()
        print()
    
    

