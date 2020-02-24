def solution(answers):
    tmp = []
    cnt = 0
    cnt_lst = [0,0,0]
    p1 = [1,2,3,4,5] * ((len(answers) // 5)+1)  # enumerate 써서 idx%len(p1) 하면 초기화 늘려줄 필요 없음.
    p2 = [2,1,2,3,2,4,2,5] * ((len(answers) // 8)+1)
    p3 = [3,3,1,1,2,2,4,4,5,5] * ((len(answers) // 10)+1)
    for i in answers:
        if p1[cnt] == i:
            cnt_lst[0] += 1
        if p2[cnt] == i:
            cnt_lst[1] += 1
        if p3[cnt] == i:
            cnt_lst[2] += 1
        cnt+=1
    max_val = max(cnt_lst)
    if cnt_lst[0] == cnt_lst[1] == cnt_lst[2]:   # enumerate 써서 max값과 val이 같으면 그 때의 idx+1을 결과 lst에 append하면 됨.
        return [1,2,3]
    elif cnt_lst[0] == cnt_lst[1] and cnt_lst[0] > cnt_lst[2]:
        return [1,2]
    elif cnt_lst[1] == cnt_lst[2] and cnt_lst[1] > cnt_lst[0]:
        return [2,3]
    elif cnt_lst[0] == cnt_lst[2] and cnt_lst[2] > cnt_lst[1]:
        return [1,3]
    else:
        if cnt_lst[0] == max_val:
            return [1]
        elif cnt_lst[1] == max_val:
            return [2]
        else:
            return [3]


answers=[1,2,3,4,5]
print(solution(answers))