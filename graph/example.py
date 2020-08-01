# -*- coding: utf-8 -*-
"""
Created on Sat Aug  1 13:01:34 2020

@author: qtckp
"""


import sys, os, io
sys.path.append(os.path.dirname('../'))

from graph.content_detector.detector import get_content_from_text



if __name__=='__main__':
    
    
    lines = ['обратная связь']
    
    print(get_content_from_text(lines))
    
    