# 배열의 인덱스를 n으로 나눴을때 몫을 a, 나머지를 b 라하면
# a <= b 이면, 값은 b+1
# a > b 이면, 값은 a+1

def solution(n, left, right):
    result = []
    for i in range(left, right+1):
        a = i // n
        b = i % n
        if a <= b:
            result.append(b+1)
        else:
            result.append(a+1)
    return result