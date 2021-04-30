""" Style Guide 
    Penggantian
"""

# cara melakukan import yang direkomendasikan
import pandas 
import numpy
from sklearn.svm import SVC

# tidak direkomendasikan
import os, math

# Penulisan operator binary gabungan
minimum_wages = 0
bonus = 0
working_day = 0
meals = 0
paid_off = 0

salary = (minimum_wages
        + bonus
        + (working_day * meals)
        - paid_off
) 