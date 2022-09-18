def solution(n):
    result = [0] * 100001
    result[1] = 1
    for i in range(2, n+1):
        result[i] = (result[i-1] + result[i-2])%1234567
    return result[n]