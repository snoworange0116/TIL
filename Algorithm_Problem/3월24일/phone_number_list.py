# 프로그래머스 level 2
def solution(phone_book):
    phone_book.sort(key=lambda x:len(str(x)))
    while phone_book:
        st = phone_book.pop(0)
        length = len(st)
        for i in phone_book:
            if i[0:0+length] == st:
                return False
    return True

#phone_book = ['119','97674223','1195524421']

# 이 문제에서는 if 조건으로 일치하는 전화번호들을 찾았을 때, break로
# 바깥의 loop만 빠져나와서 시간오류가 떴었음.
# 함수를 확실하게 종료하고자 할때는 return으로 빠져나오는게 시간복잡도를 간단하게 해결할 수 있음
# 평소 함수로 코드를 짜야하는 중요성이 된다고 생각한다.
