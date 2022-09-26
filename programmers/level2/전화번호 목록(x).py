# 딕셔너리에 폰북 넣어두기
# 딕셔너리의 원소들 하나씩 해시를 이용해, 접두어가 있는지 확인

def solution(phone_book):
    hashMap = {}
    for phone in phone_book:
        hashMap[phone] = True
        
    for phone in phone_book:
        prefix = ""
        for c in phone:
            prefix += c
            if prefix != phone and prefix in hashMap:
                return False
    return True