# 스택에 prices 넣기
# 자기보다 작은값을 만나면 pop
# pop 당한 인덱스 - 본인 인덱스를 결과에 저장

def solution(prices):
    n = len(prices) 
    stack = []
    result = [0] * n
    for index, value in enumerate(prices):
        while len(stack) > 0 and stack[-1][1] > value:
            i, v = stack.pop()
            result[i] = index - i
        stack.append([index, value])
    while len(stack) > 0:
        i, v = stack.pop()
        result[i] = n-1-i
    return result