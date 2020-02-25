def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)):    # answer = [[c + d for c, d in zip(a, b)] for a, b in zip(A,B)]
        answer.append([])
        for j in range(len(arr1[i])):
            answer[i].append(arr1[i][j] + arr2[i][j])
    return answer