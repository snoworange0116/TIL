t = int(input())
h,w = map(int,input().split())
arr = [list(input()) for i in range(h)]
n= int(input())
input_str = input()
dir = -1 # 1은 상, 2는 하, 3은 좌, 4는 우
# .	평지(전차가 들어갈 수 있다.)
# *	벽돌로 만들어진 벽
# #	강철로 만들어진 벽
# -	물(전차는 들어갈 수 없다.)
# ^	위쪽을 바라보는 전차(아래는 평지이다.)
# v	아래쪽을 바라보는 전차(아래는 평지이다.)
# <	왼쪽을 바라보는 전차(아래는 평지이다.)
# >	오른쪽을 바라보는 전차(아래는 평지이다.)
for i in range(h):
    for j in range(w):
        if arr[i][j] == '<' or '^' or '>' or 'v':
            if arr[i][j] == '^':
                dir = 1
            elif arr[i][j] == 'v':
                dir = 2
            elif arr[i][j] == '<':
                dir = 3
            else:
                dir = 4
            pos_i,pos_j = i,j
while input_str:
    q = input_str.pop(0)
    if q == 'S':
        missile_i,missile_j = pos_i,pos_j
        if dir == 1:
            while missile_i < h and missile_j < w:
                missile_i += 1

