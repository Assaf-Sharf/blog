---
layout: post
title: "파이썬 기초"
---

# random library
```
import random

print(random.choice(["된장찌개","피자","제육볶음"]))
```
리스트 중 하나 랜덤 선택  

<br>

# python for문 문법
```
for x in range(반복횟수):
    반복할코드
```
자바에서
```
for(i=0; i<횟수; i++){
  반복코드
}
```
와 같다  
혼자 문제푸는데 자바처럼 써서 안되니까 오류난줄..  

<br>

# python while문 문법
```
while 조건:
    반복코드
```
조건에 True 쓰면 무한루프  
끝낼때는 break  

<br>

# list
`list = ["A", "B", ...]`

<br>

```
list.append("값")
del list[순서]
```

<br>

- list 출력
```
for x in range(len(list)):
    print(list[x])
```
보다  

```
for x in range list:
    print(x)
```
가능  

<br>

# dictionary
`dict = {"key" : "value"}`  
자바의 맵?인듯  
```
information = {"고향":"수원", "취미":"영화관람", "좋아하는 음식":"국수"}
print(information.get("취미"))
```
하면 취미(key)의 value 출력  
`dictionary.get("key")`이며 value 넣으면 None이 출력됨  

<br>

```
dict["add"] = "more"
del dict["삭제할 key값"]
len(dict)
```
add가 편하다  
자바는 map.put("","")인데  

<br>

- dict 
```
for x, y in dict.items():
  print(x + " : " + y)
```

<br>

# 집합(set)
중복 X, 요소 순서 X  

- 선언
`set = set([리스트])`  

<br>

- list 👉 set
```
foods = ["된장찌개", "피자", "제육볶음"]
foods_set1 = set(foods)
foods_set2 = set(["된장찌개", "피자", "제육볶음"])
```

<br>

- 합집합  
```
menu1 = set(["된장찌개", "피자", "제육볶음"])
menu2 = set(["된장찌개", "떡국", "김밥"])
menu3 = menu1 | menu2
print(menu3)
```
- 차집합  
```
menu1 = set(["된장찌개", "피자", "제육볶음"])
menu2 = set(["된장찌개", "떡국", "김밥"])
menu3 = menu1 - menu2
print(menu3)
```
- 교집합  
```
menu1 = set(["된장찌개", "피자", "제육볶음"])
menu2 = set(["된장찌개", "떡국", "김밥"])
menu3 = menu1 & menu2
print(menu3)
```

<br>

# 오늘은 뭐 드실?
저메추, 점메추 프로그램  

<br>

# 기타
똑같은거 5번 이상 반복하면 잘못된 코딩  
python : 변수에 타입설정X  
데이터 타입은????  
