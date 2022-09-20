'''
이진수2

0이상 1미만 십진수 n을 이진수로 바꾸려 한다. 예를 들어 0.625는 0.101이 된다.
N을 소수점 아래 12자리 이내인 이진수로 표시할 수 있으면 0.을 제외한 나머지 숫자를 출력하고, 13자리 이상이 필요한 경우에는 ‘overflow’를 출력하는 프로그램을 작성하시오.

입력
테케
n

출력
#테케 답
'''
cz = [2 ** (-i) for i in range(1, 13)]
for tc in range(1, int(input())+1):
    num, ans=float(input()), ''
    for i in range(12):
        if num == 0:break
        if num>=cz[i]:num-=cz[i];ans+='1';continue
        ans += '0'
    if num > 0:ans = 'overflow'
    print(f"#{tc} {ans}")







