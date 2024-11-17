import os
import sys

from 2015.utils import load


def process(daynum):
  line = load(daynum,False)  
  process_part2(line[0])

def process_part1(line):
  print(line.count('(') - line.count(')'))

def process_part2(line):
  floor=0
  for i,c in enumerate(line):
    if c == '(':
      floor+=1
    elif c == ')':
      floor-=1
    if floor == -1:
      print(i+1)
      break