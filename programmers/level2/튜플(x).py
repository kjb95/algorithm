from collections import Counter

def solution(s):
    s = s.lstrip("{{").rstrip("}}").split("},{")
    counter = []
    for strs in s:
        for str in strs.split(","):
            counter.append(str)
                  
    counter = Counter(counter).items()
    counter = sorted(counter, key=lambda x:x[1], reverse=True)
    result = []
    for i in counter:
        result.append(int(i[0]))
    return result