# n진법 숫자를 0부터 크기가 m*t까지 구하기
# 구한 숫자를 m으로 나눈 나머지가 p-1인 값만 결과에 추가하기

def baseCalculate(base, n):
    if n == 0:
        return ""
    string = "0123456789ABCDEF"
    q = n // base
    r = n % base
    return str(baseCalculate(base, q)) + string[r]

def solution(n, t, m, p):
    bucket = "0"
    i = 0
    while len(bucket) <= m*t:
        i += 1
        baseNumber = baseCalculate(n, i)
        bucket += baseNumber
    
    result = ""
    for i in range(t):
        result += bucket[i*m + p-1]
    return result