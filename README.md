# GEO datasets
Publically available datasets with the sample information provided in .soft and .miniml file formats. This script is currently being created specific to one such dataset - Mammals Methylation Consortium

## soft_2_csv
Parses the .soft file into a csv sample_sheet containing information about each entry.
Also stores that information as a list of dictionaries

## load_soft
Includes functions .soft file into a list of lines and creates a .pkl file to reload lines if needed.

## read_series_data
Extremely specific for this particular dataset. In the function parse_txt_file add line numbers to get more columns.

```
usage: read_series_data.py [-h] [-x] [-c] input_file

script to extract required information from the sample_matrix file
positional arguments:
  input_file  Path to the input file
options:
  -h, --help  show this help message and exit
  -x, --xlsx  creates excel file
  -c, --csv   creates csv file```
