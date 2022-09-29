# 모든 경우의수를 딕셔너리에 저장
    # 문자열이 크기가 5 미만이면, 문자열에 A추가
    # 문자열의 크기가 5 이면, 문자열의 끝값 올리기
    # 문자열의 마지막 문자열이 U이면, 마지막 문자열을 지우고 마지막 전 문자열 값 올리기
    # 문자열의 마지막이 문자열이 U가 아니면, 마지막 문자열 끝값 올리기
    
def solution(word):
    alphaDic = {"A":0, "E":1, "I":2, "O":3, "U":4, 0:"A", 1:"E", 2:"I", 3:"O", 4:"U"}
    dic = {"A": 1}
    w = "A"
    v = 1
    while w != "UUUUU":
        if len(w) < 5:
            w += "A"
        else:
            findNotUIndex = len(w)-1
            while w[findNotUIndex] == "U":
                findNotUIndex -= 1
            w = w[:findNotUIndex] + alphaDic[alphaDic[w[findNotUIndex]]+1]
        v += 1
        dic[w] = v
    return dic[word]