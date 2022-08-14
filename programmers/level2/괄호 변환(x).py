# 다시 풀기

from collections import Counter

def isBalancedStr(s):
    if Counter(s)["("] == Counter(s)[")"]:
        return True
    return False

def isCorrectStr(string):
    top = 0
    for s in string:
        top = top+1 if s == "(" else top-1
        if top < 0:
            return False
    return True  

def invertStr(string):
    result = ""
    for s in string:
        result = result+"(" if s==")" else result+")"
    return result

def getCollectStr(s1, s2):
    if s2 == "":
        return s1
    
    i = 0
    for i in range(len(s2)):
        u = s2[:i+1]
        v = s2[i+1:]
        if not isBalancedStr(u):
            continue
        if isCorrectStr(u):
            return getCollectStr(s1 + u, v)
        return s1 + "(" + getCollectStr("", v) + ")" + invertStr(u[1:-1])

def solution(p):
    return getCollectStr("", p)