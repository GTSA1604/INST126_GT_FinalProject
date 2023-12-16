# Name: Operator Selection Program
# Author: Garrette Tsang
# Creation Date: 11/28/2023
# Updated: 12/16/2023
# This script is designed to interact with a static CSV file,
# and retrieve stats for video game characters based on user input
# through a text file.

import os
import pandas as pd
from prefab_team_reader import TeamCompReader

OperatorCSV = pd.read_csv("Arknights Stats - Operators.csv") # Reading the CSV file
OperatorCSV["DMG/Min"] = OperatorCSV["Attack"] * (60 / (OperatorCSV["Atk Interval"])) # Damage per minute
OperatorList = [] # Creating an empty list to store the contents of the input file

TeamCompReader("SquadOne.txt", OperatorList)
# calling the TeamCompReader function to read the SquadOne.txt file and append the contents to the OperatorList list

os.chdir("c:\\Users\\gtsa1\\OneDrive\\Desktop\\UMD\\INST126\\Final_Project")
# for the purposes of this script, this chdir is necessary to ensure the CSV file would
# be properly accessed, and the output CSV file would be written to the correct directory.

def selectOperator():
    """
        This function operates as a team composition builder for the mobile game Arknights.
        It hinges on the use of a CSV file containing all of the operators in the game and their stats.
        The function will read a file containing a list of desired operators and their levels,
        and retrieve the relevant operator stats from the CSV file
        that correspond to the operators and levels in the file.
    """

    OperatorCSV = pd.read_csv("Arknights Stats - Operators.csv")
    print("Greetings, Doctor. Welcome to the operator selection terminal.")
    for OpName, OpLevel in OperatorList: # Iterating through the OperatorList list
        MatchingOpInfo = OperatorCSV[ (OperatorCSV["Character"] == OpName) & (OperatorCSV["Promotion"] == OpLevel)]
        # Finding the rows in the CSV file that match the operator name and level in the OperatorList list
        if not MatchingOpInfo.empty: # Check if any matching rows were found
        # Convert the matching rows to a dictionary
            matching_dict = MatchingOpInfo.to_dict(orient='records')    # Convert the matching rows to a dictionary
            result_list = []                                            # Create an empty list to store the results
            result_list.extend(matching_dict)                           # Append the dictionary to the list
        
        else:
            print(f"No matching rows found for Operator Name: {OpName}, Operator Level: {OpLevel}")
            raise ValueError       # Raise an error if no matching rows were found
 
        if result_list:
            result_df = pd.DataFrame(result_list)
            # Create a DataFrame from the list of matching rows

            # Write the resulting DataFrame to a CSV file
            result_df.to_csv('matching_results.csv', index=False, mode='a',header=False)

            print("Matching row(s) found and written to CSV.")
        else:
            print("No matching rows found.")