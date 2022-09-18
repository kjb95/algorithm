def solution(arr1, arr2):
    answer = [[0] * len(arr2[0]) for _ in range(len(arr1))]
    
    for arr1RawIndex in range(len(arr1)):
        for arr2ColIndex in range(len(arr2[0])):
            for index in range(len(arr1[0])):
                answer[arr1RawIndex][arr2ColIndex] += arr1[arr1RawIndex][index]*arr2[index][arr2ColIndex]
    return answer