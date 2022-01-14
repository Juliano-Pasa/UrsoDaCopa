"""
    This module is responsable for writing new data into the txt files
"""

import os
import csv

def write_to_file(filename, metrics):
    
    relative_path = "../Data/" + filename + ".csv"
    file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), relative_path)
    
    with open(file_path, "a", newline='') as f:
        writer = csv.writer(f)
        writer.writerow(metrics)