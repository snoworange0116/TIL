t = int(input())
for tc in range(1,t+1):
    n , m = map(int,input().split())
    n_lst = list(map(int,input().split())) # 종목들
    m_lst = list(map(int,input().split())) # 평가위원들
    n_lst2 = []
    for _ in n_lst:
        n_lst2.append([_,0])
    max_val = -99
    result = 0
    for i in m_lst:
        for j in n_lst2:
            if j[0] <= i:
                j[1] += 1
                break
    for idx,val in enumerate(n_lst2):
        if val[1] >= max_val:
            max_val = val[1]
            result = idx
    print('#{} {}'.format(tc,result+1))