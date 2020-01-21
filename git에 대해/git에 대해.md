# git 에 대해

git을 통해 차이가 무엇인지, 수정 이유를 log로 남길 수 있다.

add : 커밋할 목록에 추가
commit : 커밋 만들기
push 혀재까지의 역사가 기록되어 있는 곳에 새로 생성한 커밋들 반영하기.

git add helloworld.py
git commit -m
git config -global



### git bash를 통해 git hub 업로드 하는 방법

1. 해당 폴더에서 마우스 우클릭 -> git bash열기 클릭
2. gitbash에서 git init
3. git add .(현재 폴더 내의 모든 폴더, 파일 임시저장)
4. git commit -m "homeworkshop01 완료" (-m은 메세지라는 옵션,)
5. git remote add origin https: ~~ 제일 긴 주소
6. git push origin master : 최신화



### git bash

ls : 파일 목록 보는거
ls -a : 숨겨진 파일 목록까지 보는 것
git init : ~ 하위 파일들을 관리하겠다는 뜻
git status :  현재 git의 상태 보는 것
git commit -m : git에 보내면서 남길 메세지
git remote add github `올릴 주소` : github이라는 변수(?)에 올릴 주소를 할당 하겠다.
git diff : git이 트래킹하고 있는 파일들을 찾아 차이점을 비교해 줌
git pull github master : 
git ignore : git에게 특정 파일들은 빼놓길 원할 때
git readme : 만들 프로젝트에 대한 설명서를 쓰는 습관을 들여야 함.