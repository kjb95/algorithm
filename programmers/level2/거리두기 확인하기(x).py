isPass = 0
visit = 0

def dfs(p, y, x, d):
  global isPass, visit
  dy = [-1, 1, 0, 0]
  dx = [0, 0, -1, 1]
  if d > 2 or not isPass:
    return

  visit[y][x] = True
  if d > 0 and p[y][x] == 'P':
    isPass = 0
    return

  for i in range(4):
    ny = y + dy[i]
    nx = x + dx[i]
    if ny < 0 or ny > 4 or nx < 0 or nx > 4 or visit[ny][nx] == 1 or p[ny][nx] == 'X':
      continue
    dfs(p, ny, nx, d+1)

def checkDistance(p):
  global isPass
  isPass = True
  global visit
  visit = [[False] * 5 for _ in range(5)]
  
  for y in range(5):
    for x in range(5):
      if p[y][x] == 'P':
        dfs(p, y, x, 0)
  return isPass

def solution(places):
  result = []
  for p in places:
    if checkDistance(p):
      result.append(1)
    else:
      result.append(0)
  return result