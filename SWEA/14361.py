'''
숫자가 같은 배수

입력
테케
하나의 줄

숫자 N을 재배열해서 N보다 더 큰 N의 배수 숫자 가능하면 possible
불가능한 최대 수이면 impossible
'''

for testcase in range(1, int(input())+1) :
    strn = input()
    intn, listn = int(strn), list(map(int, strn))
    nl = [0]*10
    for i in listn:
        nl[i] += 1
    print(f"#{testcase}", end=' ')
    ci, c = 2, 0
    while intn*ci <= 10**sum(nl): # n의 배수가 n의 자릿수 이내라면
        newnum = intn*ci # 그 숫자를
        nnl = [0]*10
        for i in list(map(int, str(newnum))): # 리스트로 만들어서 훑으면서
            nnl[i] += 1 # nnl에 숫자들을 정리해준다.
        if nnl == nl: # 그게 만약 nl과 같다면
            c+=1 # 카운트 올린다
        if c>0: # 카운트 되었다면
            break # 반복문 끝낸다.
        ci += 1 # ci가 증가했을 때도 확인한다.
    if c != 0: # 카운트가 증가했다면 가능
        print('possible')
    if c == 0: # 카운트 증가 안했으면 불가능
        print('impossible')
    








'''
    nn, f = n, 0
    print(f"#{testcase}", end=' ')
    while nn > 0:
        if f > nn % 10:
            print("possible")
            break
        f = nn % 10
        nn = nn // 10
    if nn == 0:
        print("impossible")
'''