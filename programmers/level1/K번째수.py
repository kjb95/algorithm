def solution(array, commands):
    result = []
    for cmd in commands:
        arr = array[cmd[0]-1:cmd[1]]
        arr.sort()
        result.append(arr[cmd[2]-1])
    return result