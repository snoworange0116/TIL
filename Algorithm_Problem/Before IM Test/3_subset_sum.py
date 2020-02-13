
t = int(input())
for t_i in range(t):
    #A = [1,2,3,4,5,6,7,8,9,10,11,12]
    A = [1,2,3,4,5,6,7,8,9,10,11,12]
    n, k = map(int,input().split()) # n은
    count = 0
    A_n = len(A)

    for i in range(1<<A_n):
        temp = []
        for j in range(A_n+1):
            if i & (1<<j):
                temp.append(A[j])
        if len(temp) == n and sum(temp) == k:
            count += 1

    print("#{} {}".format(t_i+1, count))
