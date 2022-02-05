---
layout: single
title: "[Elasticsearch] Elastic Stack 검색 문제와 해설"
date: "2022-02-05 12:25:27"
categories: Elasticsearch
tag: [Elasticsearch, Kibana]
toc: true
author_profile: true
# sidebar:
#   nav: "docs"
---

## 📌 실습에 앞서 기본적인 부분 복기

### ✅ Query Context 와 Filter Context 의 차이

- Query Context는 Full Text Search(**전문검색**)에 사용된다.
- Filter Context는 **YES/NO** 조건의 바이너리 구분에 사용된다.
- Query Context는 **스코어링 계산**을 수행한다.
- Filter Context는 **스코어링 계산**을 수행하지 않는다.
  - 캐싱 사용 가능.
  - 응답 속도가 빠르다.

### ✅ term

```sql
# term는 SQL의 equals 절과 유사하다
SELECT * FROM TB_USER WHERE 컬럼명 = "컬럼명"
```

<u class="custom-border-bottom">term은 색인이 나눠지면서 형태소로 나누어지는 저장되는 토큰등을 term이라고 한다.</u>  
또한 **term 쿼리**는 주어진 질의문과 저장된 텀과 **정확히 일치하는 문장**을 찾는다.

term으로 "name" : "cjung gglee" 라고 입력하게 되는경우에는 "cjung gglee"라는 하나의  
term을 찾기 때문에 결과가 나오지 않는다. 만약 2개 이상의 term을 같이 검색하고 싶을 때는 terms 쿼리를 이용해야 한다.

### ✅ match

```sql
# match는 SQL의 LIKE 절과 유사하다
SELECT 컬럼명 FROM 테이블 WHERE 컬럼명 LIKE '%A%'
```

match 쿼리도 term 쿼리와 마찬가지로 주어진 질의문을 색인된 term과 비교해서 일치하는 도큐먼트를 검색하는 질의다. <u class="custom-border-bottom">다만 term 쿼리와 다르게 match 쿼리에서는 주어진 질의문 또한 형태소 분석을 거친 뒤 분석된 질의문으로 검색을 수행한다.</u>

<u class="custom-border-bottom">예를 들면 The And로 검색하면 매치 쿼리는 이 질의문을 형태소 분석을 거쳐서 the and로 질의문을 바꾸고 이 값을 term과 비교해서 검색한다.</u>

그리고 기본적으로 match에 들어가는 데이터들은 or 검색으로 진행된다. 다시말하면 아래의 예에서는 Diamond 또는 Street 또는 Bartlett 라는 term으로 검색한다. 이것을 and로 바꾸고 싶은 경우에는 "operator" : "and" 옵션을 넣어주어야 한다.

```json
GET /bank/_search
{
  "query": {
    "match": {
      "address": "Diamond Street Bartlett"
    }
  }
}

// operator 적용
GET /bank/_search
{
  "query": {
    "match": {
      "address": {
        "query" : "Diamond Street Bartlett",
        "operator" : "and" // operator를 and로 수행하면 'Diamond Street Bartlett'를 찾는다
      }
    }
  }
}
```

## 📌 문제 풀이

### ✅ Info

```text
#=====================================================================================
# @since  : 2022-02-05(토)
# @author : ymkim
# @desc   : 퀴즈를 활용한 엘라스틱서치 익히기 2
#=====================================================================================
```

### ✅ 문제풀이 전 실습 데이터를 등록

```json
#=====================================================================================
# @문제풀이   : 문제풀이 전 실습 데이터를 등록한다.
# @주의사항   : _bulk API를 사용하는경우 한 줄로 입력을해야 한다.
#=====================================================================================
POST tourcompany/customerlist/_bulk
{"index": {"_id": "1"}}
{"name": "Alfred", "phone": "010-1234-5678", "holyday_dest": "Disneyland", "departure_date": "2017/01/20"}
{"index": {"_id": "2"}}
{"name": "Huey", "phone": "010-2222-4444", "holyday_dest": "Disneyland", "departure_date": "2017/01/20"}
{"index": {"_id": "3"}}
{"name": "Naomi", "phone": "010-3333-5555", "holyday_dest": "Hawaii", "departure_date": "2017/01/10"}
{"index": {"_id": "4"}}
{"name": "Andra", "phone": "010-6666-7777", "holyday_dest": "Bora Board", "departure_date": "2017/01/11"}
{"index": {"_id": "5"}}
{"name": "Paul", "phone": "010-9999-8888", "holyday_dest": "Hawaii", "departure_date": "2017/01/10"}
{"index": {"_id": "6"}}
{"name": "Clin", "phone": "010-5555-4444", "holyday_dest": "Venice", "departure_date": "2017/01/16"}

```

