'''
가르침

남극 사는 김지민 선생. 많은 단어를 읽을 수 있도록 하려 한다.
얼음이 녹아서 곧 학교가 무너져서 k개의 글자만 가르칠 수 있다. 가르치면 k개의 글자로만 이루어진 단어만 읽을 수 있다. 어떤 k개의 글자를 가르쳐야 학생들이 읽을 수 있는 단어의 갯수가 최대가 되는지? anta 시작 tica 끝. 단어는 n개밖에 없음. 학생들이 읽을 수 있는 단어의 최댓값

입력
단어 갯수 n과 k 제시. n은 50이하 자연수 k는 26이하 음아정.
n개 줄 남극 언어의 단어 제시. 소문자로만. 길이 8이상 15이하. 중복x

출력
k개를 가르칠 때 학생들이 읽을 수 있는 단어 갯수의 최댓값 출력
'''
import sys
input = sys.stdin.readline

def cga(a:str):
    """
    문자 하나 받아서 방문 배열 인덱스로 반환
    """
    return ord(a)-97

def check():
    """
    cnt가 0이거나 k가 0인 경우, 몇 개의 단어를 셀 수 있나 카운트 하는 함수
    """
    global ans
    ret = 0
    for i in qst:
        for j in i:
            if not v[j]:
                break
        else:
            ret += 1
    if ret > ans:
        ans = ret

def dfs(sta, cnt):
    """
    dfs 실행, k만큼 실행 되었다면 검사 후 답 갱신
    """
    global ans
    if not cnt:
        check()
        return
    for i in range(sta+1, 26):
        if v[i]:
            continue
        v[i] = 1
        dfs(i, cnt-1)
        v[i] = 0


n, k = map(int, input().rstrip().split())
qst, mst = [], [0,2,8,13,17,19]
for i in range(n):
    a = set()
    s = input().rstrip()
    for j in s:
        a.add(cga(j))
    qst.append(a)
if k < 5:
    print(0)
    exit()
k -= 5
ans = 0
v = [1,0,1,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0]

if not k:
    check()
    print(ans)
    exit()

for i in range(26):
    if v[i]:
        continue
    v[i] = 1
    dfs(i, k-1)
    v[i] = 0
print(ans)





