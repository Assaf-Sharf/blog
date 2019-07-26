---
layout: post
title:  "Jekyll Minima Theme 커스터마이징 Part 1"
subtitle: "Home 레이아웃 변경하기"
author: "코마 (gbkim1988@gmail.com)"
date:   2019-07-26 00:00:00 +0900
categories: [ "jekyll", "minima", "css", "layout", "custom"]
excerpt_separator: <!--more-->
---

안녕하세요 **코마**입니다. 오늘은 지킬의 Minima 플러그인의 레이아웃을 변경하는 방법을 알아보겠습니다. 😺

<!--more-->

# 개요

지킬은 Github 등에서 블로그를 만들때 아주 유용한 도구입니다. 그러나 다른 사용자들이 만든 템플릿을 사용하다보면 어느새 식상한 것을 알 수 있는데요. 저 코마는 커스텀(custom) 꾸미기를 위한 초 간단 팁을 알려드리고자 합니다.

{% include advertisements.html %}

## Minima 란?

Minima 는 Jekyll 의 theme 중 하나입니다. 매우 심플한 디자인을 제공하고 있어 커스터 마이징하기에 매우 좋습니다. 설치를 원하시는 분들은 아래의 링크를 참고해 주세요.

- [깃헙 : Minima ](https://github.com/jekyll/minima)

## Minima Default Landing Page

Minima 를 사용하시기로 결정하였다면, 매우 좋은 선택입니다. 조금씩 자신의 스타일에 맞는 블로그로 꾸며가는 과정이 상당히 재밌습니다. 그렇다면 어떤 디자인인지 한번 확인해 볼까요?

![테마-1](/assets/img/2019/07/Minima_home.png)

조금 심심한 감이 있습니다. 좌우 사이드 패널에 무엇가를 더해주는 것도 나쁘지 않겠습니다. 그리고 전체적인 색감 조정이 필요할 것 같은데요. 이번 파트에서는 디폴트 랜딩 페이지를 수정하는 방법을 알아보고, 각 레이아웃을 변경해 보도록 하겠습니다.

## 레이아웃 커스터 마이징

우선, Jekyll 를 설치하고 Minima Theme 설정을 완료하였다고 가정하겠습니다. 여기서 핵심 포인트를 짚고 넘어가야겠네요.

**Minima 는 Default Theme 을 제공하기 때문에 설치 경로에 CSS, HTML 파일이 있습니다.**

따라서, CSS, HTML 을 커스터마이징 하기 위해서는 Minima 가 제시하는 규약을 따라야 합니다. 규약을 일일이 설명하는 것은 이해하기 어렵기 때문에 실습을 통해서 알아보겠습니다.

### 실습 스텝

1. Minima 설치 경로 확인
2. 로컬 경로에 동일한 디렉터리명 생성
3. Home.html 파일을 복사
4. HTML 코드 변경
5. 디자인 변경 확인

#### **1. Minima 설치 경로 확인**

`bundle` 명령어를 통해 minima 설치 경로를 확인할 수 있습니다.

```bash
> bundle show minima
/var/lib/gems/2.3.0/gems/minima-2.5.0
```

#### **2. 로컬 경로에 동일한 디렉터리명 생성**

`tree` 명령어를 통해서 현재 디렉터리 경로를 확인합니다. `_layouts` 폴더가 있네요. 만약에 없다면 `mkdir -p ./_layouts` 명령을 실행해 줍니다.
이제부터 Custom HTML 파일은 여기에 저장될 것입니다.

```bash
> tree -d -L 1
.
├── assets
├── _data
├── _drafts
├── _includes
├── _layouts
├── _posts
├── _sass
└── _site

8 directories
```

#### **3. home.html 파일 복사**

그렇다면, 프로젝트 폴더에 home.html 파일을 복사해 보겠습니다.

```bash
> cp /var/lib/gems/2.3.0/gems/minima-2.5.0/_layouts/home.html ./_layouts/
```

복사된 html 파일을 확인해 보니 _Posts 폴더에 생성한 블로그 글의 링크를 출력하는 코드가 보입니다.
여기에 우리가 원하는 코드를 넣어보겠습니다.

{% raw %}

```html
---
layout: default
---

<div class="home">
  {%- if page.title -%}
    <h1 class="page-heading">{{ page.title }}</h1>
  {%- endif -%}

  {{ content }}

  {%- if site.posts.size > 0 -%}
    <h2 class="post-list-heading">{{ page.list_title | default: "Posts" }}</h2>
    <ul class="post-list">
      {%- for post in site.posts -%}
      <li>
        {%- assign date_format = site.minima.date_format | default: "%b %-d, %Y" -%}
        <span class="post-meta">{{ post.date | date: date_format }}</span>
        <h3>
          <a class="post-link" href="{{ post.url | relative_url }}">
            {{ post.title | escape }}
          </a>
        </h3>
        {%- if site.show_excerpts -%}
          {{ post.excerpt }}
        {%- endif -%}
      </li>
      {%- endfor -%}
    </ul>

    <p class="rss-subscribe">subscribe <a href="{{ "/feed.xml" | relative_url }}">via RSS</a></p>
  {%- endif -%}

</div>
```

{% endraw %}

#### 4. HTML 코드 변경

저는 글 사이마다 광고를 삽입하고 싶습니다. 구글 광고를 한번 넣어보도록 할까요?

{% raw %}

```html
<!-- 구글 광고 코드 영역 (시작) -->

  {%- include advertisements.html html=content -%}
  
  <div class="cm-right-sidebar">
      <div class="cm-googlead">
          {%- include googlead-left-side.html html=content -%}
      </div>    
  </div>

  <div class="cm-left-sidebar">
      <div class="cm-googlead">
          {%- include googlead-left-side.html html=content -%}
      </div>    
  </div>
  
  <!-- 구글 광고 코드 영역 (종료) -->
```

{% endraw %}

#### 추가된 광고 화면

저의 홈페이지의 첫 화면으로 돌아가보시면 광고가 상단, 좌우에 배치된 것을 확인할 수 있습니다.

# 마무리

지금까지 초 간단 Jekyll Minima 꾸미기 였습니다. 구독해 주셔서 감사합니다.