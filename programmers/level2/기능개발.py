import math

def solution(progresses, speeds):
    remainDays = []
    for p, s in zip(progresses, speeds):
        remainDays.append(math.ceil((100 - p) / s))
    
    maxValue = remainDays[0]
    count = 0
    result = []
    for i, r in enumerate(remainDays):
        if max(r, maxValue) != maxValue:
            maxValue = r
            result.append(count)
            count = 1
        else:
            count += 1
        if i == len(remainDays)-1:
            result.append(count)
    return result