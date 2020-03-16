import collections

t = int(input())
n = int(input())
room = []
for i in range(n):
    a,b= map(int,input().split())
    room.append([a,b])
room = collections.deque(room)
cnt = 0
while room:
    a = room.popleft()