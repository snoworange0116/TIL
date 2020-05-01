# sw expert advanced 문제해결 1일차 - 이진수 5185

def Bprint(val):
    for i in range(4):
        if val&(8>>i):
            print("1",end='')
        else:
            print("0",end='')

t = int(input())
for tc in range(1, t+1):
    print('#{}'.format(tc), end=' ')
    N,S = input().split()
    for i in range(0, int(N)):
        t = int(S[i] , 16)
        Bprint(t)
        # if S[i] >= '0' and S[i] <= '9':
        #     Bprint(int(S[i]))
        # else:
        #     Bprint(ord(S[i]) - ord('A') + 10)
    print()


# N = int(N)
# res = ''
# for i in range(N):
#     if '0' <= num[i] <= '9':
#         print(bin(int(num[i])))
#     else:
#         print(int(num[i],2))
