def JadenCase(s):
    if (len(s) > 1):
        return s[0].upper() + s[1:len(s)].lower()
    else:
        return s.upper()

def solution(s):
    s = s.split(" ")
    return " ".join(list(map(JadenCase,s)))