#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 14:30:52 2018

@author: ciobanutudor
"""
import numpy as np

# This is a function which checks if a string s can be parsed into a number. A string kind specifies if
# the string s should be parsed to a integer or a float.
def is_number(s, kind):
    try:
        if (kind == "int"):
            int(s)
        elif (kind == "float"):
            float(s)
        return True
    except ValueError:
        return False

# This is a function which reads a file with a given file name and loads all the valid lines in a N x 3 matrix.
def dataLoad(filename):
    
    # Creating an array called data which will store all the valid lines from the file.
    data = np.empty(shape = [0, 3])
    
    # Array which contains all possible bacteria types.
    bacteria = np.array(["Salmonella enterica", "Bacillus cereus", "Listeria", "Brochothrix thermosphacta"])
    
    # Checking if a file with the specified name exists and can be read.
    try:
        
        # Opening the file for reading.
        fileIn = open(filename, "r")
        
        # Reading all the lines from the file.
        lines = fileIn.readlines()
        
        # Checking each line if it does not contain errors and appending each valid line to the data array.
        for i in range(len(lines)):
            
            # Each line is split in 3 values, which stand for the temperature, growth rate and bacteria type.
            values = lines[i].split()
            temp = values[0]
            growthRate = values[1]
            bactType = values[2]
            
            error = ""
            if is_number(temp, "float") == False or (is_number(temp, "float") and (float(temp) < 10 or float(temp) > 60)):
                error += "\nError in line 50! The Temperature must be a number between 10 and 60 but value was: " + str(temp) + "."
            if is_number(growthRate, "float") == False or (is_number(growthRate, "float") and float(growthRate) < 0):
                error += "\nError in line 52! The Growth rate must be a positive number but value was: " + str(growthRate) + "."
            if is_number(bactType, "int") == False or (is_number(bactType, "int") and (int(bactType) < 1 or int(bactType) > 4)):
                error += "\nError in line 54! The Bacteria must be an integer between 1 and 4 but value was: " + str(bactType) + "."
            else:
                bactType = bacteria[int(bactType)-1]
            if error == "":
                line = np.array([temp, growthRate, bactType])
                data = np.vstack([data, line])
            else:
                print(error)
    except IOError:
        print("Could not read file:", filename)
    return data

print(dataLoad('test.txt'))
