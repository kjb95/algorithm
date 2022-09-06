from itertools import permutations

counter = set([])

def isPrime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if (n%i == 0):
            return False
    return True

def getPrime(expression):
    for p in permutations(expression, len(expression)):
        n = int("".join(p))
        if isPrime(n):
            counter.add(n)

def dfs(numbers, depth, expression):
    if len(numbers) == depth:
        if expression != "":
          getPrime(expression)
        return
    dfs(numbers, depth+1, expression+numbers[depth])
    dfs(numbers, depth+1, expression)
    
def solution(numbers):
    numbers = list(numbers)
    dfs(numbers, 0, "")
    return len(counter)