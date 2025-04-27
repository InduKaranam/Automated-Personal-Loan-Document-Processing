import json
import os

def save_extracted_data(data, filename):
    if not os.path.exists('extracted_data'):
        os.makedirs('extracted_data')

    filepath = os.path.join('extracted_data', filename)
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=4)
