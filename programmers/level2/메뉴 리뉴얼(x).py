# 다시풀기

from itertools import combinations

def solution(orders, courses):
    countMax = [0] * 11
    count = {}
    for order in orders:
        order = sorted(order)
        for course in courses:
            for combination in combinations(list(order), course):
                unify = "".join(str for str in combination)
                if unify in count:
                    count[unify] += 1
                else:
                    count[unify] = 1
                countMax[course] = max(countMax[course], count[unify])
    
    result = []
    for key, value in count.items():
        if countMax[len(key)] == value and value > 1:
            result.append(key)
    result.sort()
    return result