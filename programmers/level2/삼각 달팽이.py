# 숫자는 세가지 방법으로 나열됨
    # 1. y 방향으로 +1
    # 2. x 방향으로 +1
    # 3. y 방향으로 -1, x 방향으로 -1
# 나열되는 숫자는 1씩 줄어듬

def solution(n):
    arr = [[0] * n for _ in range(n)]
    x, y = 0, -1
    number = 0
    for i in range(n):
        for j in range(n-i):
            number += 1
            if i%3 == 0:
                y += 1
            elif i%3 == 1:
                x += 1
            else:
                x -= 1
                y -= 1
            arr[y][x] = number
    result = []
    for raw in arr:
        for number in raw:
            if number == 0:
                break
            result.append(number)
    return result