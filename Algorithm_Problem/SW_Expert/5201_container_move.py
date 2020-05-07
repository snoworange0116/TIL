t = int(input())
for tc in range(1,t+1):
    n,m = map(int,input().split()) # 컨테이너수 n, 트럭 수 m
    weight = list(map(int,input().split())) # 화물 용량
    truck = list(map(int,input().split())) # 트럭 적재 용량
    sum = 0
    weight.sort(reverse=True)
    truck.sort(reverse=True)
    # print(weight)
    # print(truck)
    for i in range(m):
        if truck[0] >= weight[0]:
            truck.pop(0)
            sum += weight.pop(0)
        else:
            weight.pop(0)
        if len(weight) == 0:
            break
    print('#{} {}'.format(tc,sum))