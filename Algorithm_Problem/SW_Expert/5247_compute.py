# 5247 sw expert 그래프, 연산
from collections import deque

def find(n,cnt):
    q = deque()
    q.append([n,0])
    while q:
        num, cnt = q.popleft()
        if num > 1000000 or num < 0:
            continue
        if num == m:
            return cnt
        if visited[num] == 0:
            cnt += 1
            q.append([num+1,cnt])
            q.append([num-1,cnt])
            q.append([num*2,cnt])
            q.append([num-10,cnt])
            visited[num] = 1

t = int(input())
for tc in range(1,t+1):
    n,m = map(int,input().split())
    visited =[0] * 1000001
    result = find(n,0)
    print('#{} {}'.format(tc,result))