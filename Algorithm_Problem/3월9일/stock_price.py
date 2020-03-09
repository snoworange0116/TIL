from collections import deque

def solution(prices):
    l = len(prices)
    answer =[0] * l
    prices = deque(prices)
    idx = 0
    while prices:
        cnt = 0
        st = prices.popleft()
        for i in prices:
            cnt+=1
            if st > i:
                break
        answer[idx] = cnt
        idx += 1
    return answer

prices = [1,2,3,2,3,1]
prices = deque(prices)
print(solution(prices))