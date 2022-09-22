def solution(s):
    removedZeroCount, convertCount = 0, 0
    while s != "1":
        convertCount += 1
        zeroCount = s.count("0")
        removedZeroCount += zeroCount
        s = bin(len(s)-zeroCount)[2:]
    return [convertCount, removedZeroCount]

print(solution("110010101001"))