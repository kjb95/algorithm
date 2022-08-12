# 다시 풀기

def solution(N, stages):
    notClearList = [0] * (N+1)
    for stage in stages:
        notClearList[stage-1] += 1

    totalList = [0] * N
    failRateList = {}
    for i in range(N):
        if i == 0:
            totalList[i] = len(stages)
        else:
            totalList[i] = totalList[i-1] - notClearList[i-1]
        failRateList[i+1] = 0 if totalList[i] == 0 else notClearList[i]/totalList[i]

    return sorted(failRateList, key=lambda x: failRateList[x], reverse=True);

a = solution(5, [2, 1, 2, 6, 2, 4, 3, 3]);
for i in a:
    print(i)