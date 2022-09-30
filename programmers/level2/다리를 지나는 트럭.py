# 큐에 있는 모든 트럭의 무게 합과 새로 들어올 트럭의 합이 weight 이하이면 큐에 새로운 트럭과 다리 길이 값을 추가
# 1초마다 큐에 있는 모든 트럭의 다리 길이 값을 -1
# 큐안에 있는 다리 길이가 0 이되면 큐에서 빠져나옴
# 큐가 비어있으면 끝

def solution(bridge_length, weight, truck_weights):
    queue = []
    timer = []
    result = 0
    while True:
        result += 1
        allTruckWeight = sum(queue)
        if len(truck_weights) > 0 and allTruckWeight + truck_weights[0] <= weight:
            queue.append(truck_weights.pop(0))
            timer.append(bridge_length)
        if len(queue) == 0:
            break
        timer = list(map(lambda x:x-1, timer))
        while len(timer) > 0 and timer[0] == 0:
            queue.pop(0)
            timer.pop(0)
    return result
