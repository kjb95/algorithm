def solution(clothes):
    countClothes = {}
    for cloth in clothes:
        if cloth[1] in countClothes:
            countClothes[cloth[1]] += 1
        else:
            countClothes[cloth[1]] = 1
    
    answer = 1
    for key in countClothes:
        answer *= (countClothes[key] + 1)
    return answer - 1