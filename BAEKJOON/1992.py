'''
쿼드트리

흰 점을 나타내는 0과 검은 점을 나타내는 1로 이루어진 2차원 배열.
주어진 영상이 모두 0으로만 되어있으면 압축 결과는 0이 되고
모두 1로만 되어 있으면 압축 결과는 1이 된다.
0과 1이 섞여있으면 전체를 한 번에 나타내지 못하고 좌상단 우상단 좌하단 우하단 4개로 나누어 압축하게 되며, 압축한 결과를 차례대로 괄호 안에 묶어서 표현.

사분면 나눠서
0 1  0 0  1 1
1 0  0 0  1 1
이면 각각 0110 0 1로 나타내진다.

입력
영상 크기 N. 2제곱수, 1이상 64이하.
그래프 제시.

출력
영상 압축한 결과 출력
'''
import sys
input = sys.stdin.readline

def 네모네모(h, w, ln):
    ret = '' # 리턴값
    b = g[h][w] # b는 초기값
    if ln == 2: # 종료조건
        for i in range(h, h+ln): # 범위 순회
            for j in range(w, w+ln):
                ret += g[i][j] # 일단 모든 값 저장
        fla = True # 같은 걸로 구성되어 있는가?
        for i in ret:
            if i != b: # 같은 걸로 구성 안되어있으면
                fla = False # 거짓
                break
        if fla: # 같은걸로 구성되어 있으면
            ret = b # 한글자로갱신
        else: # 아니면
            ret = '('+ret+')' # 괄호 붙여서 갱신
        return ret

    # 길이가 2가 아니면 받은 것 전부에 대해 확인
    fla = True
    for i in range(h, h+ln):
        for j in range(w, w+ln):
            if g[i][j] != b:
                fla = False
                break
        if not fla:
            break
    
    if fla: # 같으면 한글자 리턴
        return b
    else: # 다르면 합쳐서 리턴
        nln = ln//2
        return '('+네모네모(h, w, nln)+네모네모(h, w+nln, nln)+네모네모(h+nln, w, nln) + 네모네모(h+nln, w+nln, nln)+')'

n = int(input())
g = [list(input().rstrip()) for _ in range(n)]
print(네모네모(0, 0, n))
