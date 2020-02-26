t = int(input())
for tc in range(1,t+1):
    n = int(input())
    nosun = []
    visit_lst = []
    for i in range(n):
        nosun.append(list(map(int,input().split())))
    p = int(input())
    c = [int(input()) for pc in range(p)]
    for cc in c:
        val = 0
        for a,b in nosun:
            if a <= cc <= b:
                val += 1
        visit_lst.append(val)
    print('#{} {}'.format(tc,' '.join(map(str,visit_lst))))

