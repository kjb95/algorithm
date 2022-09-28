# 이차원 배열의 행을 i, 열을 j라 하면, dp[i][j]는 i번째에 j땅을 밟았을때의 최대값을 의미
# 배열의 마지막 행의 값들 중 최대값을 구하면 됨

def solution(land):
    rawN = len(land)
    colN = len(land[0])
    dp = [[0] * colN for _ in range(rawN+1)]
    for i in range(1, rawN+1):
        for j in range(colN):
            for k in range(colN):
                if j == k:
                    continue
                dp[i][j] = max(dp[i][j], dp[i-1][k]+land[i-1][j])
    return max(dp[rawN])