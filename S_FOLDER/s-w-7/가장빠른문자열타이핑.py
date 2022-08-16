'''
가장 빠른 문자열 타이핑

문자열 A를 타이핑 한다.
한글자씩하면 A의 길이만큼 누름
어떤 문자열 B가 저장되어 있다면 원탭으로 입력 가능
이미 한 타이핑 못지움
A와 B가 주어질 때 A 전체를 타이핑 하기 위해 키를 눌러야 하는 횟수의 최솟값

입력
테케T
테케마다 A 1이상 10000이하 B 1이상 100이하 제시

출력
#1 각 테케마다 A 전체를 타이 하기 위해 키를 눌러야 하는 횟수의 최솟값
'''

for testcase in range(1, int(input())+1):
    s1, s2 = input().split()
    sl1, sl2, c, pl = len(s1), len(s2), 0, 0
    for i in range(sl1-sl2+1):
        if pl <= i:
            if s1[i:i+sl2] == s2:
                c += 1
                pl = i+sl2
    print(f"#{testcase} {sl1 - sl2 * c + c}")









