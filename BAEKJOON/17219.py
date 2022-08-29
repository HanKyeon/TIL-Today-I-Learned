'''
비밀번호 찾기

두 문자열에서 공통으로 존재하는 가장 긴 부분 문자열을 비밀번호
메모장에 적었다.
메모장에서 비밀번호를 찾는 프로그램.

입력
저장된 사이트 주소의 수 N 1이상 10만이하 찾으려는 사이트 주소 수 M 1이상 10만이하
N개 걸쳐 사이트 주소와 비번이 공백구분 제시. 사이트 주소는 소문자, 대문자, 하이픈-, 닷.으로 이루어져 있고, 중복되지 않는다. 비번은 알파벳 대문자로만. 길이는 최대 20자
이후 M개 줄에 걸쳐 비밀번호를 찾으려는 사이트 주소가 한 줄에 하나씩 입력.

출력
찾으려는 사이트 주소의 비번 각 줄에 하나씩 출력
'''
import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
di = {}
for _ in range(n):
    s, p = input().rstrip().split()
    di[s] = p
for _ in range(m):
    print(di[input().rstrip()])
