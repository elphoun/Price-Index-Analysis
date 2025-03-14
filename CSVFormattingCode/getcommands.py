
import pandas as pd
import os

FILTERINSTRUCTIONS = """Input desired headers in order
                        /initialheaders: outputs the original list of headers
                        /currentheaders: outputs the current desired headers
                        /remove <headername>: removes the desired header
                        /exit: exits the program"""

# getFilterCommands(sampleCSV) returns a list containing all of the headers that the user desires to keep
def getFilterCommands(sampleCSV: pd.DataFrame) -> list:
    print(FILTERINSTRUCTIONS)
    InitialHeaders = sampleCSV.headers()
    DesiredHeaders = []
    
    while True: 
        
        header = input()
        
        if header not in InitialHeaders:
            print("ERROR: Header not found")
            continue
            
        if header in DesiredHeaders:
            print("ERROR: Header already included")
            continue
            
        if header == "/exit":
            break
        elif header == "/initialheaders":
            for i in InitialHeaders:
                print(i, end = ", ")
            print("\n")
        elif header == "/currentheaders":
            for i in DesiredHeaders:
                print(i, end = ", ")
            print("\n")
        elif header.startswith("/remove"):
            header = header.split(" ", 1)[1]
            if header in InitialHeaders:
        else:
            DesiredHeaders.append(header)
    return DesiredHeaders
            

            
            
