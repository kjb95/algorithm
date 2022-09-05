def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key = lambda x: x*3, reverse=True)
    
    result = ""
    for n in numbers:
        result += n
    return str(int(result))
