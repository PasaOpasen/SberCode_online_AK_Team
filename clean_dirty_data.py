# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 19:59:27 2020

@author: qtckp
"""

import os
from os import listdir
from os.path import isfile, join
import csv

dr = os.path.dirname(__file__)
bad_chars = """(){}<>"._ '-"""

data_path = join(dr, 'data')

dirty_data_path = join(data_path, 'dirty_data')
useful_data_path = join(data_path, 'useful_data')


appstore_path = join(dirty_data_path, 'AppStore.csv')

googleplay_paths = [join(dirty_data_path,'Google Play', f) for f in listdir(join(dirty_data_path,'Google Play')) if isfile(join(dirty_data_path,'Google Play', f))]

how_many = 0


for i, google in enumerate(googleplay_paths):
    
    #with open( google, 'r', encoding = 'utf-16') as file:
    #    lines = [' '.join(line.split(',')[10:12]) for line in file]
    
    lines = []
    with open( google, 'r', encoding = 'utf-16') as file:
        reader = csv.reader(file, delimiter=',')
        for row in reader:
            lines.append(' '.join(row[10:12]))
    
    tot = [line.replace('\n',' ').strip(bad_chars) + '\n' for line in lines[1:] if line.strip()]
    how_many += len(tot)
    
    with open(join(useful_data_path, f'google {i+1}.txt'), 'w', encoding = 'utf-16') as file:
        file.writelines(tot)





lines = []
with open(appstore_path, 'r', encoding = 'utf-8') as file:
    reader = csv.reader(file, delimiter=',')
    for row in reader:
        lines.append(' '.join(row[7:9]))

tot = [line.replace('\n',' ').strip(bad_chars) + '\n' for line in lines[1:] if line.strip()]
how_many += len(tot)
    
with open(join(useful_data_path, f'appstore.txt'), 'w', encoding = 'utf-16') as file:
    file.writelines(tot)
    
    
   
    
if True:
   lines = []
   for i, google in enumerate(googleplay_paths):
    
       with open(join(useful_data_path, f'google {i+1}.txt'), 'r', encoding = 'utf-16') as file:
           lines += file.readlines()
   
   with open(join(useful_data_path, f'appstore.txt'), 'r', encoding = 'utf-16') as file:
       lines += file.readlines()
       
   with open(join(useful_data_path, f'all.txt'), 'w', encoding = 'utf-16') as file:
       file.writelines(lines)
    
    
    
    
    
    
    
    
    