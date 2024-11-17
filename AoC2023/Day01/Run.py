import re

def process():
  lines = load(True)
  process_part1(lines,1)
  
def load(is_test=True):
  # Construct the file path based on whether it's a test or not
  file_path = f"/home/runner/AoCPython/AoC2023/Day01/day-01{'-sample' if is_test else ''}.txt"
  # Read and return the lines from the file
  with open(file_path, 'r') as file:
      return file.readlines()

def process_part1(lines, mode):
  # Assuming the get_num function is defined elsewhere
  # Summing up the result of get_num applied to each line
  print(sum([get_num(line, 2) for line in lines]))

def text2num(line):
  # Dictionary mapping text to numbers
  rep_dict = {
      'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
      'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9
  }
  # Replacing text numbers with their numeric counterparts
  for text, num in rep_dict.items():
      line = line.replace(text, str(num))
  return line

def text2num_2(line):
    rep_dict = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9
    }
    nums = {}

    # Get all numbers into the dictionary
    for i, c in enumerate(line):
        if c.isdigit():
            nums[i] = int(c)

    # Hunt for the word numbers
    for key in rep_dict.keys():
        spos = 0
        while spos < len(line):
            spos = line.find(key, spos)
            if spos != -1:
                nums[spos] = rep_dict[key]
                spos += 1
            else:
                break

    # Sorting and joining the values
    return ''.join(str(value) for _, value in sorted(nums.items()))

# Placeholder for get_num function as it is not defined in the provided snippet
def get_num(line, mode):
  line = text2num_2(line) if (mode == 2) else re.sub("[a-z]","",line)
  return 0 if int(line) else 
