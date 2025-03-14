import pandas as pd
import os
from adjustformat import *

INSTRUCTIONS = """Note: Invalid Commands will be skipped. Commands should be seperated using spaces.
                \nfilter: filter a database using the given headers
                \nsplit: split a column in half
                \nmerge: merge two columns
                \nremovenull: removes all null values
                \ntranspose: tranposes the data
                \ninstructions: displays the instructions
                \nexit: exits and applies changes\n"""
                
LISTOFCOMMANDS = ["filter", "split", "merge", "removenull", "transpose", "instructions", "exit"]

def main():
    inputdirectory = InputDirectory()
    outputdirectory = OutputDirectory()
    
    csvFiles = os.listdir(inputdirectory)
    sampleCSV = pd.read_csv(fr"{inputdirectory}\{csvFiles[0]}")
    
    listofCommands = takeCommands(sampleCSV)
    
    for csvFile in csvFiles[1:]:
        csv = pd.read_csv(fr"{inputdirectory}\{csvFile}")
        changedcsv = applyChanges(csv, listofCommands)
        changedcsv.to_csv(fr"{outputdirectory}\{csvFile}", header=csv.columns)

def takeCommands(sampleCSV):
    global INSTRUCTIONS, LISTOFCOMMANDS
    changes = []
    while True:
        command = input("Input a Command: ")
        if "filter" == command:
            
        elif "split" == command:
            
        elif "merge" == command:
            
        elif "removenull" == command:
            
        elif "transpose" == command:
            
        elif "instructions" == command:
            
        elif "exit" == command:
            return changes
        else:
            print("Not a Valid Command")

def applyChanges():
    print("Placeholder")

        
# def TakeCommands() -> list:
#     global INSTRUCTIONS, LISTOFCOMMANDS
#     print(INSTRUCTIONS)
#     changes = []
#     while True:
#         command = input("Input a Command: ")
#         if command == "exit":
#             break
#         elif command in LISTOFCOMMANDS:
#             changes.append(command)
#     return changes
        
        
# def applyChanges(database):
#     while True:
#             command = input()
#             if command == "filter":
#                 database = adjustformat.FilterHeaders(database)
#             elif command == "split":
#                 database = adjustformat.SplitMergeColumn(database, True)
#             elif command == "merge":
#                 database = adjustformat.SplitMergeColumn(database, False)
#             elif command == 'removenull':
#                 database = adjustformat.RemoveNull(database)
#             elif command == "transpose":
#                 database = adjustformat.Transpose(database)
#             elif command == "exit":
#                 return database
#             else:
#                 print("not valid")

# getCSV()
