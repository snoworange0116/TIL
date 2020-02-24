def solution(strings, n):
    strings = sorted(strings)
    strings.sort(key= lambda element : element[n])
    return strings

# def solution(strings, n):
#     for i in range(len(strings)):
#         strings[i] = strings[i][n] + strings[i]
#     strings.sort()
#     for i in range(len(strings)):
#         strings[i] = strings[i][1:len(strings[i])]
#     return strings