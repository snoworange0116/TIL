def recur(mon, price):
    global min_val
    if mon >= 12:
        if price < min_val:
            min_val = price
        return
    elif price > min_val:
        return
    if plan[mon] != 0:
        recur(mon+1, price + plan[mon] * price_lst[0])
        recur(mon+1, price + price_lst[1])
        recur(mon+3, price + price_lst[2])
    else:
        recur(mon+1, price)

t = int(input())
for tc in range(1,t+1):
    price_lst = list(map(int,input().split())) # 1일, 1달, 3달, 1년
    plan = list(map(int,input().split()))
    min_val = price_lst.pop()
    recur(0,0)
    print('#{} {}'.format(tc,min_val))