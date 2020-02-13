t = int(input())

for i in range(t):
    P,A,B = map(int,input().split())
    base = 1
    P_a , P_b = P, P
    c_a,c_b = int((base + P) / 2) , int((base + P) / 2)
    cnt_a, cnt_b = 0, 0

    while (c_a != A):
        if c_a > A:
            P_a = c_a
            c_a = int((base + P_a)/2)
            cnt_a += 1
        elif c_a < A:
            base = c_a
            c_a = int((base+P_a)/2)
            cnt_a += 1

    base = 1
    while(c_b != B):
        if c_b > B:
            P_b = c_b
            c_b = int((base + P_b)/2)
            cnt_b += 1
        elif c_b < B:
            base = c_b
            c_b = int((base+P_b)/2)
            cnt_b += 1
    if cnt_a < cnt_b:
        result = 'A'
    elif cnt_a > cnt_b:
        result = 'B'
    else:
        result = 0
    print('#{} {}'.format(i+1,result))

