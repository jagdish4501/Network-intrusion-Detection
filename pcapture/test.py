import pandas as pd

def check_header_mismatch(file1_path, file2_path):
    # Read headers of both CSV files
    header1 = pd.read_csv(file1_path, nrows=0).columns.tolist()
    header2 = pd.read_csv(file2_path, nrows=0).columns.tolist()

    # Iterate through headers and check for mismatches
    for column1, column2 in zip(header1, header2):
        if column1==column2:
            print(column1,' ',column2,'------------------------Eqaul')
        else:
            print(column1,' ',column2,'-----------Not Eqaul')

# Example usage:
file1_path = "./packet_features.csv"
file2_path = "../ref.csv"
check_header_mismatch(file1_path, file2_path)
