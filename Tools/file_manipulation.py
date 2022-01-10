"""
    This module is responsable for writing new data into the txt files
"""

import csv

def write_to_file(filename, metrics):
    
    file_path = "../Data/" + filename + ".csv"
    
    with open(file_path, "a", newline='') as f:
        writer = csv.writer(f)
        writer.writerow(metrics)