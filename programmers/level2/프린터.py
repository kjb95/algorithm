def getMax(queue):
    result = 0
    for q in queue:
        result = max(result, q[1])
    return result

def solution(priorities, location):
    queue = []
    for i, v in enumerate(priorities):
        queue.append([i, v])
    
    order = 0
    while queue:
        maxValue = getMax(queue)
        front = queue.pop(0)
        if front[1] == maxValue:
            order += 1
            if front[0] == location:
                return order
        else:
            queue.append(front)
    return order
  
print(solution([1, 1, 9, 1, 1, 1], 0))