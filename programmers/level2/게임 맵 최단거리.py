# dfs로 거리의 모든 경우의 수를 세어 최단거리 구하기
# 이미 방문한 곳 체크하기

# dfs는 도착해도 다른 최단거리가 있는지 찾아야 하므로 시간초과가 날 수 있음
# bfs로 풀기

def solution(maps):
    n, m = len(maps[0]), len(maps)
    dx, dy = [1, 0, 0, -1], [0, 1, -1, 0]
    shortestDistance = [[987654321] * n for _ in range(m)]
    shortestDistance[0][0] = 1
    queue = [[0, 0]]
    while True:
        y, x = queue.pop(0)
        if x == n-1 and y == m-1:
            return shortestDistance[y][x]
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=m or maps[ny][nx]==0 or shortestDistance[ny][nx] <= shortestDistance[y][x]+1:
                continue
            queue.append([ny, nx])
            shortestDistance[ny][nx] = shortestDistance[y][x]+1
        if len(queue) == 0:
            break
    return -1
    