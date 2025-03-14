import pandas as pd
import os

from adjustformat import InputDirectory, OutputDirectory, FilterHeaders, Transpose, SplitMergeColumn, FirstasHeader, toDate

def numerical_headers():
    return list(map(str, range(197001, 202402)))

NON_NUMERICAL_HEADERS = ["Country Code", "Country"] + numerical_headers()

def process_csv(dataframe: pd.DataFrame) -> pd.DataFrame:
    columnsFiltered = FilterHeaders(dataframe, NON_NUMERICAL_HEADERS)
    mergedColumns = SplitMergeColumn(columnsFiltered, "Country", "Country Code", "Country", 0)
    transposedData = Transpose(mergedColumns)
    renameHeaders = FirstasHeader(transposedData)
    includeDates = renameHeaders.reset_index(names=["Dates"])
    includeDates = toDate(includeDates)
    return includeDates

def main():
    input_directory = InputDirectory()
    output_directory = fr"C:\Users\kalem\OneDrive\Desktop\PowerBI\Formatted"
    csv_files = [file for file in os.listdir(input_directory) if file.endswith(".csv")]
    os.mkdir(output_directory)
    os.chmod(output_directory, 0o700)
    
    for csv_file in csv_files:
        input_path = os.path.join(input_directory, csv_file)
        output_path = os.path.join(output_directory, csv_file)
        csv_data = pd.read_csv(input_path)
        changed_csv = process_csv(csv_data)
        changed_csv.to_csv(output_path, index=False)
    return

if __name__ == "__main__":
    main()
