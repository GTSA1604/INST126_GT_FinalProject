import os
import pandas as pd
from prefab_team_reader import TeamCompReader

"""
    Insert docstring here
"""

# Missing Checklists:
"""
IN PROGRESS    RQ 6.1 You wrote documentation in the form of a README.
    RQ 6.2 You wrote documentation in comments at the top of a script.
    RQ 6.5 You wrote documentation sufficient to enable someone else to use your script/program.
DONE    RQ 6.7 You chose an appropriate license for your program/script.
    RQ 6.8 You made appropriate use of another person’s license when incorporating their software.
"""

# In order to get credit for this “advanced topic”, all you need to do is:
# use Git on your Final Project to make commits and track changes
# turn in your work as a Git repo, either by sharing a remote address (like
# GitHub) or by just zipping up the Git repo folder and submitting that


OperatorCSV = pd.read_csv("Arknights Stats - Operators.csv")
OperatorCSV["DMG/Min"] = OperatorCSV["Attack"] * (60 / (OperatorCSV["Atk Interval"])) # Damage per minute
OperatorList = []

TeamCompReader("SquadOne.txt", OperatorList)

os.chdir("c:\\Users\\gtsa1\\OneDrive\\Desktop\\UMD\\INST126\\Final_Project")
def selectOperator():
    OperatorCSV = pd.read_csv("Arknights Stats - Operators.csv")
    print("Greetings, Doctor. Welcome to the operator selection terminal.")
    for OpName, OpLevel in OperatorList:
        MatchingOpInfo = OperatorCSV[ (OperatorCSV["Character"] == OpName) & (OperatorCSV["Promotion"] == OpLevel)]
        # Check if any matching rows were found
        if not MatchingOpInfo.empty:
        # Convert the matching rows to a dictionary
            matching_dict = MatchingOpInfo.to_dict(orient='records')
            result_list = []
            result_list.extend(matching_dict)
        
        else:
            print(f"No matching rows found for Operator Name: {OpName}, Operator Level: {OpLevel}")
            raise ValueError
 
        if result_list:
            result_df = pd.DataFrame(result_list)

            # Write the resulting DataFrame to a CSV file
            result_df.to_csv('matching_results.csv', index=False, mode='a',header=False)

            print("Matching row(s) found and written to CSV.")
        else:
            print("No matching rows found.")