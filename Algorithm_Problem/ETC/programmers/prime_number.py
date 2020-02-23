def solution(n):
    cnt = 0
    arr = [x for x in range(n+1)]
    arr[1] = 0
    for i in range(2,n):
        if arr[i] == 0:
            pass
        else:
            for j in range(i*2,n+1,i):
                arr[j] = 0
    for i in arr:
        if i != 0:
            cnt += 1
    return cnt

# n = 10
# n = 5