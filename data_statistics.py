#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 11:07:49 2018

@author: marinanocera
"""

import numpy as np

# This is a function which calculates various statistics based on some given data.
def dataStatistics(data, statistic):
    
    # An array which contains all the possible statistics that can be calculated on the given data.
    statistics = np.array(["Mean Temperature", "Mean Growth rate", "Std Temperature", "Std Growth rate", 
                           "Rows", "Mean Cold Growth rate", "Mean Hot Growth rate"])
    
    if (statistic == statistics[0]):
        result = np.average(data[:,0].astype(np.float))  
    elif (statistic == statistics[1]):
        result = np.average(data[:,1].astype(np.float))
    elif (statistic == statistics[2]):
        result = np.std(data[:,0].astype(np.float)) 
    elif (statistic == statistics[3]):
        result = np.std(data[:,1].astype(np.float))  
    elif (statistic == statistics[4]):
        result = np.size(data, 0)      
    elif (statistic == statistics[5]):
        indices = np.where((data[:,0]).astype(np.float) < 20)  # This array holds the indices for the lines which contain a temperature less than 20 degrees.
        result = np.average(data[:,1][indices].astype(np.float), axis = 0)
    elif (statistic == statistics[6]):
        indices = np.where((data[:,0]).astype(np.float) > 50)  # This array holds the indices for the lines which contain a temperature more than 20 degrees.
        result = np.average(data[:,1][indices].astype(np.float), axis = 0)       
    return result
