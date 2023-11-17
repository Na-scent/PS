import sys

n, m = map(int, sys.stdin.readline().split())
memo = []

for _ in range(n):
  memo.append(sys.stdin.readline().rstrip())

memo = set(memo)

for _ in range(m):
  
  tmp = set(list(map(str, sys.stdin.readline().rstrip().split(','))))
  memo -= tmp
  print(len(memo))
