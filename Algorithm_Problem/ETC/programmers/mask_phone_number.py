def solution(phone_number):
    answer = ''
    for i in range(len(phone_number) - 4):
        answer += '*'
    answer += phone_number[len(phone_number) - 4:]  # phone_number[-4:] 도 가능

    return answer