from AoC2024.utils import load

#problem url: https://adventofcode.com/2024/day/2

#function to see if a list of numbers is all increasing or all decreasing
def is_it_safe(lst):  
  diffs = []
  for i in range(1,len(lst)):
    diffs.append(lst[i] - lst[i-1])
  
  gradual = all(x >= 0 for x in diffs) or all(x <= 0 for x in diffs)
  smooth = all(abs(x) >= 1 and abs(x) <= 3 for x in diffs)
  return gradual and smooth

#function to see if a list of numbers can be made safe by removing one number
def can_be_safe(report):  
  for i in range(len(report)):    
    new_report = report[:]
    del new_report[i]
    if is_it_safe(new_report):    
      return True
  return False

def process(daynum):  
  level = 1
  lines = load(daynum,False)

  #convert the list of strings to a list of list of integers
  reports = [list(map(int, x.split())) for x in lines]

  if level == 1:
    print(process_part1(reports))
  else:
    print(process_part2(reports))
  

def process_part1(reports):  
  safe = []
  for report in reports:    
    if is_it_safe(report): 
      safe.append(report)
  return len(safe)

def process_part2(reports):  
  safe = []
  unsafe = []
  for report in reports:
    if is_it_safe(report): 
      safe.append(report)
    else: 
      unsafe.append(report)
    
  for report in unsafe:
    if can_be_safe(report):
      safe.append(report)

  return len(safe)