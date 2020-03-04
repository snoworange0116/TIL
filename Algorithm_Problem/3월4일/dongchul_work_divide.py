# import itertools
# t = int(input())
# for tc in range(1,t+1):
#     n = int(input())
#     arr = [list(map(int, input().split())) for i in range(n)]
#     num = 0
#     max_val = -9999
#     lst = list(itertools.permutations(range(n)))
#     # print(lst)
#     for i,v in enumerate(lst):
#         tmp = 1
#         for j in range(n):
#             tmp *= arr[j][v[j]]/100
#             if tmp < max_val:
#                 break
#         if tmp > max_val:
#             max_val = tmp
#     print('#{} {}'.format(tc, round(max_val*100,6)))

def dfs(val , cnt):
    global max_val
    if cnt == n:
        if val > max_val:
            max_val = val
        return
    elif val < max_val:
        return
    else:
        for i in range(n):
            if visit[i] == 0 and val*arr[i][cnt] > max_val:
                visit[i] = 1
                dfs(val * arr[i][cnt]/100 , cnt + 1)
                visit[i] = 0
t = int(input())
for tc in range(1,t+1):
    n = int(input())
    arr = [list(map(int, input().split())) for i in range(n)]
    visit = [0] * n
    max_val = -9999
    dfs(1,0)
    print('#{0} {1:.6f}'.format(tc,max_val*100))