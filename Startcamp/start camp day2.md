# Start Camp Day 2

- 범위가 있으면 반복문은 for 문을 씀

- for 단수 in 복수(iter형)

- 웹에서의 커뮤니케이션 방식 : 요청(request)과 응답(response) / HTML , XML , JSON



##### import webbrowser

- webbrowser.open_new('주소')

- webbrowser.open_new_tab('주소')



##### VS Code 설정

- Ctrl + '`' : VS Code에서 터미널

* Ctrl + 'c' : VS Code에서 interpreter 탈출



### 크롤링으로 정보 스크랩하기 (KOSPI 지수 뽑기)

- 터미널 창에서 `pip install requests` 을 통해 api를 다운로드

- python 파일명.py로 터미널 창 안에서 실행

  

* import requests

  1. requests/get(주소).select : 
  
  2. requests.get(주소) .text : 
  
3. requests.get(주소).select : 문서 안에 있는 특정 내용을 모두 뽑아주는 기능
  
  4. requests.get(주소).select_one : 문서 안에 있는 특정 내용을 하나만 뽑아주는 기능
  
     


```python
import requests  
from bs4 import BeautifulSoup #bs4 안의 beautifulsoup 가져오기

sise_url = 'https://finance.naver.com/sise/' # url 변수화

res = requests.get(sise_url).text #url 주소에서 문서만 가져와 준다
soup = BeautifulSoup(res, 'html.parser') #Html 문서를 예쁘게 가다듬어 준다 (터미널 상에서)
#KOSPI_now
kospi = soup.select_one('#KOSPI_now') #ID가 KOSPI_now를 가져옴 (#은 아이디)
print(kospi.text) #kospi에서 숫자만 가져오기
```



### HTML

HTML 기초

! + tab : 기본 html 구조 만들기 (doc, html, head , body)

``` html
<!DOCTYPE html>
<html> 
    <head>
        <!-- head는 웹 브라우저 탭 타이틀 -->
        <title>여기는 html 실습을 위한 페이지입니다.</title>
    </head>

    <body>
        <h1>HTML!!!!</h1>
        <h2>좀더 작은 글씨</h2>
        <h6>제일 작음</h6>
        <!-- body는 웹사이트 보여지는 내용물 -->
        <ul> 
            <li>안녕하세요</li>
            <li>반갑습니다</li>
        </ul>
        <!-- ul은 순서 없는 리스트
             ol은 순서 있는 리스트
             li는 그 안의 리스트 목록들 -->
        <ol>
            <li>1번</li>
            <li>2번</li>
        </ol>

    <a href = "https://www.naver.com">네이버</a>
        <!-- 텍스트에 링크를 연결해주는 것 -->
    </body>
</html>
```



### Flask

from flask import Flask, escape, request (코드에 입력)

flask run FLASK_APP = hellp.py (터미널 창에 입력)

cd : change directory 

cd .. :  (상위 폴더로)

cd flask_intro : flask_intro 폴더로 이동)

flask run : flask 서버 실행

CTRL + C 서버 실행 종료



##### 라우터를 변수화



- 점심메뉴 랜덤 출력

```python
@app.route('/lunch')
def lunch():
    menu = ['라면', '닭갈비', '낙지볶음밥', '오므라이스', '조기매운탕']
    pick = random.choice(menu)
    return render_template('lunch.html', pick = pick)
```



``` html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    <h1>오늘의 추천메뉴</h1>
    <h2>{{pick}}</h2>
</body>
</html>
```



- HTML , FLASK의 if문 사용

```html
<body>
	{% if html_name == 'admin' %}
		<h1>관리자님 안녕하세요</h1>
	{% else %}
		<h1>안녕하세요 {{html_name}}님</h1>
	{% endif %}
</body>
```

  

* HTML Full

```python
from flask import Flask, escape, request, render_template
import random

app = Flask(__name__)

@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return f'안녕하세요, {escape(name)}!'

@app.route('/html_tag')
def html_tag():
    return """
    <h1>헤딩1번입니다.</h1>'
    <ul>
        <li>안녕하세요</li>
        <li>반갑습니다.</li>
    </ul>
    """

@app.route('/first')
def first():
    return render_template('hello.html')


@app.route('/name/<string:name>')
def name(name):
    return render_template('name.html',html_name=name)

@app.route("/welcome")
def welcome():
    return '반갑습니다'


@app.route('/cube/<int:num>')
def cube(num):
    cube_num = num ** 3
    return render_template('cube.html', html_num = num, html_cube_num = cube_num)

@app.route('/lunch')
def lunch():
    menu = ['라면', '닭갈비', '낙지볶음밥', '오므라이스', '조기매운탕']
    menu_dict = {
        '라면': 'http://static.hubzum.zumst.com/2017/11/14/09/de6fe845120a4e06b5d4b50d9e8f5cd2.jpg',
        '닭갈비': 'http://recipe1.ezmember.co.kr/cache/recipe/2016/01/22/4a6aa74a48653f1cb1416f9c42230fd91.jpg',
        '낙지볶음밥': 'https://allchanmall.com/web/product/medium/201812/0c19c4997645486310cb51af8bb25c1f.jpg',
        '오므라이스': 'http://mblogthumb2.phinf.naver.net/20160610_9/sallysto_1465485225315gh1xq_JPEG/DSC_0023.JPG?type=w800',
        '조기매운탕': 'http://recipe1.ezmember.co.kr/cache/recipe/2015/06/27/23c4d74ad5599bf80d6d35e2425b60ba.jpg',
    }
    pick = random.choice(menu)
    pick_img = menu_dict[pick]
    return render_template('lunch.html', pick = pick, pick_img = pick_img)

@app.route('/movies')
def movies():
    movies = ['해치지 않아','닥터두리틀','나쁜녀석들']
    return render_template('movies.html', movies = movies)

@app.route('/ping')
def ping():
    return render_template('ping.html')


@app.route('/pong')
def pong():
    location = request.args.get("location")
    return render_template('pong.html', location = location)

@app.route('/past')
def past():
    
    return render_template('past.html',)

@app.route('/result')
def result():
    name = request.args.get("name")
    faces = ['원빈', '디카프리오', '조세호']
    face_dict = {
        '원빈' : 'http://dh.aks.ac.kr/Edu/wiki/images/thumb/a/ae/Wonbin1.jpg/400px-Wonbin1.jpg',
        '디카프리오': 'http://ojsfile.ohmynews.com/STD_IMG_FILE/2013/0522/IE001581410_STD.jpg',
        '조세호': 'https://dimg.donga.com/wps/NEWS/IMAGE/2014/08/29/66080255.3.jpg',
                }
    pick = random.choice(faces)
    pick_img = face_dict[pick]
    return render_template('result.html', faces = faces,pick_img = pick_img ,name= name)

if __name__ == '__main__':
    app.run(debug=True)
  
```

  

* Past.html 파일

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    <h1>당신의 전생을 보여드립니다.</h1>
    <form action = "/result">
        이름: <input name = "name">
        <input type = "submit">
    </form>
</body>
</html>
```

* Result.html 파일

```html
  <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    <h1>당신의 전생</h1>
    <img src = "{{pick_img}}">
</body>
</html>

```

  

