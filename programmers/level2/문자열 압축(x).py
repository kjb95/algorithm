# 다시풀기

def compressStr(s, unit):
    result = ""
    i = 0
    while i<len(s):
        sameStrCount = 0
        while s[i:i+unit] == s[i+unit:i+2*unit]:
            i += unit
            sameStrCount += 1
        if sameStrCount == 0:
            result += s[i:i+unit]
        else:
            result += str(sameStrCount+1)+s[i:i+unit]
        i += unit
    return result

def solution(s):
    result = [len(s)]
    for unit in range(1, len(s)//2+1):
        result.append(len(compressStr(s, unit)))
    return min(result)