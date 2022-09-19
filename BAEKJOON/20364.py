'''
부동산 다툼

이진 트리 모양의 땅 꽉꽉 마을. 땅 번호는 완전 이진트리 처럼.
오리끼리 부동산 다툼이 일어남. 해결책 제시.

오리 한 줄. 1번 땅 대기.
오리들이 서있는 순서대로 원하는 땅 가지기.
가는 길에 땅이 막혀있으면 땅을 못지나가서 땅을 못가진다.

이렇게 했을 때, 각 오리 별로 원하는 빵을 가질 수 있는지, 없다면 처음 마주치는 점유된 땅의 번호를 구하자.

입력
땅 갯수n, 오리 수 q 제시. n은 2이상 2**20 이하. q는 1이상 20만이하.

출력
Q개의 줄에 원하는 땅에 갈 수 있다면 0을, 갈 수 없다면 처음 마주치는 점유된 땅의 번호 출력.
'''
import sys
input = sys.stdin.readline

n, q = map(int, input().rstrip().split())
quest = [int(input()) for _ in range(q)]
v = [0] * (n+1) # 방문
for i in quest:
    val = i
    ans = 0
    while val:
        if v[val]: # 처음 만나는걸 확인해야 하므로 계속 갱신해줘야 한다.
            ans = val
        val //= 2
    if not ans:
        v[i] = 1
    print(ans)





















