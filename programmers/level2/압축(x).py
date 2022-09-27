# 모든 알파벳 딕셔너리에 넣기
# 반복문으로 문자열 순회
    # 딕셔너리에 값이 있을때 까지 확인
    # 값을 출력하고 다음 단어 까지 사전에 등록
    # 출력한 값은 문자열에서 제거
    
def solution(msg):
    dictionary = {}
    for i in range(26):
        dictionary[chr(ord('A')+i)] = i+1

    result = []
    endIndex = 0
    while endIndex < len(msg):
        endIndex += 1
        if msg[:endIndex+1] in dictionary:
            continue
        result.append(dictionary[msg[:endIndex]])
        dictionary[msg[:endIndex+1]] = len(dictionary)+1
        msg = msg[endIndex:]
        endIndex = 0
    result.append(dictionary[msg])
    
    return result
