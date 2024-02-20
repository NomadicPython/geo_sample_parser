import pickle

def read_soft(input_file):
    """convert file into a list of lines
    Then dumps the list of lines as a pkl file"""
    with open(input_file,'r') as file:
        lines = file.readlines()
    
    # Don't want to read file everytime, so dump lines to disk
    with open(input_file+'_lines.pkl', 'wb') as f:
        pickle.dump(lines, f)
    
def load_lines(input_file):
    """loads lines variable from *_lines.pkl file"""
    with open(input_file+'_lines.pkl', 'rb') as f:
        lines = pickle.load(f)
