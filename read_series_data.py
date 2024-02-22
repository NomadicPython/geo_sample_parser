import argparse
import pandas as pd
import os

def parse_args():
    """Parse input arguments."""
    parser = argparse.ArgumentParser(description="Script to extract required information from the sample_matrix file.")
    parser.add_argument("input_file", help="Path to the input file.")
    parser.add_argument("-x", "--xlsx", action="store_true", help="Creates an Excel file.")
    parser.add_argument("-c", "--csv", action="store_true", help="Creates a CSV file.")
    return parser.parse_args()

def extract_ids_from_line(line):
    """Extract IDs from the line."""
    ids = line.split('\t')[1:]
    ids = [id.split(' ')[-1].strip('\n').strip('"') for id in ids]
    return pd.DataFrame({'ID': ids})

def extract_characteristic_from_line(line, df):
    """Extract characteristic from the line, setting the identifier as the column header."""
    parts = line.split('\t')[1:]
    # The identifier is now extracted from the first entry's format "identifier: value"
    identifier = parts[0].split(': ')[0].strip('"')
    values = [part.split(': ')[1].strip('\n').strip('"') for part in parts]
    df[identifier] = values
    return df

def generic_extract(line, df):
    """Generic extraction for simple structured lines."""
    items = line.split('\t')
    title = items[0]
    items = [item.strip('"') for item in items[1:]]
    df[title[1:]] = items
    return df

def parse_txt_file(file_path):
    """Parse the txt file and extract information."""
    with open(file_path, 'r') as file:
        lines = file.readlines()
        
    df = None
    for index, line in enumerate(lines):
        if index == 380:
            df = extract_ids_from_line(line)
        elif 389 <= index <= 395:  # Adjust to include the range of lines you're interested in
            df = extract_characteristic_from_line(line, df)
        elif index in (387, 388):
            df = generic_extract(line, df)
            
    if df is None:
        raise ValueError("The dataframe could not be created. Check the file format and line indices.")
    return df

def main():
    args = parse_args()
    df = parse_txt_file(args.input_file)
    
    if args.xlsx:
        df.to_excel(os.path.splitext(args.input_file)[0] + '.xlsx', index=False)
    if args.csv:
        df.to_csv(os.path.splitext(args.input_file)[0] + '.csv', index=False)

if __name__ == '__main__':
    main()
