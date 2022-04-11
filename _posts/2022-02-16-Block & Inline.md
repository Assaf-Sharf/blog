---
layout: single
title: "Block과 Inline"
categories: FrontEnd
tag: [total, css]
---

대부분의 HTML element(이하 요소)는 block 요소입니다.

예를 들어, `<header>`, `<footer>`, `<p>`, `<li>`, `<table>`, `<div>`, `<h1>` 등이 모두 block 요소에 해당하는 태그들입니다.

block 요소의 의미는, 이 요소 바로 **옆(좌우측)에 다른 요소를 붙여넣을 수 없다**는 뜻입니다.

block 요소와 성질이 반대인 inline 요소도 있습니다.

`<span>`, `<a>`, `<img>` 태그 등이 inline 요소입니다.

inline이라는 말 그대로 inline 요소는 요소끼리 서로 한 줄에, 바로 옆에 위치할 수 있다는 뜻입니다.

![2022-02-161.29.41](/Users/sonseongho/Library/Application Support/typora-user-images/2022-02-161.29.41.png)

첫번째 부터 네번째 까지는 `<p>` 태그와 같은 **block 요소**입니다.

노란색 영역이 해당 요소가 차지하는 영역입니다.

노란색 영역을 보면 알겠지만, 텍스트는 짧은데 그 이상으로 영역을 차지하고 있습니다.

block 요소들은 이런식으로 **항상 새 줄에서 시작하며 좌우로 최대한 늘어납니다.**

마지막 'span의 오른쪽 정렬'이라고 작성된 것은 **inline요소**인 `<span>` 태그를 사용했습니다.

그림과 같이 딱 텍스트만큼의 영역만 차지하고 있습니다.

아마 저 이후로 inline 성질을 가진 태그가 더 있었다면,

**새로운 줄에 시작되는게 아니라 바로 오른쪽에 그려졌을 것입니다.**

inline, block 성질에 의해 태그가 결정되지만,

아무 태그나 사용해도 **결국은 CSS를 통해 얼마든지 성질을 바꿀 수 있습니다.**

아무리 block 요소의 성질을 가진 `<p>` 태그도

css을 사용하여 inline 스타일로 바꾸면 `<span>` 과 똑같은 디자인이 됩니다.
