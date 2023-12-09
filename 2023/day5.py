# source_map = {}

# def solve_part_1(input_data):
#     lines = input_data.split("\n")
#     _, seeds_str = lines[0].split(": ")
    
#     seeds = [int(seed) for seed in seeds_str.split(" ")]
    
#     for seed in seeds:
#         source_map[seed] = seed
    
#     for line in lines[1:]:
#         if line == "":
#             continue
#         if not line.split(" ")[0].isdigit():
#             source_map[line] = []
#         else:
#             destination, range_start, range_length = [int(num) for num in line.split(" ")]
#             for i in range(range_length):
#                 s = range_start + i
#                 d = destination + i
#                 source_map[s] = d
    
            
    
#     print(source_map)

# def solve_part_2(input_data):
#     pass

import sys
import re
from collections import defaultdict
D = open("input/2023/day5.txt").read().strip()
L = D.split('\n')

parts = D.split('\n\n')
seed, *others = parts
seed = [int(x) for x in seed.split(':')[1].split()]

class Function:
  def __init__(self, S):
    lines = S.split('\n')[1:] # throw away name
    # dst src sz
    self.tuples: list[tuple[int,int,int]] = [[int(x) for x in line.split()] for line in lines]
    #print(self.tuples)
  def apply_one(self, x: int) -> int:
    for (dst, src, sz) in self.tuples:
      if src<=x<src+sz:
        return x+dst-src
    return x

  # list of [start, end) ranges
  def apply_range(self, R):
    A = []
    for (dest, src, sz) in self.tuples:
      src_end = src+sz
      NR = []
      while R:
        # [st                                     ed)
        #          [src       src_end]
        # [BEFORE ][INTER            ][AFTER        )
        (st,ed) = R.pop()
        # (src,sz) might cut (st,ed)
        before = (st,min(ed,src))
        inter = (max(st, src), min(src_end, ed))
        after = (max(src_end, st), ed)
        if before[1]>before[0]:
          NR.append(before)
        if inter[1]>inter[0]:
          A.append((inter[0]-src+dest, inter[1]-src+dest))
        if after[1]>after[0]:
          NR.append(after)
      R = NR
    return A+R

Fs = [Function(s) for s in others]

def f(R, o):
  A = []
  for line in o:
    dest,src,sz = [int(x) for x in line.split()]
    src_end = src+sz

P1 = []
for x in seed:
  for f in Fs:
    x = f.apply_one(x)
  P1.append(x)
print(min(P1))

P2 = []
pairs = list(zip(seed[::2], seed[1::2]))
for st, sz in pairs:
  # inclusive on the left, exclusive on the right
  # e.g. [1,3) = [1,2]
  # length of [a,b) = b-a
  # [a,b) + [b,c) = [a,c)
  R = [(st, st+sz)]
  for f in Fs:
    R = f.apply_range(R)
  #print(len(R))
  P2.append(min(R)[0])
print(min(P2))