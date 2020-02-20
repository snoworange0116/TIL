from itertools import permutations

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    arr = [list(map(int,input().split())) for i in range(n)]
    lst = permutations(list(range(n)),n)  # permutation list로 안감싸 줘도 됨.
    # range(n) 객체를 사용하면 list에 0부터 n-1까지의 값을 append 할 필요가 없음

    min = 100000000 # min,max와 같은 비교 값의 초기화는 루프 밖에다가 해주어야 함.
    for i in lst:
        sum = 0
        for j in range(n):
            sum += arr[j][i[j]]
            if sum >= min: # sum이 큰 경우 말고 같은 경우도 루프를 진행시킬 필요가 없으므로
                break
        if min > sum:
            min = sum

    print('#{} {}'.format(tc,min))