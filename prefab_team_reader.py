# Name: prefab_team_reader.py
# Author: Garrette Tsang
# Creation Date: 12/16/2023
# Updated: 12/16/2023
# This module is designed to interact with the main Operator Selection program. 
# It will read a file containing a list of operators and their levels, 
# and return a list of tuples containing the operator name and level.

import os

def TeamCompReader(prefabFile, prefabList):
    """
    This function is designed to read a preexisting team composition file and return a list of the contents.
    """
    os.chdir("C:\\Users\\gtsa1\\OneDrive\\Desktop\\UMD\\INST126\\Final_Project")
    with open(prefabFile, 'r') as file:     # Opening the file in read mode
        for line in file:                   # Iterating through each line in the file
            name, level = line.strip().split(', ')  # Splitting the line into name and level using a comma as the separator
            prefabList.append((name, level)) # Append the name and level as a tuple to the list