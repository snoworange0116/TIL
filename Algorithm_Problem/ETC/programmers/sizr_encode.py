def solution(s, n):
    answer = ''
    tmp = []
    for i in s:
        if i is not ' ':
            if 97 <= ord(i) <= 122 and ord(i) + n > ord('z'):  #s.isupper() 조건으로 대소문자 판별 가능
                tmp.append(chr(ord(i)+n-26))
            elif 65 <= ord(i) <= 90 and ord(i) + n > ord('Z'):
                tmp.append(chr(ord(i)+n-26))
            else:
                tmp.append(chr(ord(i)+n))
        else:
            tmp.append(' ')
    answer = ''.join(tmp)
    return answer