def recur(res,n,val):
    if n == 1:
        print(val)
        return
    else:
        return recur(res,n-1,val*n)
n = int(input())
recur(1,n,1)