# 현재 스킬을 가리키는 인덱스 선언
# 스킬에 있는 문자인데 현재스킬을 가리키는 문자가 아니면 실패

def solution(skill, skill_trees):
    result = 0
    for st in skill_trees:
        skillOrder = 0
        for s in st:
            if s in skill:
                if s != skill[skillOrder]:
                    break
                skillOrder += 1
        else:
            result += 1
    return result