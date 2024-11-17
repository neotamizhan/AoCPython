import os
import sys
import re

from AoC2015.utils import load

def process():
  lines = load('02',False)
  process_part2(lines)

def process_part2(lines):
  total_ribbon = 0
  for line in lines:
    total_ribbon += ribbon(line)
  print(total_ribbon)
  
def process_part1(lines):
  total_wrap_area = 0
  for line in lines:
    total_wrap_area += wrap_area(line)
  print(total_wrap_area)

def wrap_area(line):  
  (l,w,h) = [int(num) for num in re.findall(r'\d+', line)]
  return (2*l*w + 2*w*h + 2*h*l) + small_area(l,w,h)

def small_area(l,w,h):
  arr = [l,w,h]
  arr.remove(max(arr))
  return arr[0] * arr[1]

def small_peri(l,w,h):
  arr = [l,w,h]
  arr.remove(max(arr))
  return 2 * (arr[0] + arr[1])

def ribbon(line):
  (l,w,h) = [int(num) for num in re.findall(r'\d+', line)]  
  return small_peri(l,w,h) + (l*w*h)