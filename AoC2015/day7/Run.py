import re
from AoC2015.utils import load

#locals
def handle_ins(ins, d):  
  op, key = ins.split(" -> ")
  key = key.strip()
  parts = op.split()

  if "AND" in parts:
    op1, optr, op2 = parts
    d[key] = get_value(d,op1) & get_value(d,op2)
  elif "OR" in parts:    
    op1, optr, op2 = parts
    d[key] = get_value(d,op1) | get_value(d,op2)
  elif "NOT" in parts:
    optr, op = parts
    d[key] = ~get_value(d,op) % 65536
  elif "LSHIFT" in parts:
    op1, optr, shift = parts
    d[key] = get_value(d,op1) << int(shift)
  elif "RSHIFT" in parts:
    op1, optr, shift = parts
    d[key] = get_value(d,op1) >> int(shift)
  else:
    d[key] = get_value(d,parts[0])

def are_all_inputs_valid(ins, d):
  lhs, rhs = ins.split(" -> ")
  inputs = re.compile(r'([a-z]{1,2})')
  for inp in re.findall(inputs, lhs):
    if inp not in d:
      return False    
  return True


def get_value(d, key):
  if key.isdigit():
    return int(key)
  return d.get(key,0)

def solve(instructions):
    d = {}
    changed = True
    while changed:
        changed = False
        for ins in instructions:
            try:
                old_val = d.get(ins.split(" -> ")[1].strip())
                handle_ins(ins, d)
                new_val = d.get(ins.split(" -> ")[1].strip())
                if old_val != new_val:
                    changed = True
            except Exception as e:
                continue
    return d

def process(daynum):
  lines = load(daynum,False)  
  process_part1(lines)
  

def process_part1(lines):
  circuit = solve(lines)
  print(circuit["a"])
  return 

def process_part2(line):
  return