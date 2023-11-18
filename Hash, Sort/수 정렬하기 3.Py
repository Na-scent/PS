import sys
import collections

n = int(input())
hash = {}

for _ in range(n):
  tmp = int(sys.stdin.readline())
  if tmp in hash.keys():
    hash[tmp] += 1
  else:
    hash[tmp] = 1


od = collections.OrderedDict(sorted(hash.items()))

for i, j in od.items():
  for _ in range(j):
    print(i)
  

