# 리스트를 사용하여 도시 넣기
# 최대 크기를 넘으면 먼저 들어간 도시 빼기

def solution(cacheSize, cities):
    if cacheSize == 0:
        return 5 * len(cities)
    cash = []
    result = 0
    for city in cities:
        city = city.lower()
        if city in cash:
            cash.remove(city)
            result += 1
        else:
            if len(cash) == cacheSize:
                cash.pop(0)
            result += 5
        cash.append(city)
    return result