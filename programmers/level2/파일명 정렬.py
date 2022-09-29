# 커스텀 정렬 함수 만들기
# 문자열을 헤드, 넘버, 테일로 쪼개기

def solution(files):
    bucket = []
    for file in files:
        state = 0
        head, number, tail = "", "", ""
        for c in file:
            if state == 0 and c.isdigit():
                state = 1
            if state == 1 and not c.isdigit():
                state = 2
            if state == 0:
                head += c
            elif state == 1:
                number += c
            else:
                tail += c
        bucket.append([head, number, tail])
    bucket.sort(key=lambda x : [x[0].lower(), int(x[1])])
    for i in range(len(bucket)):
        bucket[i] = bucket[i][0] + bucket[i][1] + bucket[i][2]
    return bucket