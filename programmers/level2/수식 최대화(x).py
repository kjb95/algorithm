from itertools import permutations
import re

def solution(expression):
    permutation = list(permutations(["*", "-", "+"]))
    expression = re.split('([-*+])', expression)
    result = 0
    
    for operators in permutation:
        express = expression[:]
        for op in operators:
            while op in express:
                i = express.index(op)
                express[i-1] = str(eval(express[i-1]+express[i]+express[i+1]))
                del express[i:i+2]
        result = max(result, abs(int(express[0])))
    return result