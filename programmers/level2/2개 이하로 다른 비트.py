# 작은 비트부터 확인하여 0을 발견하면 1로 바꿔주고 그전 비트가 존재하면 0으로 바꿔주기
# 모든 비트가 1이면 최상위 비트를 0으로 바꾸고 최상위 비트 다음을 1로 바꾸기

def solution(numbers):
    result = []
    for n in numbers:
        bit = bin(n)[2:]
        for i in range(len(bit)-1, -1, -1):
            if bit[i] == '0':
                num = bit[:-1]+"1" if i == len(bit)-1 else bit[:i] + "10" + bit[i+2:]
                result.append(int("0b"+num, 2))
                break
        else:
            result.append(int("0b10" + bit[1:], 2))
    return result