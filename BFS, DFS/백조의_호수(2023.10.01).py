# --------------------------------------------------------------------------------------------------------------------------------

# 문제

# 두 마리의 백조가 호수에서 살고 있었다. 그렇지만 두 마리는 호수를 덮고 있는 빙판으로 만나지 못한다.

# 호수는 행이 R개, 열이 C개인 직사각형 모양이다. 어떤 칸은 얼음으로 덮여있다.

# 호수는 차례로 녹는데, 매일 물 공간과 접촉한 모든 빙판 공간은 녹는다. 두 개의 공간이 접촉하려면 가로나 세로로 닿아 있는 것만 (대각선은 고려하지 않는다) 생각한다.

# --------------------------------------------------------------------------------------------------------------------------------

# 입력

# 입력의 첫째 줄에는 R과 C가 주어진다. 단, 1 ≤ R, C ≤ 1500.

# 다음 R개의 줄에는 각각 길이 C의 문자열이 하나씩 주어진다. '.'은 물 공간, 'X'는 빙판 공간, 'L'은 백조가 있는 공간으로 나타낸다.

# --------------------------------------------------------------------------------------------------------------------------------

# 출력

# 걸리는 날을 출력한다. 

# --------------------------------------------------------------------------------------------------------------------------------

import copy
from collections import deque
import sys

# matrix data 전처리
# 각 발판마다 녹을 때까지 얼마나의 시간이 걸리는지에 대한 Matrix 생성
def days(matrix):
  queue = deque()
  
  # 물 공간은 처음부터 백조가 지나다닐 수 있으니 0
  for i in range(R):
    for j in range(C):
      if matrix[i][j] == "." or matrix[i][j] == "L":
        matrix[i][j] = 0
        queue.append([i, j])
  
  # BFS 진행
  while queue:
    x, y = queue.popleft()
    for i in range(4):
      u, v = x + dx[i], y + dy[i]
      if 0<= u < R and 0 <= v < C and matrix[u][v] == "X":
        matrix[u][v] = matrix[x][y] + 1
        queue.append([u, v])
  return matrix

matrix = []
swan_pos = []
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1] # 좌, 우, 상, 하

# input
R, C = map(int, input().split())

# matrix 생성 및 백조 위치 저장
for i in range(R):
  ip = input()
  matrix.append(list(ip))
  idx = ip.find("L")
  if idx != -1:
    swan_pos.append([i, idx])
  idx = ip.find("L", idx+1)
  if idx != -1:
    swan_pos.append([i, idx])

matrix = days(matrix)
visited = [[0 for _ in range(C)] for _ in range(R)]

# 몇 일만에 백조가 만나는지에 대한 변수
day = 0

# 하루가 지나야 갈 수 있는 위치를 저장하는 queue
next_queue = deque()
next_queue.append(swan_pos[0])

while True:  
  # while문을 한 번 돌 때 하루가 지남
  # next day queue를 today queue로 옮겨줌
  queue = copy.deepcopy(next_queue)
  # next queue 초기화
  next_queue = deque()
  
  while queue:
    x, y = queue.popleft()
    visited[x][y] = 1
    
    for i in range(4):
      u, v = x + dx[i], y + dy[i]
      if 0 <= u < R and 0 <= v < C and visited[u][v] == 0:
        # 찾았을 때        
        if [u, v] == swan_pos[1]:
          print(day)
          sys.exit()
        
        # 못 찾았을 때
        visited[u][v] = 1
        # 오늘 이동할 수 있는 곳이면 today queue에 삽입
        if matrix[u][v] <= day:
          queue.append([u, v])
        # 내일 이동할 수 있는 곳이면 next queue에 삽입
        else:
          next_queue.append([u, v])
  # 오늘 이동할 수 있는 곳을 다 이동했음에도 백조를 찾지 못했다면, 다음날로 이동
  day += 1
