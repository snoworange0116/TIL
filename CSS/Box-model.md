# Box Model

### -  block 요소

블록 박스는 다른 블록 박스에 포함디거나, 포함할 수 있고, 너비와 높이 설정이 가능하다.
내부에 아무 콘텐츠가 없을 경우 높이는 0이 된다.

```css
// 블록 요소 종류들
section, article, aside, header, footer, nav, main, hx, div, o, dl, dt, dd, ul, ol, p, audio, video, blockquote, canvas, fieldset, figure, figcaption, footer, form, table, tfoot, hr, noscript, pre 등등
```

- 가운데 정렬 하는 법: `margin : 0 auto;`



### - Inline 요소

인라인 박스는 다른 인라인 박스에 포함되거나 포함할 수 있지만, 블록 요소는 포함할 수 없다.
너비와 높이 설정이 가능하지 않고 내부 콘텐츠의 크기에 따라 높이와 너비가 정해진다.
형제끼리는 동생(뒤에 선언된 태그)이 형(먼저 선언된 태그)의 오른쪽 옆에 붙는 구조를 가진다.

```css
// 인라인 요소 종류들
a, abbr, acronym, b, bdo, big, br, button, cite, code, dfn, em, i, img, input, kbd, label, map, object, q, samp, small, script, select, span, strong, sub, sup, textarea, tt, var
```



### - inline-block 요소

기본적인 속성은 inline과 유사하지만 블록 처럼 너비와 높이 값 설정이 가능한 것이 차이점이다.
즉 수평 배치를 유지한 상황에서 특정 태그에 width 속성 부여가 가능하게 된다. 

