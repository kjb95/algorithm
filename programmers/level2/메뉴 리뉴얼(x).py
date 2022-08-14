# 다시풀기

from itertools import combinations
from collections import Counter

def solution(orders, courses):
    countMax = [0] * 11
    menuCombinations = []
    for order in orders:
        order = sorted(order)
        for course in courses:
            for combination in combinations(list(order), course):
                menuCombinations.append("".join(combination))
    
    for key, value in Counter(menuCombinations).items():
        countMax[len(key)] = max(countMax[len(key)], value)
    
    result = []
    for key, value in Counter(menuCombinations).items():
        if countMax[len(key)] == value and value > 1:
            result.append(key)
    result.sort()
    return result