#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 11:49:10 2018

@author: ciobanutudor
"""

import matplotlib.pyplot as plt
import numpy as np
from data_load import dataLoad

def dataPlot(data):
    # Number of bacteria
    bacteria = np.array(["Salmonella enterica", "Bacillus cereus", "Listeria", "Brochothrix thermosphacta"])
    numberOfBact = np.array([],dtype = int)
    for i in range(len(bacteria)):
        bact = np.where(data[:,2] == bacteria[i])
        numberOfBact = np.append(numberOfBact, len(data[:,2][bact])) 
    colors = ['red','blue','green','yellow']
    plt.bar(np.array(['1','2','3','4']), numberOfBact, color = colors, edgecolor='black')
    plt.xlabel('Bacterias')
    plt.ylabel('Nr. of Bacterias')
    plt.title('Number of bacterias')
    plt.legend(bacteria)
    plt.show()
    # Growth rate by temperature
    
data = dataLoad('test.txt')
dataPlot(data)