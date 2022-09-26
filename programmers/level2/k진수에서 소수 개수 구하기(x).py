# 숫자 n을 k 진수로 바꾸기
# k진수를 처음부터 돌며 소수 개수 찾기
    # 0을 만날때까지 돌기
    # 0 전까지 그 숫자가 소수인지 판별

def convert(n, k):
    if (n == 0):
        return ""
    q = n // k
    r = n % k
    return convert(q, k) + str(r)

def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
    
def solution(n, k):
    num = convert(n, k)
    numbers = num.split('0')
    result = 0
    for number in numbers:
        if number != '' and isPrime(int(number)):
            result += 1
    return result