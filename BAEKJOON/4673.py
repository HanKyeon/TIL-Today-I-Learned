'''
셀프 넘버

자신과 자신의 각 자리 수를 더하는 함수. ex d(75)  = 75 + 7 + 5
이 방식으로 무한 수열을 만들 수 있다. 예를 들어서
33, 39, 51, 57, 69, 84, 96, 111, 114, 120, 123, 129, 141, ...
이 때 앞 전 숫자를 생성자라고 한다.
이 때, 101은 생성자가 91과 100 두개ㅑ가 있다.
이 때, 생성자가 없는 숫자를 셀프 넘버라고 한다. 100보다 작은 셀프 넘버는 총 13개가 있따.
1 3 5 7 9 20 31 42 53 64 75 86 97
이 때, 10000보다 작거나 같은 셀프 넘버를 한 줄에 하나씩 출력하는 프로그램을 작성하시오.

입력
없음

출력
10000 이하 셀프 넘버를 한 줄에 하나씩 오름차순 출력
'''
def selfnum(num):
    d = 0
    nnum = num
    while nnum > 0:
        d += nnum % 10
        nnum = nnum // 10
    num += d
    if num <= 10000 :
        g[num] = False
        return selfnum(num)
    else:
        return
#dp 테이블
g = [False] + [True] * 10000
for i in range(1, len(g)):
    if g[i] == True:
        selfnum(i)
selnum =[idx for idx, v in enumerate(g) if v == True]
for s in selnum:
    print(s)








