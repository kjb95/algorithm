def countUpDown(c):
    if c <= 'N':
        return ord(c) - ord('A')
    else:
        return ord('Z') - ord(c) + 1

def dfs(name, index, depth):
    global countLR
    if depth >= countLR:
        return
    
    name = name[:index] + 'A' + name[index+1:]
    if all(n == 'A' for n in name):
        countLR = min(countLR, depth)
    
    if (index == len(name)-1):
        dfs(name, 0, depth+1)
    else:
        dfs(name, index+1, depth+1)
    if index == 0:
        dfs(name, len(name)-1, depth+1)
    else:
        dfs(name, index-1, depth+1)
    
def countLeftRight(name):
    global countLR
    countLR = len(name) - 1
    dfs(name, 0, 0)
    return countLR

def solution(name):
    result = 0
    for c in name:
        result += countUpDown(c)
    result += countLeftRight(name)
    return result