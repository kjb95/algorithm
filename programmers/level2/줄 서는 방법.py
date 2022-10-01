# n의 경우의 수는 n!
# 13! 은 10억보다 크므로 모든 경우의수를 나열하면 숫자 초과
# k를 (n-1)!로 나눴을때의 몫과 나머지를 이용하여 값 구하기

import math

def solution(n, k):
    l = []
    k -= 1
    result = []
    for i in range(n):
        l.append(i+1)
    while len(l) > 0:
        q, r = divmod(k, math.factorial(len(l)-1))
        result.append(l[q])
        k = r
        del l[q]
    return result