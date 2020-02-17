def shelve():
    min = 100000
    for i in range(1<<n):
        for j in range(n+1):
            if i & (1<<j):
                temp.append(lst[j])
        length = sum(temp)
        if length >= b and length < min:
            min = length
        temp.clear()
    return min

t = int(input())
for tc in range(1,t+1):
    n,b = map(int,input().split())
    lst = list(map(int,input().split()))
    n = len(lst)
    temp = []
    result = shelve()
    print('#{} {}'.format(tc,result-b))
