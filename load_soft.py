import pickle

def read_soft(input_file):
    # convert file into a list of lines
    with open(input_file,'r') as file:
        lines = file.readlines()