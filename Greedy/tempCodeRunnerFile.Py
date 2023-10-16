import sys
num = input()
number = 1
result = 0
idx = 0


for i in range(1, 3001):
  # 포함할 때 
  if num[idx] in str(i):
    idx2 = str(i).index(num[idx])+1
    idx += 1
    while idx < len(num) and idx2 < len(str(i)) and num[idx] in str(i)[idx2:]:
      idx2 += 1
      idx += 1

  if idx == len(num):
    print(i)
    sys.exit()
    
    