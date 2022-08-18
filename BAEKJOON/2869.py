'''
달팽이는 올라가고 싶다

V미터 나무막대
낮에 A미터 올라감
밤에 B미터 미끄러짐
막대기를 다 오르려면 며칠이 걸리는가?

입력
A B V 한줄 1~10억

'''

a, b, v = map(int, input().split())
gh = v-a
dn = a-b
if gh % dn == 0:
    print(gh//dn + 1)
else:
    print(gh//dn + 2)
