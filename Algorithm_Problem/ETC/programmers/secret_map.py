def solution(n, arr1, arr2):
    answer = []
    aft_arr1, aft_arr2, sum_arr = [],[],[]
    for i in range(n):
        if len(bin(arr1[i])) == n+2:
            aft_arr1.append(bin(arr1[i])[2:])
        else:
            aft_arr1.append('0' * (n+2-len(bin(arr1[i]))) + bin(arr1[i])[2:])
        if len(bin(arr2[i])) == n+2:
            aft_arr2.append(bin(arr2[i])[2:])
        else:
            aft_arr2.append('0' * (n+2-len(bin(arr2[i]))) + bin(arr2[i])[2:])
        # print(aft_arr1)
        # print(aft_arr2)

    for i in range(n):
        sum_tmp = ''
        for j in range(n):
            if (aft_arr1[i])[j] == '1' or (aft_arr2[i])[j] == '1':
                sum_tmp += '#'
            else:
                sum_tmp += ' '
        answer.append(sum_tmp)
    return answer

n=6
arr1 = [46, 33, 33 ,22, 31, 50]
arr2 = [27 ,56, 19, 14, 14, 10]
print(solution(n,arr1,arr2))

# 모범답안
# def solution(n, arr1, arr2):
#     answer = []
#     for i,j in zip(arr1,arr2):
#         a12 = str(bin(i|j)[2:])
#         a12=a12.rjust(n,'0')
#         a12=a12.replace('1','#')
#         a12=a12.replace('0',' ')
#         answer.append(a12)
#     return answer