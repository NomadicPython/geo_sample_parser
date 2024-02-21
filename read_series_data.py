
import pandas as pd

def extract_ids_from_line(line):
    ids = line.split('\t')[1:]
    for index in range(len(ids)):
        ids[index] = ids[index].split(' ')[-1].strip('\n').strip('"')
    df = pd.DataFrame({'ID': ids})
    return df

def extract_age_from_line(line, df):
    ages = line.split('\t')[1:]
    for index in range(len(ages)):
        ages[index] = ages[index].split(' ')[-1].strip('\n').strip('"')
    df['Age'] = ages
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
            if index == 389:
                df = extract_age_from_line(line, df)
                num_na = count_na_in_age_column(df)
                print(num_na)
                
        return df

df = parse_txt_file('GSE223748_series_matrix.txt')
print(df)