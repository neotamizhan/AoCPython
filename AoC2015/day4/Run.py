import os
import sys
import hashlib

from AoC2015.utils import load


def get_md5_hash(input_string):
  # Encode the input string to bytes
  encoded_string = input_string.encode('utf-8')
  # Create an MD5 hash object
  md5_hash = hashlib.md5()
  # Update the hash object with the encoded string
  md5_hash.update(encoded_string)
  # Return the hexadecimal digest of the hash
  return md5_hash.hexdigest()


def process(daynum):
  line = load(daynum, True)
  process_part1(line[0])


def process_part1(line):
  key = line
  seed = 0
  md5 = ''
  while md5[:5] != '00000':
    seed += 1
    md5 = get_md5_hash(f'{key}{seed}')

  print(f'{seed}:{md5}')
  return


def process_part2(line):
  key = line
  seed = 0
  md5 = ''
  while md5[:6] != '000000':
    seed += 1
    md5 = get_md5_hash(f'{key}{seed}')

  print(f'{seed}:{md5}')
  return
