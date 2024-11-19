import re

from AoC2015.utils import load


def has3vowels(word):
  vowels = re.compile(r'[aeiou]')
  return len(re.findall(vowels, word)) >= 3

def hasrepeat(word):
  repeat = re.compile(r'(.)\1')
  return len(re.findall(repeat, word)) > 0

def hasnotchars(word):
  chars = re.compile(r'ab|cd|pq|xy')
  return len(re.findall(chars, word)) == 0


def process(daynum):
  lines = load(daynum, False)
  process_part2(lines)


def process_part1(lines):
  v = re.compile(r'(.)[^\1]\1')
  
  print(re.findall(v,"xyxabcabaccc"))
  
  nice = 0
  for line in lines:
    if has3vowels(line) and hasrepeat(line) and hasnotchars(line):
      nice += 1
      print(f'{line} is nice')

  print(nice)
  return

def process_part2(lines):
  v1 = re.compile(r'(..).*\1')
  v2 = re.compile(r'(.)[^\1]\1')

  nice = 0
  for line in lines:
    if len(re.findall(v1, line)) > 0 and len(re.findall(v2, line)) > 0:
      nice += 1
      print(f'{line} is nice')
  print(nice)
  return
