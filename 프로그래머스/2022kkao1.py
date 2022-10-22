def solution(n, k):
    answer = -1
    def makek(val):
        if not val:
            return ''
        return makek(val//k)+ str(val%k)
    a = makek(n)
    print(a)
    return answer

solution(1000000, 3)