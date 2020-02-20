def find(n,s):
    global minV   # n은 순열의 인덱스, s는 생성된 부분까지의 합
    if n == N:
        if minV > s: # 순열이 완성된 경우
            minV = s # 기존의 최소값 보다 작으면
        return
    elif minV <= s: # 순열이 완성되지 않았지만 합이 최소값보다 큰 경우
        return
    else:
        for i in range(N): # 순열의 n번 인덱스에 들어갈 숫자 선택
            if u[i] == 0:
                u[i] = 1
                find(n+1, s+m[n][i])
                u[i] = 0
        return