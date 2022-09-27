# records를 돌며 딕셔너리를 이용해 각 차들의 이용시간 저장

import math

def convert(s):
    minute, second = s.split(":")
    return int(minute) * 60 + int(second)

def calculateFee(fees, value):
    basicTime, basicFee, unitTime, unitFee = fees
    if basicTime >= value:
        return basicFee
    return (math.ceil((value - basicTime) / unitTime) * unitFee + basicFee)

def solution(fees, records):
    parkingInside = {}
    parkingOutside = {}
    for record in records:
        time, number, command = record.split(" ")
        if command == "IN":
            parkingInside[number] = convert(time)
        else:
            if number in parkingOutside:
                parkingOutside[number] += (convert(time) - parkingInside[number])
            else:
                parkingOutside[number] = (convert(time) - parkingInside[number])
            parkingInside.pop(number)
            
    for key, value in parkingInside.items():
        if key in parkingOutside:
            parkingOutside[key] += (convert("23:59") - value)
        else:
            parkingOutside[key] = (convert("23:59") - value)
    
    for key, value in parkingOutside.items():
        parkingOutside[key] = calculateFee(fees, value)
        
    answer = []
    for po in sorted(parkingOutside.items()):
        answer.append(po[1])
    return answer