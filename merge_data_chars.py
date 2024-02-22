import argparse
import pandas as pd
from time import time

def main(feather_file_path, csv_file_path, output_file_path):
    start_time = time()

    print('Loading the Feather file...')
    df_feather = pd.read_feather(feather_file_path)
    print('Feather file loaded.')

    print('Transposing the dataset...')
    df_feather_transposed = df_feather.T
    print('Dataset transposed.')

    print('Correcting the header...')
    new_header = df_feather_transposed.iloc[0]
    df_feather_transposed = df_feather_transposed[1:]
    df_feather_transposed.columns = new_header
    print('Header corrected.')

    print('Loading the CSV file with additional features...')
    df_csv = pd.read_csv(csv_file_path)
    print('CSV with characteristics loaded.')

    print('Merging the datasets...')
    df_feather_transposed.reset_index(inplace=True)
    df_feather_transposed.columns.values[0] = 'ID'
    merged_df = pd.merge(df_feather_transposed, df_csv, on='ID', how='left')
    print('Datasets merged.')

    print(f'Saving the merged dataset as {output_file_path} in Feather format...')
    merged_df.to_feather(output_file_path)
    print('Merge saved successfully.')

    end_time = time()
    print(f'Total time taken: {end_time - start_time:.2f} seconds')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Merge a transposed Feather file with a CSV file and save the output.')
    parser.add_argument('--feather_file', type=str, required=True, help='Path to the input Feather file.')
    parser.add_argument('--csv_file', type=str, required=True, help='Path to the input CSV file with additional characteristics.')
    parser.add_argument('--output_file', type=str, required=True, help='Path where the merged Feather file should be saved.')

    args = parser.parse_args()
    main(args.feather_file, args.csv_file, args.output_file)
