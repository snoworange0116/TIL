import itertools
n = int(input())
arr = [list(map(int,input().split())) for i in range(n)]
min_val = 10000
tmp = list(range(n))
st_subset = list(map(list,itertools.combinations(tmp, n//2))) #st팀의 후보들
# print(st_subset)
for i in st_subset: #st팀의 후보들로 루프 돌리기
    st_subset_2 = []
    link_subset_2 = []
    link_subset = []
    for j in range(n):  #st팀이 아닌 녀석들을 link팀의 리스트로 만들어주기
        if j not in i:
            link_subset.append(j)
    sum_st, sum_link = 0,0
    st_subset_2 = list(map(list,itertools.combinations(i,2)))  #st팀 행,열 값 조합 만들기
    for a,b in st_subset_2:
        sum_st += (arr[a][b] + arr[b][a])  # 만든 조합으로 st팀 능력치 합 구하기
    link_subset_2 = list(map(list,itertools.combinations(link_subset,2))) #link팀 행,열 값 조합 만들기
    for c,d in link_subset_2:
        sum_link += (arr[c][d] + arr[d][c]) # 만든 조합으로 link팀 능력치 합 구하기
    if abs(sum_st - sum_link) < min_val:   # st랑 link 능력치 차이 빼서 min보다 작으면 할당최신화 해주기
        min_val = abs(sum_st - sum_link)
print(min_val)