while True:
    try: n = int(input())
    except: break
    num, cnt = 1, 1
    cnt = 1
    while True:
        if num%n: num*=10; num+=1;cnt+=1
        else: break
    print(cnt)