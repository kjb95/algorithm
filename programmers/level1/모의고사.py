def solution(answers):
    answerCount = [0] * 3
    oneList = [1, 2, 3, 4, 5]
    twoList = [2, 1, 2, 3, 2, 4, 2, 5]
    threeList = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    for i, answer in enumerate(answers):
        one = oneList[i%5]
        two = twoList[i%8]
        three = threeList[i%10]

        if (answer == one):
            answerCount[0] += 1
        if (answer == two):
            answerCount[1] += 1
        if (answer == three):
            answerCount[2] += 1
    
    result = []
    for i, count in enumerate(answerCount):
        if count == max(answerCount):
            result.append(i+1)
    return result