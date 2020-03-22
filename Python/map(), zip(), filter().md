# map(),  zip(), filter()

### map(function, iterable)

```python
numbers = [1, 2, 3]
result = [str(number) for number in numbers] #숫자를 문자로 각각 바꾼 리스트를 만들고 join
print("".join(result)) # 123
print(result) #['1', '2', '3']
```



### zip( *iterables )

복수의 iterable 객체를 모아준다.
결과는 튜플의 모음으로 구성된 zip object를 반환한다.

```python
girls = ['jane', 'iu', 'mary']
boys = ['justin', 'david', 'kim']
list(zip(girls, boys)) # [('jane','justin'),('iu','david'),('mary','kim')]
```



### filter(function, iterable)

iterable에서 function의 반환된 결과가 True인 것들만 구성하여 반환한다.
filter object를 반환한다.

```python
def odd(num):
    if num % 2:
        return True
    else:
        return False
    return num % 2
numbers = [1,2,3,4,5,6,7,8,9]
result = list(filter(odd,numbers))
print(result) # [1, 3, 5, 7, 9]
```

