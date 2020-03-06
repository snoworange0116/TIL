# 재귀
# def solution(v1,base):
#     T = '124'
#     q,r = divmod(v1,base) #몫,나머지
#     if q == 0:
#         if r != 0:
#             return T[r-1]
#         if r == 0:
#             return T[r]
#     else:
#         if r == 0:
#             if v1 > 3:
#                 return solution(q-1,base) + T[-1]
#             else:
#                 return T[-1]
#         else:
#             return solution(q,base) + T[r-1]
# print(solution(5,3))

# 재귀 안쓰고 풀기
def solution(n):
    answer = ''
    num_dict = {1: '1', 2: '2', 0:'4'}
    mok , nam = 1,1
    while mok != 0:
        mok,nam = divmod(n,3)
        if nam == 0:
            mok -=1
        n = mok
        answer = num_dict[nam] + answer
    return answer

print(solution(3))