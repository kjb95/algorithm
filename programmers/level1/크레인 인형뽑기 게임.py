def solution(board, moves):
    bucket = []
    result = 0
    for m in moves:
        m -= 1
        for y in range(len(board)):
            if (board[y][m] == 0):
                continue
            bucket.append(board[y][m])
            board[y][m] = 0
            break
        if len(bucket)>=2 and bucket[-1]==bucket[-2]:
            result += 2
            bucket.pop(-1)
            bucket.pop(-1)
    return result