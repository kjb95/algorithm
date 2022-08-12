def solution(n, lost, reserve):
    arr = [1] * n
    for l in lost:
        arr[l-1] = 0
    for r in reserve:
        arr[r-1] += 1
    
    for i, student in enumerate(arr):
        if student != 2:
            continue
        if i==0: 
            if arr[i+1]==0:
                arr[i+1] = 1
        elif i==len(arr)-1:
            if arr[i-1]==0:
                arr[i-1] = 1
        else:
            if arr[i-1]==0:
                arr[i] = 1
                arr[i-1] = 1
            elif arr[i+1]==0:
                arr[i+1] = 1
    return n - arr.count(0)