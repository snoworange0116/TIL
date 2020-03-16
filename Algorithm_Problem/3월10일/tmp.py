import sys;
sys.stdin = open('6190.txt','r')

for tc in range(1, int(input()) + 1):
    n = int(input())
    arr = list(map(int,input().split()))
    # n개의 값들에서 2개 선택해서 곱하는 모든 경우
    for i in range(n-1):
        for j in range(i+1, n):
            
            num = arr[i] * arr[j]
            if ans >= num : continue
            t = num
            b = t%10
            t //= 10
            while t:
                a = t % 10
                if a > b : break
                t //= 10
                b = a
            else:
                ans = max(ans,num)
    print(ans)


            # 곱하기 결과가 단조 증가하는 수인지 판단
