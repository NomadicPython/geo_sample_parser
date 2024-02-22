import argparse
import pandas as pd

def convert_csv_to_feather(input_file, chunk_size_multiplier):
    # Calculate actual chunk size
    chunk_size = chunk_size_multiplier * 1000000

    # Construct the output file path from the input file name
    feather_file_path = input_file.replace('.csv', '.feather')

    # Initialize an empty list to hold chunks
    chunks_list = []

    # Load the CSV file in chunks
    for chunk in pd.read_csv(input_file, chunksize=chunk_size):
        # Process each chunk if needed
        chunks_list.append(chunk)

    # Concatenate all chunks into a single DataFrame
    df = pd.concat(chunks_list, ignore_index=True)

    # Save the entire DataFrame as a Feather file
    df.to_feather(feather_file_path)

    # To verify, load the Feather file and perform operations
    df = pd.read_feather(feather_file_path)
    print(df.head())  # Just to verify it works

if __name__ == '__main__':
    # Create the parser
    parser = argparse.ArgumentParser(description='Convert CSV to Feather format.')

    # Add the arguments
    parser.add_argument('--input_file',
                        type=str,
                        required=True,
                        help='The path to the input CSV file.')

    parser.add_argument('--chunk_size',
                        type=int,
                        required=True,
                        help='The chunk size multiplier (actual chunk size will be this value multiplied by 1,000,000).')

    # Parse the arguments
    args = parser.parse_args()

    # Call the function with the parsed arguments
    convert_csv_to_feather(args.input_file, args.chunk_size)
