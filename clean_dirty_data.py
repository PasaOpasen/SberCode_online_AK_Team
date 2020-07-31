# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 19:59:27 2020

@author: qtckp
"""

import os
from os import listdir
from os.path import isfile, join

dr = os.path.dirname(__file__)


data_path = join(dr, 'data')

dirty_data_path = join(dr, 'dirty_data')


appstore_path = join(dirty_data_path, 'AppStore.csv')

googleplay_paths = [f for f in listdir(join(dirty_data_path,'Google Play')) if isfile(join(dirty_data_path,'Google Play', f))]








