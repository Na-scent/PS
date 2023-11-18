
# 힙의 작동원리만 이해하고 내장 라이브러리 사용 방법 숙지

import heapq
import sys

n = int(input())
heap = []

for _ in range(n):
  command = int(sys.stdin.readline())
  if command == 0:
    if len(heap) == 0:
      print(0)
    else:
      print(heapq.heappop(heap))
  else:
    heapq.heappush(heap, command)
