# start camp day1

### 프로그래밍 3형식

1. 저장

2. 조건

3. 반복

   

##### 저장

> 저장은 save?? 어떤걸 저장했지?
>
> - 글자, 숫자, True, False
> - 리스트
> - 딕셔너리



##### 조건

조건문은 **if, else, elif** 로 구성된다.



##### 반복

- `while`문을 이용한 반복문

``` python
n = 0
while n < 3:
	print('80미만입니다.')
    n = n+1
```

- for문을 이용한 반복문

``` python
dust = [10, 20, 30]
for i in dust:
	print(dust)
```



### Markdown 활용법

- ' # ' 개수가 많아짐에 따라 head 크기가 작아짐

- ' > ' : 좌측 눈에 띄는 블록 생성 
- ' ``` ' : 코드 기입할 블록 생성
- ' - ' : unordered list 생성
- ' 숫자 ' : ordered list 생성
- ' ` 둘로 감싸기 '  : 단어 강조



### 챗봇 만들기

- 점심 메뉴 출력

``` python
import random

menu = ['짜장면', '삼겹살']

menu_dict = {'짜장면':'062-123-1234', '삼겹살':'062-789-6543'}

b = random.choice(menu)
print("오늘의 메뉴는 {0} : {1}".format(b,menu_dict[b]))

```

- if문 활용해 미세먼지 농도 출력

```python
  print('{} 기준 미세먼지 농도는 {}입니다.'.format(time, dust))
  
  # dust 변수에 들어 있는 값을 기준으로 상태 정보를 출력해보세요.
  if dust > 150:
    print('매우나쁨')
  elif dust <= 150 and dust >80:
    print('나쁨')
  elif 30 <= dust < 80:
    print('보통')
  else:
    print('좋음')
```

- 로또 번호 6개 출력

``` python
  import random
  num = []
  num = random.sample(range(1,46,),6)
  print(num)
```

