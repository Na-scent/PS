import sys

n, m = map(int, input().split())
dic = {}
for _ in range(n):
  word = sys.stdin.readline().rstrip()
  # 길이 확인
  if m <= len(word):
    # 사전에 있는지 확인.
    if word in dic.keys():
      dic[word] += 1
    else:
      dic[word] = 1

# set은 순서대로 정렬해줌
values = list(set(dic.values()))

result = []
# 배열 역으로 슬라이싱
for value in values[::-1]:
  keys = list(k for k, v in dic.items() if v == value)
  # 두 가지 조건으로 정렬
  keys.sort()
  keys.sort(key=len, reverse=True)
  result.extend(keys)

for i in result:
  print(i)