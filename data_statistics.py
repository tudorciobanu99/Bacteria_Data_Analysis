#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 16:32:45 2018

@author: ciobanutudor
"""
import numpy as np

def dataStatistics(data, statistic):
    possibleStatistics = np.array(['Mean Temperature', 'Mean Growth rate', 'Std Temperature',
                                   'Std Growth rate', 'Rows', 'Mean Cold Growth rate',
                                   'Mean Hot Growth rate'])
    result = 0
    
    if statistic == possibleStatistics[0]:
        result = np.average(data[:,0].astype(np.float), axis = 0)
    elif statistic == possibleStatistics[1]:
        result = np.average(data[:,1].astype(np.float), axis = 0)
    elif statistic == possibleStatistics[2]:
        result = np.std(data[:,0].astype(np.float), axis = 0)
    elif statistic == possibleStatistics[3]:
        result = np.average(data[:,1].astype(np.float), axis = 0)
    elif statistic == possibleStatistics[4]:
        result = np.size(data, 0)
    elif statistic == possibleStatistics[5]:
        indices = np.where(data[:,0].astype(np.float) < 20)
        result = np.average(data[:, 1][indices].astype(np.float), axis = 0)
    elif statistic == possibleStatistics[6]:
        indices = np.where(data[:,0].astype(np.float) > 50)
        result = np.average(data[:, 1][indices].astype(np.float), axis = 0)
    return result