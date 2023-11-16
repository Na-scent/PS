s = input()
length = len(s)
zNum = s.count('0')
oNum = length - zNum
newString = ''

cnt = 0
idx = 0
for i in range(length):
  if cnt == oNum//2:
    newString += s[idx:]
    break

  if s[i] == '1':
    newString += s[idx : i]
    idx = i+1
    cnt +=1
    
# ---------------------------

cnt = 0
idx = len(newString)
newString2 = ''

for i in range(len(newString)-1, -1, -1):
  if cnt == zNum//2:
    newString2 = newString[:idx] + newString2
    break
  
  if newString[i] == '0':
    newString2 = newString[i+1: idx] + newString2
    idx = i
    cnt += 1
print(newString2)
ㄴ