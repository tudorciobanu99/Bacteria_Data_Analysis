#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 11:49:10 2018

@author: ciobanutudor
"""

import matplotlib.pyplot as plt
import numpy as np

def dataPlot(data):
    
    # Number of bacteria plot
    # This array holds the possible names for bacterias
    bacteria = np.array(["Salmonella enterica", "Bacillus cereus", "Listeria", "Brochothrix thermosphacta"])

    # This array will eventually contain all the types of bacterias present in the data given. It will also be eventually used as the x-axis.
    bacteriaAxis = np.array([])

    # This empty array will eventually hold the number of each type of bacteria. It will also be eventualy used as the y-axis.
    numberOfBact = np.array([],dtype = int)

    for i in range(len(bacteria)):
        bact = np.where(data[:,2] == bacteria[i])
        if (len(data[:,2][bact]) > 0):    # if there is 0 bacterias of a specific type, it won't be included in the numberOfBact and bacteriaAxis arrays
            numberOfBact = np.append(numberOfBact, len(data[:,2][bact]))
            bacteriaAxis = np.append(bacteriaAxis, bacteria[i])


    ax1 = plt.subplot()
    ax1.bar(bacteriaAxis, numberOfBact, color = 'g', label = bacteria) # y-values: number of each type of bacteria, x-values: the name for the bacterias
    ax1.set_xticklabels(bacteriaAxis, rotation = 45)  # rotation = 45 means that the x-values are going to be displayed with a 45 degree anti-clockwise shift from the horizontal position
    plt.xlabel('Bacterias')
    plt.ylabel('Nr. of Bacterias')
    plt.title('Number of bacterias')
    plt.show(block=True) # makes possible the visualization of the plot when executing the main script from the command line


    # Growth rate by temperature
    ax2 = plt.subplot()
    colors = np.array(['green', 'red', 'blue', 'magenta'])  # An array that holds the 4 colors that could be used for this plot
    for i in range(len(bacteria)):
        bact = np.where(data[:,2] == bacteria[i])
        if (len(data[:,2][bact]) > 0):   # if there is 0 bacterias of a specific type, it won't be included in the plot
            temperature = data[:,0][bact].astype(np.float)
            growth_rate = data[:,1][bact].astype(np.float)
            ax2.scatter(temperature, growth_rate, color = colors[i], label = bacteria[i], marker = 'x')
            plt.xlim(10,60)   # setting x limits
            plt.ylim(ymin = 0)  # setting y limits
    ax2.legend()
    plt.xlabel('Temperature')
    plt.ylabel('Growth rate')
    plt.title('Growth rate by temperature')
    plt.show(block=True)
