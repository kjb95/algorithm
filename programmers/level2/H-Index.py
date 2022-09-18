def solution(citations):
    for hIndex in range(max(citations), -1, -1):
        count = 0
        for citation in citations:
            if hIndex <= citation:
                count += 1
        if hIndex <= count:
            return hIndex