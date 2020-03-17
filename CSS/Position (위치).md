# Position (위치)



### - static

모든 태그들의 기본 상태는 static 이다. 왼쪽에서 오른쪽, 위쪽에서 아래 방향으로 쌓여간다.



### - relative

`position : relative` 속성을 줌으로써 `top`, `right`, `bottom`, `left` 속성을 사용해 위치 조절이 가능해진다. relative는 각 방향을 기준으로 태그 안쪽방향으로 이동하게 된다. 
`z-index` 라는 속성을 통해 태그들이 겹칠 때 누가 더 위로 올라가는지 결정할 수 있다.



### - absolute 

`relative`가 static 상태를 기준으로 픽셀 이동을 한 반면, `absolute`는 static 속성을 가지고 있지 않은 부모를 기준으로 움직인다. 만약 부모 중 relative, absoulte, fixed인 태그가 없다면 가장 위의 태그가 기준이 된다.
absolute가 되면 div 태그도 더 이상 width가 100%가 아니게 된다. 



### - fixed

웹 사이트 상단의 navigation이나 하단의 footer에 주료 사용되어 지는데, 스크롤로 사이트 화면 이동을 하여도 해당 `fixed` position을 가진 태그들은 고정되어 움직이지 않게 된다.



### - sticky

relative처럼 동작하면서 relative 요소가 없는 경우에는 fixed처럼 동작하는 두가지 효과를 모두 가질 수 있음.
평소에는 static 상태와 같이 일반적인 흐름에 따르지만 스크롤 위치가 임계점에 이르면 fixed처럼 고정되어 진다.
sticky를 적용하기 위해서는 첫 째로 top, bottom, left, right 등의 값을 필요로 하고, 둘 째로 부모 요소들 중 어느 하나라도 overflow: hidden 값인 경우 동작하지 않으므로 이에 유의해야 한다.