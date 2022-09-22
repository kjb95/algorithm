def solution(s):
    stack = []
    for c in s:
        stack.append(c)
        if len(stack) >= 2 and stack[-1] == stack[-2]:
            stack.pop()
            stack.pop()
    return 1 if len(stack) == 0 else 0