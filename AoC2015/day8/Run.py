import codecs
from AoC2015.utils import load


#locals
def char_len(line):
    print(line)
    # Remove the surrounding quotes
    if line.startswith('"') and line.endswith('"'):
        print('removing quotes')
        line = line[1:-1]
    # Decode the escape sequences
    decoded_line = codecs.decode(line, 'unicode_escape')
    

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