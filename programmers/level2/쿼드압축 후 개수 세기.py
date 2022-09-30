# n의 최대 크기는 50,000,000 이므로 대략 수행 연산은 20번 이하 이어야 함
# 124진법으로 변환했을때 숫자 크기 구하기

def solution(n):
    size124 = 0
    threeSquare = 1
    bucket = 0
    while True:
        bucket += threeSquare
        if bucket > n:
            break
        size124 += 1
        threeSquare *= 3
        
    result = ""
    dic = {1:"1", 2:"2", 3:"4"}
    for i in range(size124-1, -1, -1):
        q, r = divmod(n, 3**i)
        subValue = 3 if q > 3 else q
        n -= (3**i)*subValue
        result += dic[subValue]
    return result
for i in range(10):
  print(solution(i))