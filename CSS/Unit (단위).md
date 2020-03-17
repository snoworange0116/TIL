# Unit(단위)

- ### em 

  em은 현재의 font-size를 기본 값으로 하여 그 수치 만큼 곱한 값을 말한다.
  하지만 태그 안에 자식 태그가 이어질 경우 해당 수치가 계속 곱해져 font-size는 지속적으로 커지게 된다.
  
  
  
- ### rem (root em)

  최상위 태그(요소)에 지정한 것을 기준으로 그 수치 만큼 곱한 값이 된다. 보통 최상위 태그는 html태그가 된다.

  

- ### vw (vertical height & vertical width)

  원하는 타겟 요소의 너비값과 높이 값을 뷰포트의 너비값과 높이값에 맞게 사용할 수 있게 해준다.
  vh 값은 높이나 너비 값의 1/100의 값이 적용된다.
  따라서 450px의 높이 값을 가진다면 1vh는 4.5px이 된다.

  

- ### vmin & vmax

  vw와 vh가 뷰포트의 너비값과 높익밧에 상대적인 영향을 받는다면 vmin과 vmax는 너비값과 높이값에 따라 최대, 최소값을 지정할 수 있다.

  예를 들어 터치화면 양 변에 가득차는 정사각형을 만들 때는 아래와 같이 입력하면 된다.

  ![image-20200316002416640](C:\Users\wooyoung\AppData\Roaming\Typora\typora-user-images\image-20200316002416640.png)

  ```css
  .test {
      height: 100vmin;
      width: 100vmin;
  }
  ```

  만약 커버 이미지처럼 모든 네변이 스크린에 꽉 차야한다면 아래와 같이 입력하면 된다.

  ![image-20200316002435849](C:\Users\wooyoung\AppData\Roaming\Typora\typora-user-images\image-20200316002435849.png)

  ```css
  .test {
      height: 100vmax;
      width: 100vmax;
  }
  ```

  

