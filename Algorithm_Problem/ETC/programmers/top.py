# def solution(heights):
#     answer = []
#     origin_heights = heights[:]
#     heights_copy = heights[::-1]  # 탑 순서 뒤집은거
#     top_len = len(heights) # 탑 길이
#     recept_top = heights[:] # 수신전용 탑
#     recept_top.pop()
#     send_cnt = 0
#     while heights:
#         flag = 0
#         flag2 = 0
#         send = heights.pop()
#         recept_top = origin_heights[:]
#         send_cnt += 1
#         # print('-', send_cnt)
#         print('-------------------')
#         while recept_top:
#             if flag == 0:
#                 for i in range(send_cnt):
#                     print('before', recept_top)
#                     recept_top.pop()
#                 print('after', recept_top)
#                 recept = recept_top.pop()
#                 # print(send,recept)
#                 if recept > send:
#                     idx = heights_copy.index(recept) # 탑 순서 뒤집은거에서 인덱스 찾는중
#                     answer.append(top_len-idx)
#                     flag = 1
#                     break
#             flag2 = 1
#         if flag == 0:
#             answer.append(0)
#     return answer[::-1]
# heights = [1,5,3,6,7,6,5]
# print(solution(heights))

def solution(heights):
    len_top = len(heights)
    answer = [0] * len_top
    while heights:
        send = heights.pop()
        for idx in range(len(heights)-1,-1,-1):
            if heights[idx] > send:
                answer[len(heights)] = idx+1
                break
    return answer
