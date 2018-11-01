#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 23:34:08 2018

@author: ciobanutudor
"""

import numpy as np
from data_load import dataLoad
from data_statististics import dataStatistics
from data_graph import dataPlot
from data_load import is_number

dataLoaded = False
bacterias = np.array(["Salmonella enterica", "Bacillus cereus", "Listeria", "Brochothrix thermosphacta"])
statistics = np.array(["Mean Temperature", "Mean Growth rate", "Std Temperature", "Std Growth rate", 
                           "Rows", "Mean Cold Growth rate", "Mean Hot Growth rate"])
dataFiltered = np.array([False, False])
fullData = None
currentData = None

def printMenu():
    print("\nMenu:")
    print("1. Load data.")
    print("2. Filter data.")
    print("3. Display statistics.")
    print("4. Generate plots.")
    print("5. Quit.")
    choice = raw_input("Please type in the number of the operation you would like to perform:  ")
    return choice

def printFilterMenu():
    print("\nFilter Menu:")
    print("1. Filter bacterias.")
    print("2. Range filter for Growth rate.")
    print("3. Unfilter the data.")
    print("4. Back to main menu.")
    choice = raw_input("Please type in the number of the operation you would like to perform:  ")
    return choice

def printBacteriaMenu():
    print("\n")
    for i in range(len(bacterias)):
            print(str(i+1) + ". " + bacterias[i] + ".")
    print("5. Back to filter menu.")
    choice = raw_input("Please type in the number of the operation you would like to perform:  ")
    return choice

def printActiveFilter():
    if (dataFiltered[0] == True):
        print("\nWarning! Bacteria filter is active!")
    elif (dataFiltered[1] == True):
        print("\nWarning! Growth rate filter is active!")
    elif (dataFiltered[0] == True and dataFiltered[1] == True):
        print("\nWarning! Both Bacteria and Growth rate filters are active!")
    else:
        print("\nNo filter is active.")

def printStatisticsMenu():
    print("\nStatistics Menu:")
    for i in range(len(statistics)):
        print(str(i+1) + ". " + statistics[i] + ".")
    print("8. Back to main menu.")
    choice = raw_input("Please type in the number of the operation you would like to perform:  ")
    return choice
    

print('Welcome to Bacteria Analysis interactive program!')
choice = printMenu()
 
active = True
while(active):
    if choice == "1":
        filename = raw_input("Type in the name of the file you would like to use:  ")
        possibleData = dataLoad(filename)
        while(np.size(possibleData) == 0):
            answer = raw_input("Do you want to try again? Type in yes or no:  ")
            if (answer.lower() == "yes"):
                filename = raw_input("Type in the name of the file you would like to use:  ")
                possibleData = dataLoad(filename)
            elif (answer.lower() == "no"):
                choice = printMenu()
                break
        if (np.size(possibleData) > 0):
            dataLoaded = True
            fullData = possibleData
            currentData = fullData
            print("\nData loaded successfully!\n")
            choice = printMenu()
    elif choice == "2":
        printActiveFilter()
        if (dataLoaded == True):
            answer = printFilterMenu()
            runningFilter = True
            while (runningFilter == True):
                if answer == "1":
                    bacteriaChoice = printBacteriaMenu()
                    runningBacteriaFilter = True
                    while(runningBacteriaFilter):
                        if (dataFiltered[0] == True and dataFiltered[1] == True):
                            bacteriaFound = False
                            print("An existing filter for both bacteria and growth rate already exists.")
                            print("By changing the bacteria filter, the exisiting growth rate filter will be removed.")
                            confirmation = raw_input("Do you want to continue? Type in yes to confirm. Any other input will be disregarded and you will be taken to the main menu.  ")
                            if (confirmation == "yes"):
                                for i in range(len(bacterias)):
                                    if (int(bacteriaChoice)-1 == i):
                                        indices = np.where(fullData[:,2] == bacterias[i])
                                        currentData = fullData[indices]
                                        bacteriaFound = True
                                        dataFiltered[0] = True
                                        dataFiltered[1] = False
                                        print("\nBacteria filter successfully added.")
                                        runningBacteriaFilter = False
                                        runningFilter = False
                                        choice = printMenu()
                                        break
                                if (bacteriaFound == False):
                                    print("\nUnknown command. Please try again.")
                                    bacteriaChoice = printBacteriaMenu()
                            else:
                                runningBacteriaFilter = False
                                runningFilter = False
                                choice = printMenu()
                        else:
                            bacteriaFound = False
                            for i in range(len(bacterias)):
                                if (int(bacteriaChoice)-1 == i):
                                    indices = np.where(fullData[:,2] == bacterias[i])
                                    currentData = fullData[indices]
                                    bacteriaFound = True
                                    dataFiltered[0] = True
                                    print("\nBacteria filter successfully added.")
                                    runningBacteriaFilter = False
                                    runningFilter = False
                                    choice = printMenu()
                                    break
                            if (bacteriaFound == False):
                                print("\nUnknown command. Please try again.")
                                bacteriaChoice = printBacteriaMenu()
                elif answer == "2": 
                    lowerBound = raw_input("Please input the lower bound:  ")
                    upperBound = raw_input("Please input the upper bound:  ")
                    runningGrowthFilter = True
                    while(runningGrowthFilter):
                        if (is_number(lowerBound, "float") and is_number(upperBound, "float")):
                            difference = float(upperBound) - float(lowerBound)
                            if (difference > 0 and difference < 1):
                                growthRates = currentData[:,1].astype(np.float)
                                indices = np.array([], dtype = int)
                                for i in range(len(growthRates)):
                                    if (growthRates[i] >= float(lowerBound) and growthRates[i] <= float(upperBound)):
                                        indices = np.append(indices, i)
                                currentData = currentData[indices]
                                dataFiltered[1] = True
                                print("\nGrowth rate filter successfully added.")
                                runningGrowthFilter = False
                                runningFilter = False
                                choice = printMenu()
                            elif (difference < 0):
                                print("Invalid values for upper and lower bounds. The lower bound cannot be bigger or equal to the upper bound!")
                                confirmation = raw_input("Would you want to try again? Type in yes to confirm. Any other input will be disregarded and you will be taken to the main menu.  ")
                                if (confirmation == "yes"):
                                    lowerBound = raw_input("Please input the lower bound:  ")
                                    upperBound = raw_input("Please input the upper bound:  ")
                                else:
                                    runningGrowthFilter = False
                                    runningFilter = False
                                    choice = printMenu()
                        else:
                            print("Please type in integers for both the lower and upper bound!")
                            confirmation = raw_input("Would you want to try again? Type in yes to confirm. Any other input will be disregarded and you will be taken to the main menu.   ")
                            if (confirmation == "yes"):
                                lowerBound = raw_input("Please input the lower bound:  ")
                                upperBound = raw_input("Please input the upper bound:  ")
                            else:
                                runningGrowthFilter = False
                                runningFilter = False
                                choice = printMenu()
                elif answer == "3":
                    runningFilter = False
                    currentData = fullData
                    dataFiltered[0] = False
                    dataFiltered[1] = False
                    print("\nFilter removed successfully!\n")
                    choice = printMenu()
                elif answer == "4":
                    runnningFilter = False
                    choice = printMenu()
                else:
                    print("\nUnkown command. Please try again.") 
                    answer = printFilterMenu()
        else:
            print("\nData is not loaded yet! Please load the data first!")
            choice = printMenu()
    elif (choice == "3"):
        if (dataLoaded == True):
            printActiveFilter()
            answer = printStatisticsMenu()
            result = 0
            runningStatistics = True
            statisticsFound = False
            while(runningStatistics):
                if (is_number(answer, "int") and answer != "8"):
                    for i in range(len(statistics)):
                        if (int(answer)-1 == i):
                            result = dataStatistics(currentData, statistics[i])
                            print(str(statistics[i]) + ": " + str(result))
                            runningStatistics = False
                            statisticsFound = True
                            choice = printMenu()
                            break
                if (answer == "8"):
                    runningStatistics = False
                    statisticsFound = True
                    choice = printMenu()
                elif (statisticsFound == False):
                    print("\nUnkown command. Please try again.") 
                    answer = printStatisticsMenu()
        else:
            print("\nData is not loaded yet! Please load the data first!")
            choice = printMenu()
    elif (choice == "4"):
        if (dataLoaded == True):
            printActiveFilter()
            dataPlot(currentData)
            choice = printMenu()
        else:
            print("\nData is not loaded yet! Please load the data first!")
            choice = printMenu()
    elif (choice == "5"):
        print("\nThank you for using Bacteria Analysis interactive program!")
        active = False
    else:
        print("\nUnkown command. Please try again.")
        choice = printMenu()
                                    
                            
                    
                    
            
        