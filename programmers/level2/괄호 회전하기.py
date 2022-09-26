# s 크기만큼 반복문 돌리기
# 해당 문자열이 스택을 이용하여 올바른 괄호인지 확인

def isRight(s):
    stack = []
    for c in s:
        if c == '[' or c == '(' or c == '{':
            stack.append(c)
        else:
            if len(stack) == 0:
                return False
            elif c == ']':
                if stack[-1] == '[':
                    stack.pop()
                else:
                    return False
            elif c == ')':
                if stack[-1] == '(':
                    stack.pop()
                else:
                    return False
            elif c == '}':
                if stack[-1] == '{':
                    stack.pop()
                else:
                    return False
    if len(stack) == 0:
        return True
    return False

def solution(s):
    strArr = []
    for element in s:
        strArr += element
    result = 0
    for _ in range(len(s)):
        firstData = strArr.pop(0)
        strArr.append(firstData)
        if isRight(strArr):
            result += 1
    return result