'''
잃어버린 괄호

양수, +, -, 괄호로 식을 만들었다.
괄호를 뺐는데 괄호를 넣어서 최소로 만들어야 한다.

입력
숫자+-로 이루어진 문자열 길이 최대 50
55-50+40 이렇게.

출력
괄호 쳐서 얻을 수 있는 최솟값.
'''
'''
-를 찾아서 그 다음 -까지 괄호치기.
'''
s = input() # 입력
ns, yz = '0123456789', '+-' # 숫자, 연산자
nl, mflg = '', False # 임시숫자, 마이너스 조우 여부 
ans, imsi = 0, 0 # 답 / 임시 저장 값
for i in s:
    if i in ns: # 훑으면서 숫자면 nl에 더해준다.
        nl += i
        continue
    # 연산자 만나면 아래 행동 중 하나를 한다.
    elif i == '+': # 덧셈이면
        imsi += int(nl) # 임시값에 더해주고
        nl = '' # 초기화
    elif i == '-' and mflg == False: # 마이너스를 처음 만나면
        imsi += int(nl) # 임시값에 더해주고
        nl = '' # 초기화
        ans += imsi # 정답에 임시값 더해주고
        imsi = 0 # 임시값 초기화
        mflg = True # 마이너스 만났음
    elif i == '-' and mflg == True: # 마이너스 만난 상태에서 -가 뜨면
        imsi += int(nl) # 임시값에 더해주고
        ans -= imsi # 정답에서 빼준다.
        imsi = 0 # 임시값 초기화
        nl = '' # 초기화
else: # 마지막 숫자 처리
    imsi += int(nl)
if mflg: # 마이너스 만난 상태로 임시값에 더해준거면
    ans -= imsi # 빼주고
else: # 아니면
    ans += imsi # 더해줘라

print(ans) # 출력


