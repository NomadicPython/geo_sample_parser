import argparse
import pandas as pd
import os

def parse_args():
    """grab input file location"""
    parser = argparse.ArgumentParser(description="script to extract required information from the sample_matrix file")
    
    # Add positional arguments
    parser.add_argument("input_file", help="Path to the input file")
    # Add optional arguments
    parser.add_argument("-x", "--xlsx", action="store_true", help="creates excel file")
    parser.add_argument("-c", "--csv", action="store_true", help="creates csv file")

    return parser.parse_args()

def extract_ids_from_line(line):
    ids = line.split('\t')[1:]
    for index in range(len(ids)):
        ids[index] = ids[index].split(' ')[-1].strip('\n').strip('"')
    df = pd.DataFrame({'ID': ids})
    return df

def extract_characteristic_from_line(line, df):
    ages = line.split('\t')[1:]
    title = ages[0].split(' ')[0].strip('\n').strip('":')
    for index in range(len(ages)):
        ages[index] = ages[index].split(' ')[-1].strip('\n').strip('"')
    df[title] = ages
    return df

def generic_extract(line,df):
    items = line.split('\t')
    title = items[0]
    items = items[1:]
    for index in range(len(items)):
        items[index] = items[index].strip('"')
    df[title[1:]] = items
    return df

def count_na_in_age_column(df):
    return df['Age'].eq('NA').sum()

def parse_txt_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for index in range(len(lines)):
            line = lines[index]
            if index == 380:
                df = extract_ids_from_line(line)
            if index in (389):
                #Add other lines if they have "age: 1" kind of structure
                df = extract_characteristic_from_line(line, df)
            if index in (387,388,):
                # add other lines you want to extract that have a simple structure
                df = generic_extract(line,df)                        
        return df
args = parse_args()
df = parse_txt_file(args.input_file)
if args.xlsx: df.to_excel(os.path.splitext(args.input_file)[0]+'.xlsx')
if args.csv: df.to_csv(os.path.splitext(args.input_file)[0]+'.csv')