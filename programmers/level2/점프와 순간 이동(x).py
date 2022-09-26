# 1. n을 2로 나누기
# 2. n을 더이상 2로 나눌수 없으면 1을 더하거나 1로 빼서 또다시 2로 나누기
# 3. 1을 더하거나 빼서 0으로 도달할 때까지의 최소값을 구하기

result = 987654321

def solve(n, depth):
    global result
    if (depth >= result):
      return
    if (n < 1):
        result = min(result, depth)
        return
    if (n % 2 == 0):
        solve(n//2, depth)
    else:
        solve(n-1, depth+1)

def solution(n):
    solve(n, 0)
    return result