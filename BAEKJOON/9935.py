'''
문자열 폭발

문자열에 폭발 문자열을 심었다. 폭발하면 그 문자열은 사라지며 남은 문자열은 합쳐진다.
1. 문자열이 폭발 문자열을 포함하고 있는 경우, 모든 폭발 문자열이 폭발하게 된다. 남은 문자열을 순서대로 이어붙여 새로운 문자열을 만든다.
2. 새로 생긴 문자열에 폭발 문자열이 포함되어 있을 수도 잇다.
3. 폭발은 폭발 문자열이 없을 때까지 지속된다.
어떤 문자열이 남는지? 남는 문자열이 없을 경우 FRULA 출력. 폭발 문자열은 같은 문자를 2개 이상 포함하지 않는다.

입력
문자열 제시 1이상 100만이하
폭발 문자열 제시. 1이상 36이하
알파벳 소문자와 대문자, 숫자0~9로만 이루어져 있다.

출력
폭발 이후 남은 문자열 출력
'''
import sys
input = sys.stdin.readline

s = input().rstrip() # 문자열
b = list(input().rstrip()) # 비교군
sta = [] # 스택
for i in s:
    sta.append(i) # 스택에 넣고
    if b[-1] == sta[-1]: # 끝자리가 같으면
        if sta[-len(b):] == b: # 비교군 길이만큼 같은지 확인
            sta[-len(b):] = [] # 같으면 없앰
if sta: # 있으면 출력
    for i in sta:
        print(i, end='')
else: # 없으면 프룰라
    print("FRULA")










