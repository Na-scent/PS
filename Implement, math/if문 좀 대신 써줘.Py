# 디버깅 신경쓰기

import sys

n, m = map(int, input().split())
t, p = map(str, input().split())

titleList = [t]
powerList = [int(p)]

for _ in range(n-1):
  t, p = map(str, sys.stdin.readline().split())
  if int(p) != powerList[-1]:
    titleList.append(t)
    powerList.append(int(p))
    
length = len(titleList)

def bSearch(list, power, s, e):
  # 끝에 도달했을 때
  if abs(e-s) <= 1:
    if powerList[s] < power <= powerList[e]:
      return titleList[min(e, length)]
    else:
      return titleList[s]
  
  idx = (s+e)//2
  
  # idx범위에 있을 때 
  if list[idx-1] < power <= list[idx]:
    return titleList[idx]
  
  
  # idx보다 큰 범위에 있을 때 
  elif list[idx] < power:
    return bSearch(list, power, idx+1, e)
  
  # idx보다 작은 범위에 있을 때
  else: 
    return bSearch(list, power, s, idx-1)
    
for _ in range(m):
  print(bSearch(powerList, int(sys.stdin.readline()), 0, length))
  
  
  