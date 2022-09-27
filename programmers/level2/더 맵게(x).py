# 모든 음식이 스코빌 지수가 k 이상일 때까지 섞기

import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    result = 0
    while scoville[0] < K:
        if len(scoville) < 2:
            return -1
        result += 1
        a = heapq.heappop(scoville)
        b = heapq.heappop(scoville)
        heapq.heappush(scoville, a+2*b)
    return result