# 블록을 뒤지며 2X2 형태로 붙어있는 블록발견시 붙어있는 모든 블록 제거
# 블록 정리
# 지워진 블록 세기

def solution(m, n, board):
    totalMap = []
    for b in board:
        totalMap.append(list(b))
    while True:
        deleteList = []
        for raw in range(m-1):
            for col in range(n-1):
                bucket = [totalMap[raw][col], totalMap[raw+1][col], totalMap[raw][col+1], totalMap[raw+1][col+1]]
                if totalMap[raw][col] != '0' and bucket.count(totalMap[raw][col]) == 4:
                    deleteList.append([raw, col])
                    deleteList.append([raw+1, col])
                    deleteList.append([raw, col+1])
                    deleteList.append([raw+1, col+1])
        if len(deleteList) == 0:
            break
        for dl in deleteList:
            raw, col = dl
            totalMap[raw][col] = '0'
        for col in range(n):
            for raw in range(m-1, 0, -1):
                findFilledRaw = raw
                while findFilledRaw >= 0 and totalMap[findFilledRaw][col] == '0':
                    findFilledRaw -= 1
                if findFilledRaw != raw and findFilledRaw >= 0:
                    totalMap[raw][col], totalMap[findFilledRaw][col] = totalMap[findFilledRaw][col], '0'
    result = 0
    for mapRaw in totalMap:
        result += mapRaw.count('0')
    return result