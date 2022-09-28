# 좌표간 이동경로를 리스트에 저장
# 이동경로를 모두 더하기

def solution(dirs):
    y, x = 0, 0
    s = set()
    dirX = {"L": -1, "R": 1, "U": 0, "D": 0}
    dirY = {"L": 0, "R": 0, "U": 1, "D": -1}
    for d in dirs:
        nextY = y+dirY[d]
        nextX = x+dirX[d]
        if nextX < -5 or nextX > 5 or nextY < -5 or nextY > 5:
            continue
        s.add((x, y, nextX, nextY))
        s.add((nextX, nextY, x, y))
        x = nextX
        y = nextY
    return len(s)//2