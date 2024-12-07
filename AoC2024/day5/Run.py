from AoC2024.utils import load

#problem url: https://adventofcode.com/2024/day/5

def read_data(lines):    
  try:
    empty_index = lines.index('\n')
  except ValueError:    
    empty_index = -1

  guide, pages = lines[:empty_index], lines[empty_index+1:]

  guide = [list(map(int, x.strip().split("|"))) for x in guide]
  pages = [list(map(int, x.strip().split(","))) for x in pages]
  print(f"guide: {guide}\n pages: {pages}")


def process(daynum):
  level = 1
  lines = load(daynum,True)  
  if level == 1:
    process_part1(lines)
  else:
    process_part2(lines)

def process_part1(line):
  #print(line)
  read_data(line)  

def process_part2(line):
  return