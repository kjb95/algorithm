# 스택에 순서대로 넣으며 스택위보다 작은수가 들어오면 넣고, 큰수가 들어오면 안에 있는 수 빼기
# 작업횟수 100 이하로

def solution(number, k):
    stack = []
    for n in number:
        while stack and k > 0 and stack[-1] < n:
            k -= 1
            stack.pop()
        stack.append(n)
    return "".join(stack[:len(stack)-k])