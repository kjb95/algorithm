# 모든 던전을 돌며 최대값 찾기

result = 0

def dfs(depth, k, dungeons):
    global result
    result = max(result, depth)
    for i, v in enumerate(dungeons):
        need, use = v
        if (k >= need):
            dungeons.pop(i)
            dfs(depth+1, k-use, dungeons)
            dungeons.insert(i, v)

def solution(k, dungeons):
    global result
    dfs(0, k, dungeons)
    return result