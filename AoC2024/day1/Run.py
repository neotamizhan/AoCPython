from AoC2024.utils import load

def process(daynum, level):
  lines = load(daynum,False)  
  list1 = []
  list2 = []
  list3 = []
  for line in lines:
    #print(line)
    loc1, loc2 = line.split()
    list1.append(int(loc1))
    list2.append(int(loc2))

  list1.sort()
  list2.sort()

  for i in range(len(list1)):
    if level == 1:
      list3.append(process_part1(list1, list2, i))
    else:
      list3.append(process_part2(list1, list2, i))

  print(sum(list3))

def process_part1(list1, list2,i):
  return abs(list1[i]-list2[i])

def process_part2(list1, list2,i):
  return list1[i] * list2.count(list1[i])
