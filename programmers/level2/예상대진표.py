def solution(n,a,b):
    stack = [i for i in range(1, n+1)]
    result = 0
    while len(stack) > 2:
        result += 1
        temp = []
        for i in range(0, len(stack), 2):
            if stack[i] == a and stack[i+1] == b or stack[i] == b and stack[i+1] == a:
                return result
            if (stack[i] == a or stack[i] == b):
                temp.append(stack[i])
            else:
                temp.append(stack[i+1])
        stack = temp
    return result+1