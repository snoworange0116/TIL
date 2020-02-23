from datetime import date

def solution(a, b):
    answer = ''
    dayofweek = ['MON','TUE','WED','THU','FRI','SAT','SUN']

    return dayofweek[date(2016,a,b).weekday()]