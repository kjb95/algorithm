def solution(record):
    nicknameDictionary = {}
    for r in record:
        data = r.split()
        if data[0] == "Enter" or data[0] == "Change":
            nicknameDictionary[data[1]] = data[2]
    
    result = []
    for r in record:
        data = r.split()
        nickname = nicknameDictionary[data[1]]
        if data[0] == "Enter":
            result.append(nickname + "님이 들어왔습니다.")
        elif data[0] == "Leave":
            result.append(nickname + "님이 나갔습니다.")
    return result 