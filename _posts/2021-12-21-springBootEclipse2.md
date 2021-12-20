---
layout: post
title: "이클립스 스프링부트 select 완성"
---

### 📌 현재 시점에서 스펙  
Spring Boot 2.6.1  
Java 8  
Eclipse 2021-03  
MySQL - AWS 연결  
<br>
Thymeleaf 써서 프론트까지 잘 보이게 하는건 X  
오로지 백엔드쪽만 일단 마무리  
<br>
## 0. 구조 및 개념 정리
계속 추가할 예정  


## 1. 프로젝트 생성
![image](https://user-images.githubusercontent.com/86642180/146802774-07aad3ca-d2b1-4b66-bfa3-5ccdb95d1b7a.png)  
![image](https://user-images.githubusercontent.com/86642180/146804155-8bd00742-1aa2-41e9-8b72-89372076b3a8.png)  
![image](https://user-images.githubusercontent.com/86642180/146803250-3a928db3-baf3-44b8-ba78-063c3db981b4.png)  

그래들 프로젝트로 만들어서 의존성 주입도 직접 할까 했으나  
인텔리제이도 쓸지 모른다는 생각 + 어차피 할꺼 인텔리제이가 대세라니까 공부하자는 협의로  
<b>스프링 부트와 AWS로 혼자 구현하는 웹 서비스</b>를 보며 같이 공부할 것 같다.  
<br>
정리하다보니 Jar와 War 파일 차이점 좀 더 공부해야겠다.  
누가 물어보면 차이 잘 설명도 못하겠네..  
<br>
이미 필요한 의존성은 다 넣었으니 build.gradle에 추가할 필요는 없다.  
<br>
## 2. Domain 생성
