def recur(val1,val2,res):
    if val1 == val2:
        if val1 % 2 == 1:
            res.append(str(val1))
        print(' '.join(res))
        return
    else:
        if val1 % 2 == 1:
            res.append(str(val1))
        return recur(val1 + 1 , val2,res)
a,b = map(int,input().split())
res = []
recur(a,b,res)