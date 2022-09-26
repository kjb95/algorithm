# 문자열을 2개씩 쪼개기
# 교집합, 합집합 구하기

def openStr(string):
    result = {}
    for i in range(0, len(string)-1):
        s = string[i:i+2].lower()
        if not s.isalpha():
            continue
        if s in result:
            result[s] += 1
        else:
            result[s] = 1
    return result

def solution(str1, str2):
    opendStr1 = openStr(str1)
    opendStr2 = openStr(str2)
    union = {}
    intersection = {}
    
    for key, value in opendStr1.items():
        union[key] = value
        if key in opendStr2:
            intersection[key] = min(opendStr2[key], value)
    for key, value in opendStr2.items():
        if key in union:
            union[key] = max(value, union[key])
        else:
            union[key] = value

    if sum(union.values()) == 0:
        return 65536
    return int(sum(intersection.values())/sum(union.values()) * 65536)
        