### ✅ 1번 tourcompany 인덱스에서 010-3333-5555를 검색하시오

```json
#=====================================================================================
# @문제번호   : 1번
# @문제풀이   : tourcompany 인덱스에서 010-3333-5555를 검색하시오.
#=====================================================================================

GET tourcompany/customerlist/_search?q="010-3333-5555"

GET tourcompany/customerlist/_search
{
  "query": {
    "match": {
      "phone": "010-3333-5555"
    }
  }
}

GET tourcompany/customerlist/_search
{
  "query": {
    "match": {
      "phone": {
        "query": "010-3333-5555",
        "operator": "and"
      }
    }
  }
}

GET tourcompany/customerlist/_search
{
  "query": {
    "match_phrase": {
      "phone": "010-3333-5555"
    }
  }
}
```

### ✅ 2번 휴일 여행을 디즈니랜드로 떠나는 사람들의 핸드폰 번호만 검색

```json
#=====================================================================================
# @문제번호   : 2번
# @문제풀이   : 휴일 여행을 디즈니랜드로 떠나는 사람들의 핸드폰 번호만 검색한다.
#=====================================================================================

GET tourcompany/_search?q="Disneyland"&_source=phone,holyday_dest
GET tourcompany/_search
{
  "query": {
    "match": {
      "holyday_dest": "Disneyland"
    }
  },
  "_source": "phone"
}
```

### ✅ 3번 departure date가 2017/01/10 과 2017/01/11 인 사람을 조회

```json
#=====================================================================================
# @문제번호   : 3번
# @문제풀이   : departure date가 2017/01/10 과 2017/01/11 인 사람을 조회하고 이 름 순으로 출력한다
#               (name과 departure date 필드만 출력)
#=====================================================================================

GET tourcompany/customerlist/_search?q="2017/01/10" or "2017/01/11"&sort=name.keyword
```

### ✅ 4번 BoraBora 여행은 공항테러 사태로 취소, BoraBora 여행자의 명단 삭제

```json
#=====================================================================================
# @문제번호   : 4번
# @문제풀이   : BoraBora 여행은 공항테러 사태로 취소됐습니다. BoraBora 여행자의 명단을 삭제해주십시오.
#=====================================================================================

GET tourcompany/customerlist/_search
GET tourcompany/customerlist/_search?q=Bora Bora
POST tourcompany/customerlist/_delete_by_query?q=Bora Bora
```

### ✅ 5번 Hawaii 단체 관람객의 요청으로 출발일 조정

```json
#=====================================================================================
# @문제번호   : 5번
# @문제풀이   : Hawaii 단체 관람객의 요청으로 출발일이 조정됐습니다. 2017/01/10에 출발하는 Hawaii의 출발일을
#               2017/01/17일로 수정해주십시오.
#=====================================================================================

GET tourcompany/customerlist/_search?q=Hawaii

# UPDATE Query
POST tourcompany/customerlist/_update_by_query
{
  "script": {"inline": "ctx._source.departure_date='2017/01/17'", "lang": "painless"},
  "query": {
    "bool": {
      "must": [
        {"match": {"departure_date": "2017/01/10"}},
        {"match": {"holyday_dest": "Hawaii"}}
      ]
    }
  }
}
```

### 참고 자료

- [엘라스틱서치 검색 문제와 해설](https://www.inflearn.com/course/ELK-%ED%86%B5%ED%95%A9%EB%A1%9C%EA%B7%B8%EC%8B%9C%EC%8A%A4%ED%85%9C-IT%EB%B3%B4%EC%95%88/lecture/27234?tab=curriculum&volume=1.00)
- [Elasticsearch 질의 DSL 정리](https://wedul.site/493)
