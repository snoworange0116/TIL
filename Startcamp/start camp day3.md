### Start Camp Day 3

```python
from flask import Flask, request, render_template
from bs4 import BeautifulSoup
import requests, random

app = Flask(__name__)

token = '810062203:AAHf0qdjatVy3lnnDMcS1MHI6IrGK_rLVg4'
url = f'https://api.telegram.org/bot{token}/'
my_id = 965624545
ngrok_url = 'https://5cc7c659.ngrok.io'
papago_api_id = 'raHXR7GhaSciVKyjOmHc'
papago_api_secret = 'rZlX0D8gmT'


@app.route('/')
def hello():
    webhook = f'{url}setWebhook?url={ngrok_url}/telegram'
    return webhook

@app.route('/write')
def write():
    return render_template('write.html')


@app.route('/send')
def send():
    msg = request.args.get('msg')
    msg_url = f'{url}sendMessage?chat_id={my_id}&text={msg}' #fstring은 문자 안에 변수 삽입
    res = requests.get(msg_url) #
    print(res)
    return render_template('send.html', msg=msg)


@app.route('/telegram', methods = ['POST'])
def telegram():
   # print(request.get_json())
    res = request.get_json()
    user_id = res.get('message').get('from').get('id')
    user_msg = res.get('message').get('text')
   # print(user_id, user_msg)
    if user_msg == '안녕':
        return_msg = '반가워요'
    elif user_msg == '메뉴':
        menus = ['비빔밥', '청국장', '라면', '만두국']
        menu = int(random.uniform(0,4))
        return_msg = menus[menu]
    elif user_msg == '미세먼지':
        weather_url = 'https://search.naver.com/search.naver?sm=top_hty&fbm=0&ie=utf8&query=%EB%AF%B8%EC%84%B8%EB%A8%BC%EC%A7%80'
        weather_res = requests.get(weather_url).text
        soup = BeautifulSoup(weather_res,'html.parser')
        weather = soup.select_one('#main_pack > div.content_search.section._atmospheric_environment > div > div.contents03_sub > div > div:nth-child(3) > div.main_box > div.map_area > a.ct05.lv1._local > span.value > em')
        return_msg = f'광주의 미세먼지는 {weather.text}입니다.'
    elif user_msg[0:3] == '번역 ':
        before = user_msg[3:]

        headers = {
            'X-Naver-Client-Id': papago_api_id,
            'X-Naver-Client-Secret': papago_api_secret
        }
        papago_url = 'https://openapi.naver.com/v1/papago/n2mt'
        data = {
            'source':'ko',
            'target':'en',
            'text': before
            }
        
        res = requests.post(papago_url, headers=headers, data=data)
        before = res.json().get('message').get('result').get('translatedText')
        return_msg = before



    else:
        return_msg = '지원하지 않는 명령어입니다.'


    send_url = f'{url}sendMessage?chat_id={user_id}&text={return_msg}'
    requests.get(send_url)

    return '', 200

if __name__ == '__main__':
    app.run(debug=True)


```

