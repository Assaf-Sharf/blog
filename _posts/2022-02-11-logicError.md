---
layout: post
title: "ini와 date_list 로직 충돌"
---
![image](https://user-images.githubusercontent.com/86642180/153457507-cf59a6a6-f48f-4369-bdac-eae99550ec3f.png)
문제의 두 테이블  

<br>

현재 initiative 테이블에 데이터를 추가하려면  
😜클라이언트 : ob_code, ini_content, startdate, enddate, period, weekorder, ✌date✌, monthdate  
저만큼의 정보를 클라이언트에서 받는다  
💻컨트롤러 : 클라이언트에서 받은 값 + 전체기간 등을 계산  
service layer에 전달 - mapper에 전달되어 initiative 테이블에 insert됨  

<br>
🔥문제점  
클라이언트에서 받은 date(요일 목록)를 먼저 저장 뒤, initiative insert를 진행하려해도  
initiative_code가 date_list 테이블에서도 중요한거라 NULL 넣는것도 안됨  
만약 NULL 허용해주면 나중에 난잡해질 확률 10000%  

<br>

결론 : 저 두 테이블의 선행관계가 정립도 안되고 데이터 저장하는데 문제가 있다..  
이도저도 안되는 상황!  

<br>

