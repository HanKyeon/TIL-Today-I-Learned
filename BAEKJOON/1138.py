'''
한 줄로 서기

N명의 사람이 줄 선다. 오민식 맘대로
사람들은 자기보다 큰 사람이 왼쪽에 몇 명 있었는지만을 기억한다.
N명의 사람이 있고, 사람들의 키는 1부터 N까지 모두 다르다.

각 사람들이 기억하는 정보가 주어질 때, 줄을 어떻게 서야 하는지 출력하는 프로그램을 작성하시오.

입력
사람수 N 10이하 자연수
키가 1인 사람부터 차례대로 자기보다 키 큰 사람이 왼쪽에 몇 명이나 있는지 제시

키가
1 2 3 4 5 6 7 8 9 10 인 사람들이 자기 왼쪽에 자기보다 키 큰 사람이

새로 0을 n개 만들어서 판별.
작은 순서로 자기보다 키 큰 사람이 n명이라면 n의 위치에 배치 할 것임.
하지만 그 위치에 이미 자기보다 키 작은 사람이 배치되어 있다면 그 우측에 세우면 된다.
즉, 빈자리에 무조건 더 키 큰 사람이 들어 갈 수 있다는 믿음으로 한것임.
키 큰 사람을 나중에 배치하므로.
'''
n = int(input()) # 사람수
nl = list(map(int, input().split())) # 키 별 키큰사람 몇명인지
nhl = [0] * n # 재배열 할 키 리스트

for i in range(n):
    c = 0 # 0의 갯수를 카운트 할 것임.
    for j in range(n):
        if c != nl[i] and nhl[j] == 0:
            c += 1
        elif c == nl[i] and nhl[j] == 0:
            nhl[j] = i+1
            break
print(*nhl)



