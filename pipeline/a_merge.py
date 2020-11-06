import os, glob
import numpy as np

from data_merging import merge_data

print("Merging data.")
df = merge_data('/Users/jakoliendenhollander/neuefische/2020-ds-Project02-Kickstarter/raw_data/')
print("Merge completed, saving file in the data folder.")