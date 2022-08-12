numDictionary = {
    1: {"x":0, "y":0},
    2: {"x":1, "y":0},
    3: {"x":2, "y":0},
    4: {"x":0, "y":1},
    5: {"x":1, "y":1},
    6: {"x":2, "y":1},
    7: {"x":0, "y":2},
    8: {"x":1, "y":2},
    9: {"x":2, "y":2},
    "*": {"x":0, "y":3},
    0: {"x":1, "y":3},
    "#" : {"x":2, "y":3}
}

def calculateDistance(finger, number) :
    return abs(finger["x"]-number["x"]) + abs(finger["y"]-number["y"])
    
def solution(numbers, hand):
    left = numDictionary["*"]
    right = numDictionary["#"]
    
    result = ""
    for n in numbers:
        if n==1 or n==4 or n==7:
            left = numDictionary[n]
            result += "L"
        elif n==3 or n==6 or n==9:
            right = numDictionary[n]
            result += "R"
        else:
            if calculateDistance(left, numDictionary[n]) > calculateDistance(right, numDictionary[n]):
                right = numDictionary[n]
                result += "R"
            elif calculateDistance(left, numDictionary[n]) < calculateDistance(right, numDictionary[n]):
                left = numDictionary[n]
                result += "L"
            elif hand=="right":
                right = numDictionary[n]
                result += "R"
            elif hand=="left":
                left = numDictionary[n]
                result += "L"
    return result