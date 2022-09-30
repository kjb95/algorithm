# 1 1
# 2 2
# 10 3
# 11 11
# 12 12
# 20 13
# 21 21
# 22 22
# 100 23
# 101 31
# 102 32
# 110 33
# 111 111
# n의 최대 크기는 50,000,000 이므로 대략 수행 연산은 20번 이하 이어야 함

def convert124(n):
    if n == 0:
        return ""
    q, r = divmod(n, 3)
    if r == 0:
         return convert124((n-3)//3) + "4"
    return convert124(q) + str(r)

def solution(n):
    return(convert124(n))