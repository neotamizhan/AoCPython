import os
import sys

from AoC2015.utils import load


def process(daynum):
  line = load(daynum, False)
  process_part2(line[0])


def process_part1(line):
  cx = cy = 0
  path = {'0:0': 1}
  for c in line:
    match c:
      case '^':
        cy += 1
      case 'v':
        cy -= 1
      case '>':
        cx += 1
      case '<':
        cx -= 1

    cpos = f'{cx}:{cy}'
    path[cpos] = path.get(cpos, 0) + 1

  print(len(path))


def process_part2(line):
  spos = [0, 0]
  rpos = [0, 0]
  spath = {}
  rpath = {}
  path = {}
  spath['0:0'] = None
  rpath['0:0'] = None
  path['0:0'] = None

  for i, c in enumerate(line):
    #print(i)
    match c:
      case '^':
        if i % 2 == 1:
          rpos[1] += 1
        else:
          spos[1] += 1
      case 'v':
        if i % 2 == 1:
          rpos[1] -= 1
        else:
          spos[1] -= 1
      case '>':
        if i % 2 == 1:
          rpos[0] += 1
        else:
          spos[0] += 1
      case '<':
        if i % 2 == 1:
          rpos[0] -= 1
        else:
          spos[0] -= 1

    if i % 2 == 1:
      rpath[f'{rpos[0]}:{rpos[1]}'] = None
      path[f'{rpos[0]}:{rpos[1]}'] = None
    else:
      spath[f'{spos[0]}:{spos[1]}'] = None
      path[f'{spos[0]}:{spos[1]}'] = None

  print(f'{len(spath.keys())} : {len(rpath.keys())} : {len(path.keys())}')
  #print(f'Santa = {spath.keys()}; Robo = {rpath.keys()}')
  
