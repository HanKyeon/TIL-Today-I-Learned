def solution(n, s):
    answer = []
    if n > s: return [-1]
    num = s//n
    while len(answer) < n-1:
        answer.append(num if len(answer) < n-1 else s)
        s -= num
    idx = len(answer)-1
    while s-num > 1:
        s -= 1
        answer[idx] += 1
        idx -= 1
    answer.append(s)
    return answer