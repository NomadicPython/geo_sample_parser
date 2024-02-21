import pickle
import os

def read_soft(input_file):
    """convert file into a list of lines
    Then dumps the list of lines as a pkl file"""
    with open(input_file,'r') as file:
        lines = file.readlines()
    print("loaded lines")
    # Don't want to read file everytime, so dump lines to disk
    with open(input_file+'_lines.pkl', 'wb') as f:
        pickle.dump(lines, f)
    print("dumped file")
    return lines 
    
def load_lines(input_file):
    """loads lines variable from *_lines.pkl file"""
    with open(input_file+'_lines.pkl', 'rb') as f:
        lines = pickle.load(f)
    return lines

def load_soft(input_file):
    """gives list of lines for the soft file"""
    # check for _lines.pkl file
    if os.path.isfile(input_file+"_lines.pkl"):
        print("lines.pkl file found")
        return load_lines(input_file)
    else:
        print("lines.pkl file not found")
        return read_soft(input_file)