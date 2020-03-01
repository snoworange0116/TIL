import math

def calc(num,idx):
    global min_val
    global max_val
    if idx == n:
        if min_val > num:
            min_val = num
        if max_val < num:
            max_val = num
    else:
        if operator_lst[0] > 0:
            operator_lst[0] -= 1
            calc(num + num_lst[idx], idx+1)
            operator_lst[0] += 1
        if operator_lst[1] > 0:
            operator_lst[1] -= 1
            calc(num - num_lst[idx], idx+1)
            operator_lst[1] += 1
        if operator_lst[2] > 0:
            operator_lst[2] -= 1
            calc(num * num_lst[idx], idx+1)
            operator_lst[2] += 1
        if operator_lst[3] > 0:
            operator_lst[3] -= 1
            calc(math.trunc(num / num_lst[idx]), idx+1)
            operator_lst[3] += 1
    return

t = int(input())
for tc in range(1,t+1):
    n = int(input())
    operator_lst = list(map(int, input().split())) # '+ - * /' 순서
    num_lst = list(map(int, input().split())) # 계산당할 숫자들
    max_val = -999999999
    min_val = 999999999
    calc(num_lst[0],1)
    res = abs(min_val - max_val)
    print("#{} {}".format(tc,res))
