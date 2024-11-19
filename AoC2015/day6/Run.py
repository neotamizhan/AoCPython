import numpy as np
import re

from AoC2015.utils import load


def process(daynum):
  line = load(daynum, False)
  process_part2(line)


def parse(line):
  ins = re.compile(r'(.*?)(\d+),(\d+).*?(\d+),(\d+)')
  print(line)
  m = ins.match(line).groups()
  return {
      "ins": m[0].strip(),
      "ss": int(m[1]),
      "se": int(m[2]),
      "es": int(m[3]),
      "ee": int(m[4])
  }


def process_part1(lines):
  grid = np.zeros((1000, 1000), dtype=bool)
  for line in lines:
    i = parse(line)
    sub = grid[i["ss"]:i["es"] + 1, i["se"]:i["ee"] + 1]
    if i["ins"] == "turn on":
      sub[:] = True
    elif i["ins"] == "turn off":
      sub[:] = False
    else:
      sub[:] = ~sub

  num_lights_on = np.sum(grid)
  print(f"Number of lights on: {num_lights_on}")
  return


def process_part2(lines):
  grid = np.zeros((1000, 1000), dtype=int)
  for line in lines:
    i = parse(line)
    sub = grid[i["ss"]:i["es"] + 1, i["se"]:i["ee"] + 1]
    if i["ins"] == "turn on":
      sub[:] += 1
    elif i["ins"] == "turn off":
      np.maximum(sub - 1, 0, out=sub)
    else:
      sub[:] += 2

  num_lights_on = np.sum(grid)
  print(f"Number of lights on: {num_lights_on}")
  return
