import sys
sys.setrecursionlimit(1000000)
def recur(st,ed,sum):
    if st == ed:
        sum += st
        print(sum)
        return
    else:
        sum += st
        return recur(st+1,ed,sum)
n=12345
sum = 0
recur(1,n,sum)