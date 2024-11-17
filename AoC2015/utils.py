import os

def load(daynum, is_test=True):
  # Construct the file path based on whether it's a test or not
  script_dir = os.path.dirname(__file__)
  filename = f"day-{daynum}{'-sample' if is_test else ''}.txt"
  file_path = os.path.join(script_dir, f'Day{daynum}', filename)  
  # Read and return the lines from the file
  with open(file_path, 'r') as file:
    return file.readlines()
