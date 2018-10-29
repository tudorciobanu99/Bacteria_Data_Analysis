#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 14:30:52 2018

@author: ciobanutudor
"""
import numpy as np
import time

# This is a function which checks if a string s can be parsed into a number, specifically a float or an integer.
# A string kind specifies if the string s should be parsed to a integer or a float.

def is_number(s, kind):
    try:
        if (kind == "int"):
            int(s)
        elif (kind == "float"):
            float(s)
        return True
    except ValueError:
        return False

# This is a function which reads a file with a given file name and loads all the valid lines in an N x 3 matrix.
def dataLoad(filename):
    
    # This empty array will eventually store all the valid lines from the file.
    data = np.empty(shape = [0, 3])
    
    # This array contains the four possible types of bacteria.
    bacteria = np.array(["Salmonella enterica", "Bacillus cereus", "Listeria", "Brochothrix thermosphacta"])
    
    try:
        # Opening the file for reading.
        fileIn = open(filename, "r")
            
        # Reading all the lines from the file.
        lines = fileIn.readlines()
            
        # A loop that filters out the erroreous lines.
        for i in range(len(lines)):
                
            # Each line is split in three parts: the temperature, growth rate and the bacteria type.
            values = lines[i].split()
            temp = values[0]
            growthRate = values[1]
            bactType = values[2]
            
            # This variable will store the message of the errors. It is initialized as an empty string.
            error = ""
            
            if is_number(temp, "float") == False or (is_number(temp, "float") and (float(temp) < 10 or float(temp) > 60)):
                error += "\nError in line " + str(i) + ". The Temperature must be a number between 10 and 60 but value was: " + str(temp) + "."
            if is_number(growthRate, "float") == False or (is_number(growthRate, "float") and float(growthRate) < 0):
                error += "\nError in line " + str(i) + ". The Growth rate must be a positive number but value was: " + str(growthRate) + "."
            if is_number(bactType, "int") == False or (is_number(bactType, "int") and (int(bactType) < 1 or int(bactType) > 4)):
                error += "\nError in line " + str(i) + ". The Bacteria must be an integer between 1 and 4 but value was: " + str(bactType) + "."
            else:
                bactType = bacteria[int(bactType)-1] # This variable will now hold the actual name of the bacteria, instead of its respective code digit.
            if error == "":
                line = np.array([temp, growthRate, bactType]) # This array holds the final temperature, growth rate and bacteria type.
                data = np.vstack([data, line]) # The array is then stacked on top of the last row of the data matrix.
            else:
                print(error)
                time.sleep(2) # The execution is paused for 2 seconds, so that the user can read the error messages.
    except IOError:
        print("Unable to open the file with the following name: " + filename + "! Please try again with a different filename! ")
    return data

dataLoad('test.txt')
