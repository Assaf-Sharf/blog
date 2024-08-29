---
layout: single
title: '[Network] Proxy Server 란?'
categories: Backend
tag: [server]
toc: true 
author_profile: false
sidebar:
    nav: "counts"
published: true

---

<a href ="https://www.youtube.com/watch?v=YxwYhenZ3BE">[10분 테코톡] 🐿 제이미의 Forward Proxy, Reverse Proxy, Load Balancer
</a> 를 보고 이해한 내용을 정리했습니다.

-------

## Proxy란?
프록시(Proxy)란 '대리', '대신'이라는 뜻을 가지며, 프로토콜에 있어서는 대리 응답 등에서 사용하는 개념이다.

### Proxy Server 

프록시 서버는 간단히 정리하면 대신 처리하는 서버라고 말할 수 있다. 

<div style="display: flex; justify-content: center;">
    <img src="{{site.url}}\images\2024-06-12-spring-boot-architecture_1\proxy.png" alt="Alt text" style="width: 100%; height: 100%; margin: 10px;">
</div>

<p style="text-align:center;"><b><span style="font-size:14px;">정방향 프록시</span></b></p>

클라이언트와 서버 사이에 존재하며, 중계기로서 대리로 통신을 수행하는 것을 Proxy라고 하며, 그 중계 기능을 하는 주체를 Proxy Server라고 한다.

캐시, 보안, 트래픽 분산 등 여러 장점을 가질 수 있다. 

###  Forward Proxy
일반적인 Proxy는 Forward Proxy를 말하며 프록시, 프록시 서버, 웹 프록시라고도 하는 정방향 프록시는 클라이언트 시스템 그룹 앞에 위치하는 서버이다. 

Forward Proxy는 일반적으로 다음과 같은 상황에 적용한다.

- 인터넷 속도 향상을 위해
- 외국에서 접속하는 것처럼 테스트하기 위해
- IP추적을 방지하기 위해

<div style="display: flex; justify-content: center;">
    <img src="{{site.url}}\images\2024-06-12-spring-boot-architecture_1\proxy_server.png" alt="Alt text" style="width: 100%; height: 100%; margin: 10px;">
</div>

<p style="text-align:center;"><b><span style="font-size:14px;">Forward Proxy</span></b></p>

#### 캐싱
**클라이언트가 요청한 내용을 캐싱**

정방향 프록시가 설정되면 A가 대신 B에 요청을 보내고 B가 요청을 C로 전달한다. 그런 다음 C가 B에게 응답을 보내고 B가 응답을 A에게 다시 전달한다.

>- 클라이언트1이 "오늘 날씨"를 물어보면 포워드 프록시가 질문을 받아 웹 서버에 요청한다. 
>- 그 후 "오늘 날씨" 에 대한 결과 값을 저장한 후 클라이언트1에게 전달해준다. 
>- 클라이언트2가 "오늘 날씨"를 물어보면 포워드 프록시가 웹 서버에 요청하지 않고 이전에 저장한 값을 클라이언트2에게 전잘해준다.

1) 전송 시간 절약

2) 불필요한 외부 전송이 이루어지지 않는다.

3) 외부 요청이 감소한다
    - 네트워크 병목 현상이 방지된다. 

#### 익명성   
**클라이언트가 보낸 요청을 감춘다.**

프록시 서버는 Server가 응답 받은 요청을 누가 보냈는지 알지 못하게 한다. Server가 받은 요청의 IP는 Proxy Server 의 IP이기 때문이다 .

### Reverse Proxy
역방향 프록시는 하나 이상의 웹 서버 앞에 위치하여 클라이언트의 요청을 가로채는 서버이다. 이것은 프록시가 클라이언트 앞에 위치하는 정방향 프록시와 다르다. 

<div style="display: flex; justify-content: center;">
    <img src="{{site.url}}\images\2024-06-12-spring-boot-architecture_1\reverse_proxy.png" alt="Alt text" style="width: 100%; height: 100%; margin: 10px;">
</div>

<p style="text-align:center;"><b><span style="font-size:14px;">Reverse Proxy</span></b></p>

일반적으로 D의 모든 요청은 F로 직접 이동하고, F는 D에게로 직접 응답을 보낸다. 역방향 프록시를 사용하면 D의 모든 요청이 E로 직접 이동하고, E는 요청을 F에게로 보내며 F로부터 응답을 받고 E는 그런 다음 적절한 응답을 D에게 전달한다.

#### 캐싱
**클라이언트가 요청한 내용을 캐싱 (Forward Proxy와 동일)**

#### 보안
**서버 정보를 클라이언트로 부터 숨긴다.**

리버스 프록시는 클라이언트의 요청을 받으면 자기가 알고있는 서버들에게 클라이언트의 요청을 보낸다. 클라이언트는 실제 Server 정보를 알지 못한다. 

클라이언트는 Reverse Proxy를 실제 서버라고 생각하여 요청하고 실제 서버의 IP가 노출되지 않는다. 


정방향 프록시와 역방향 프록시의 차이룰 요약하면 정방향 프록시는 클라이언트 앞에 위치하며 원본 서버가 해당 특정 클라이언트와 직접 통신하지 못하도록 하는 것이고 반면에 역방향 프록시는 원본 서버 앞에 위치하며 어떤 클라이언트도 원본 서버와 직접 통신하지 못 하도록 한다.

## Load Balancing
해야할 작업을 나누어 서버의 부하를 분산 시키는 것을 말한다. 

<div style="display: flex; justify-content: center;">
    <img src="{{site.url}}\images\2024-06-12-spring-boot-architecture_1\load_balancing.gif" alt="Alt text" style="width: 100%; height: 100%; margin: 10px;">
</div>

<p style="text-align:center;"><b><span style="font-size:14px;">Load Balancing</span></b></p>

### Load Balancer란?
Load Balancer는 한마디로 서버들에게 유저를 분배해준다. 여러 대의 서버가 분산 처리할 수 있도록 요청을 나누어주는 서비스이다. 다양한 알고리즘을 이용하여 분배한다. 

> 웹사이트로 유입되는 트래픽이 가파르게 증가하면 두 대의 서버로 트래픽을 감당할 수 없는 시점이 오는데, 로드밸런서가 있으면 웹 서버 계층에 새로운 서버를 추가하는 간단한 방법으로 자동적으로 트래픽을 분산시켜 우아하게 대처할 수 있다. 


#### L4, L7
- L4 : Transport Layer(IP & Port) Level에서 Load Balancing
    - 사이트 접근 시 서버 A, 서버 B로 분산 처리 

- L7 : Application Layser(User Request) Level 에서 Load Balancing 
    - 사이트 접근 시 /a, /b  등 특정 주소 기준으로 분산 처리 


<br>
<br>

----
Reference
- Proxy
    - <a href = 'https://www.youtube.com/watch?v=YxwYhenZ3BE'>제이미의 Forward Proxy, Reverse Proxy, Load Balancer by 10분 테코톡</a>
    - <a href = 'https://www.cloudflare.com/ko-kr/learning/cdn/glossary/reverse-proxy/'>역방향 프록시란 | 프록시 서버 설명 by cloudflare</a>

- Image
    - <a href = 'https://www.haproxy.com/blog/what-is-load-balancing'>what-is-load-balancing</a>



