from ldparser import ldData
import pandas as pd
import sys, os, glob
from itertools import groupby
import pandas as pd
import matplotlib.pyplot as plt

# Create a new ldData object
if __name__ == '__main__':
    if len(sys.argv)!=3:
        print("Usage: python csv_to_ld.py <path-to-csv-file> <path_to_ld_file>")
        exit(1)

    csv_file_path = sys.argv[1]
    ld_file_path = sys.argv[2]
    df = pd.read_csv(csv_file_path)

    l = ldData.frompd(df)
    l.write(ld_file_path)
