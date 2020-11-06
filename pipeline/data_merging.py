import pandas as pd
import os, glob

def merge_data(path):
    """Reads and merges all csv-files of the kickstarter dataset. Requires a folder named data in the working directory."""
     
    all_files = glob.glob(os.path.join(path, "Kickstarter*.csv"))
    df_from_each_file = (pd.read_csv(f, sep=',') for f in all_files)

    df = pd.concat(df_from_each_file, ignore_index=True)
    df = df.loc[:, ~df.columns.str.match('Unnamed')]
    df.to_csv('data/Kickstarter_merged.csv', index=False)
    return df