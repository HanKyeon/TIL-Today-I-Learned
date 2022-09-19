'''
단순 이진 암호 코드

1. 8개 숫자.
2. 앞 7자리는 상품 고유 번호 마지막은 검증 코드

검증 코드는 홀수자리합*3 + 짝수자리합 + 검증 코드 가 10의 배수가 되어야 한다.
상품 고유 번호가 8801234일 경우
((8+0+2+4)*3 + 8+1+3+ 검증코드) % 10 == 0
검증코드는 6이어야 한다. 즉 88012346이 정상 암호코드이다.

1. 세로 50. 가로 100 이하의 크기를 가진 직사각형 배열에 암호코드 정보가 포함되어 전달된다. 이 때, 하나의 배열에는 1개의 암호코드가 존재한다. (단, 모든 암호코드가 정상적인 암호코드임을 보장할 수 없다. 비정상적인 암호코드가 포함될 수 있다.)

2. 배열은 1, 0으로 이루어져 있으며 그 안에 포함되어 있는 암호코드 정보를 확인한다.

3. 포함된 암호코드들의 검증코드를 확인하여 정상적인 암호코드인지 확인한다.

4. 정상적인 암호코드들을 판별한 뒤 이 암호코드들에 적혀있는 숫자들의 합을 출력한다.

5. 이때, 총 소요시간이 적을수록 성능이 좋은 것으로 간주된다.


1. 암호코드 하나는 숫자 8개로 구성되며 시작 구분선, 종료 구분선은 별도로 존재하지 않는다.

2. 암호코드가 일부만 표시된 경우는 없다. 모든 암호코드는 8개의 숫자로 구성되어 있다.

3. 암호코드의 세로 길이는 5 ~ 50 칸이다.

4. 암호코드의 가로 길이는 총 길이는 56칸이다. 암호코드에 구성하는 숫자 하나가 차지하는 길이는 7칸이다. 각 숫자들을 그림으로 표시하는 방법은 다음과 같다.

암호코드 정보가 포함된 2차원 배열을 입력으로 받아 정상적인 암호코드를 판별하는 프로그램을 작성하라.

입력
테케수
n, m 제시. 1이상 50이하 1이상 100이하 세로n 가로m
배열 제시.

출력
#테케T 테케 답을 순서대로 표준 출력으로 출력.
'''
di = {(0,0,0,1,1,0,1):0, (0,0,1,1,0,0,1):1, (0,0,1,0,0,1,1):2, (0,1,1,1,1,0,1):3, (0,1,0,0,0,1,1):4, (0,1,1,0,0,0,1):5, (0,1,0,1,1,1,1):6, (0,1,1,1,0,1,1):7, (0,1,1,0,1,1,1):8, (0,0,0,1,0,1,1):9}

def check(li):
    hol, zzak = 0, 0
    for i in range(8):
        if i%2:
            hol += li[i]
        else:
            zzak += li[i]
    if (zzak*3 + hol)%10:
        return 0
    else:
        return sum(li)

for testcase in range(1, int(input())+1):
    n, m = map(int, input().rstrip().split())
    g = [list(input()) for _ in range(n)]
    for i in g:
        if '1' in i:
            a = i
            break
        else:
            continue
    while a[-1] == '0':
        a = a[:-1]
    while a[0] == '0':
        a = a[1:]
    while len(a) % 7:
        a = ['0']+a
    ans = []
    for i in range(0, len(a), 7):
        na = tuple(map(int, a[i:i+7]))
        ans.append(di[na])
    print(f"#{testcase} {check(ans)}")









