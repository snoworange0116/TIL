t = int(input())
for tc in range(1,t+1):
    n,m = map(int,input().split())
    arr = list(list(input()) for i in range(n))
    entire_val = n*m #전체 칠해야하는 구역 수
    min_val = 222222222
    for x in range(1,n-1):  #white구간 구역 나눠주기
        for y in range(1,n-x): #blue구간 구역 나눠주기
            color_lst = [0, 0, 0]
            for a in range(x): #white로 정해진 행에서 white 갯수 세기
                color_lst[0] += arr[a].count('W')
            for b in range(x,x+y): #blue로 정해진 행에서 blue 갯수 세기
                color_lst[1] += arr[b].count('B')
            for c in range(x+y,n): #red로 정해진 행에서 red 갯수 세기
                color_lst[2] += arr[c].count('R')
            if min_val > entire_val - sum(color_lst):  #각 케이스 최소값을 구학 위해, 전체 칠해야하는 구역 - w,b,r의 모든합해주기
                min_val = entire_val - sum(color_lst)
    print('#{} {}'.format(tc,min_val))

