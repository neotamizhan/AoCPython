import re
from AoC2024.utils import load

#problem url: https://adventofcode.com/2024/day/3

def process(daynum):
  level = 2
  lines = load(daynum,False)  
  if level == 2:
    print(process_part1(lines))
  else:
    print(process_part2(lines))

def process_part1(lines):
  #join the lines into a single string
  line = " ".join(lines)
  muls = re.findall(r'mul[ ]*\([ ]*(\d+)[ ]*,[ ]*(\d+)[ ]*\)',line)

  #convert the string arrays into arrays of integers
  muls = [list(map(int, x)) for x in muls]
    
  #multiply the two numbers in each array and get the sum of all the results
  muls = sum([x[0] * x[1] for x in muls])
  
  return muls

def process_part2(lines):
  #join the lines into a single string
  line = " ".join(lines)

  #replace string "don't()" & "do()" with "don't()[DONT]" & "do()[DO]" respectively
  line = re.sub(r'don\'t\(\)',"don't()[DONT]",line)
  line = re.sub(r'do\(\)',"do()[DO]",line)

  #split the line based on the words "don't()" and "do()"
  line = re.split(r'don\'t\(\)|do\(\)',line)

  #remove the entries starting with "[DONT]" from the array
  lines = [x for x in line if not x.startswith("[DONT]")]
  muls = process_part1(lines)
   
  return muls