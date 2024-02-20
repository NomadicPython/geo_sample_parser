# GEO datasets
Publically available datasets with the sample information provided in .soft and .miniml file formats. This script is currently being created specific to one such dataset - Mammals Methylation Consortium

## soft_2_csv
Parses the .soft file into a csv sample_sheet containing information about each entry.
Also stores that information as a list of dictionaries

## load_soft
Includes functions .soft file into a list of lines and creates a .pkl file to reload lines if needed.
