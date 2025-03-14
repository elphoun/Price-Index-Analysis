import pandas as pd
import os

# Checks for a valid input directory
def InputDirectory():
    while True:
        filepath = input("Input the input folder path: ")
        if os.path.exists(filepath):
            return filepath
        print("FILE DIRECTORY DOES NOT EXIST")

# Creates the Output Directory
def OutputDirectory():
    fileiteration = 1
    while True:
        try:
            directory = input("Input the directory of where the folder should be: ")
            folderpath = input("Input the folder's name: ")
            os.mkdir(fr"{directory}\{folderpath}")
            break
        except FileExistsError:
            if fileiteration == 1:
                folderpath += " (1)"
            else:
                start, end = folderpath.rsplit(f"{fileiteration}", fileiteration-1)
                folderpath = start + f"{fileiteration}" + end
            fileiteration+=1
    return fr"{directory}\{folderpath}"

# Filters headers and pivots the columns
def FilterHeaders(database: pd.DataFrame, headers: list[str]) -> pd.DataFrame:
    return database.filter(items=headers)

# Transposes Data
def Transpose(database: pd.DataFrame) -> pd.DataFrame:
    return database.transpose()

# Combine and Split Headers/Specific type of Parameter (default split is " ")
def SplitMergeColumn(database: pd.DataFrame, header1: str, header2: str, mainheader: str, index: int) -> pd.DataFrame:
    column1 = database.pop(header1)
    column2 = database.pop(header2)
    merged_column = column1 + " " + column2 
    database.insert(index, mainheader, merged_column)
    return database

def FirstasHeader(database: pd.DataFrame) -> pd.DataFrame:
    return database.rename(columns=database.iloc[0]).drop(database.index[0])

def toDate(column: pd.DataFrame) -> pd.DataFrame:
    column["Dates"] = column["Dates"].map(lambda x: f"{x[:4]}-{x[4:]}-01")
    return column
