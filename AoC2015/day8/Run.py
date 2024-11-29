import codecs
from AoC2015.utils import load


#locals
def char_len(line):
    print(line)
    # Decode the escape sequences
    decoded_line = codecs.decode(line, 'unicode_escape')
    
    # Remove the surrounding quotes
    if decoded_line.startswith('"') and decoded_line.endswith('"'):
        decoded_line = decoded_line[1:-1]
    print(decoded_line)
    return len(decoded_line)

def process(daynum):
  lines = load(daynum,True)  
  process_part1(lines)

def process_part1(lines):
  for line in lines:
    print(char_len(line))
  return 

def process_part2(line):
  return