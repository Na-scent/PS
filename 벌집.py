import math
import sys
n = int(input())
cnt = 1
n -= 1
n = int(math.ceil(n/6))
for i in range(1, 1000000):
  if n < 1:
    print(cnt)
    sys.exit()
  cnt += 1
  n -= i
