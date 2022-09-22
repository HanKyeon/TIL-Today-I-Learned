'''
정식이의 은행 업무

정식이 실수함
송금 금액 까먹음
2진수 3진수 기억함
딱 하나 잘못 기억중

입력
테케T
2진수 표현
3진수 표현
'''
for tc in range(1, int(input())+1):
    n2, n3 = input(), input()
    g2 = [2**i for i in range(len(n2))]
    g3 = [3**i for i in range(len(n3))]+[3**j*2 for j in range(len(n3))]
    n2 = int(n2, 2)
    n3 = int(n3, 3)
    ans = 0
    for i in g2:
        for j in g3:
            if n2+i == n3-j:
                ans = n2+i
                break
            if n3+j == n2+i:
                ans = n3+j
                break
            if n2-i==n3-j:
                ans = n2-i
                break
            if n2-i == n3+j:
                ans = n2-i
                break
        if ans:
            break
    print(f"#{tc} {ans}")















