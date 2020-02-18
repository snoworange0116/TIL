# 모듈



### 모듈 사용법

```python
import module
import pakage1.module1, pakage2.module2
from module import var
from module import function
from module import Class
from module import *
from pakage.module import var, function, Class
```



### csv 모듈

```python
import csv

lunch = {
    '그릴스' : '매운돈까스',
    '소반' : '낙곱새'
}
csvfile = open('lunch.csv','w', encoding = 'utf-8', newline='')  #utf-8 인코딩은 한글 사용하기 위해서
csv_writer = csv.writer(csvfile)

for key,val in lunch.items():
    csv_writer.writerow([key, val])
csvfile.close()

```

```python
# csv.close()를 안해줘도 되는 코드
with open('lunch.csv','w', encoding = 'utf-8', newline='') as csvfile:  #utf-8 인코딩은 한글 사용하기 위해서
    csv_writer = csv.writer(csvfile)

    for key,val in lunch.items():
        csv_writer.writerow([key, val])
 
```

##### Daum 검색어 가져오기

```python
import requests
from bs4 import BeautifulSoup
import csv

url = 'https://www.daum.net'

res = requests.get(url).text
html = BeautifulSoup(res, 'html.parser') # res값을 예쁘게 바꿔주기 위해
rankings = html.select('#mArticle > div.cmain_tmp > div.section_media > div.hot_issue.issue_mini > div.hotissue_layer > ol > li > div > div:nth-child(1) > span.txt_issue > a')

rank_dict = {}
for idx,rank in enumerate(rankings, 1):
    # print(idx,rank.text)
    rank_dict[f'{idx}위'] = rank.text

# print(rank_dict)
with open('ranking.csv', 'w', encoding = 'utf-8', newline = '') as csvfile:
    csv_writer = csv.writer(csvfile)  # csv.writer를 사용함으로써 csv파일자료의 수정이 용이하도록 만듬.
    for key,val in rank_dict.items():
        csv_writer.writerow([key,val])
    # csv_writer.writerow(['1위','싸피'])
```

##### Daum 검색어 가져오기(dict활용)

```python
import requests
from bs4 import BeautifulSoup
import csv

url = 'https://www.daum.net'

res = requests.get(url).text
html = BeautifulSoup(res, 'html.parser') # res값을 예쁘게 바꿔주기 위해
rankings = html.select('#mArticle > div.cmain_tmp > div.section_media > div.hot_issue.issue_mini > div.hotissue_layer > ol > li > div > div:nth-child(1) > span.txt_issue > a')


rank_list = []
for idx, rank in enumerate(rankings, 1):
    # print(idx,rank.text)
    rank_dict = {
        'rank':f'{idx}위',
        'value': rank.text,
    }
    rank_list.append(rank_dict)
    # rank_dict[f'{idx}위'] = rank.text

with open('ranking.csv', 'w', encoding = 'utf-8', newline = '') as csvfile:
    fieldnames = ['rank','value']
    # csv_writer = csv.writer(csvfile) 
    csv_writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
    csv_writer.writeheader()
    for rank in rank_list:
        csv_writer.writerow(rank)

```

##### csv 읽어오기

```python
import csv

with open('ranking.csv', 'r', encoding='utf-8',newline='') as csvfile:
    csv_reader = csv.DictReader(csvfile)
    for row in csv_reader:
        print(row['rank'],row['value'])
```

##### Melon Top50 제목,가수 가져오기

```python
import requests
from bs4 import BeautifulSoup
import csv

url = 'https://www.melon.com/chart/index.htm'
user_agent = 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'
h = {
    'User-Agent' : user_agent
}
res = requests.get(url,headers=h).text
html = BeautifulSoup(res,'html.parser')
#==================================================
data = html.select('#lst50 > td:nth-child(6) > div > div > div.ellipsis.rank01 > span > a')
singers = html.select('#lst50 > td:nth-child(6) > div > div > div.ellipsis.rank02 > span')

rank_list = []
for i in range(50):
    rank_dict = {
        'rank' : f'{i+1}위',
        'value' : data[i].text,
        'singer' : singers[i].text,
    }
    rank_list.append(rank_dict)

with open('melon_ranking.csv','w',encoding='utf-8',newline='') as csvfile:
    fieldnames = ['rank','value','singer']
    csv_writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
    csv_writer.writeheader()
    for rank in rank_list:
        csv_writer.writerow(rank)
```

