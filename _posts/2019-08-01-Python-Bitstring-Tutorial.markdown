---
layout: post
title:  "파이썬 바이너리 변환 (Raw Data 다루기)"
subtitle: "Bitstring 을 이용한 간편한 바이너리 다루기"
author: "코마"
date:   2019-08-01 00:00:00 +0900
categories: [ "python", "bitstring", "binary" ]
excerpt_separator: <!--more-->
---

안녕하세요 코마입니다. 오늘은 파이썬을 이용해서 Binary 값을 다루는 방법을 소개해 드리도록 하겠습니다.😺

<!--more-->

# 개요

파이썬은 타입에 민감하지 않은 언어입니다. 그러다보니 종종 Hex, Bin 을 다루어야 하는 경우 딱히 방법이 떠오르지 않을 때가 많습니다. 저 코마는 이러한 여러분의 어려움을 해소하기 위해 Bitstring 이라는 모듈을 소개해 드리도록 하겠습니다.

- bitstring 설치하기 

```bash
pip install bitstring
```

- hexdump 설치하기 

```bash
pip install hexdump
```

{% include advertisements.html %}

## int 를 이용한 데이터 변환

python 에도 타입이 있습니다. int, float, bytes 등이 그것입니다. 그 중에 int 는 n 진법으로 표현된 문자열 데이터를 읽어와 정수로 표현하는 좋은 기능이 있습니다. 

아래는 우리에게 친숙한 이진법, 16진법, 십진법의 데이터를 정수로 변환하는 과정입니다.

```python
# 이진 데이터를 변환 
[11] : int('00100001',base=2)
33
```

```python
# 16진수 데이터를 변환
[12] : int('0xff',base=16)
255
```

```python
# 10진법 데이터를 변환
[13] : int('255', base=10)
255
```

## 문자열 변환

우리는 여러가지 진법으로 표현된 데이터를 정수로 변경하였습니다. 그리고 이제는 문자열로 변환하거나 문자열에서 정수로 변환하고 싶습니다. 이때 사용하는 타입이 chr, ord 입니다.

```python
[14] : chr(int('00100001',base=2))
'!'
[15] : ord('!') # 문자만(char) 정수로 바꾸어줍니다.
33
```

## Bit Stream 다루기

지금까지 길이가 짧은 데이터를 다루었습니다. 그러나 만약, jpg, mp4 등의 파일 타입에 대해서 Bit 조작을 해야 한다면 어떻게 해야 할까요? 저는 `bitstring` 과 `hexdump` 를 이용하는 것을 추천합니다.

```bash
Raw Data <-------------> Bitstring <---------------> Raw Data
```

### bitstring 클래스

bitstring 은 아래의 클래스들을 제공해줍니다. 그리고 그 역할들은 아래와 같습니다.

| No. | class | descr |
|:----:|:----:|:----:|
| 1 | bitstring.Bits (object) | 가장 기본 클래스로 `immutable` 한 속성을 가집니다. 즉, 한번 생성 이후 값을 변경할 수 없습니다. |
| 2 | bitstring.BitArray (Bits) | Bits 에 대해 변경(mutation) 속성을 추가한 것입니다. 즉, 변경 가능합니다. |
| 3 | bitstring.ConstBitStream (Bits) | bits 를 스트림처럼 다루도록 메서드와 프로퍼티를 제공합니다. position 에 기반한 읽기(read) 와 parse 를 제공합니다. |
| 4 | bitstring.BitStream (BitArray, ConstBitStream) | 가장 다재 다능한 클래스입니다. bistream 의 기능과 mutating 기능이 합쳐져 있습니다. |

{% include advertisements.html %}

이 장에서는 BitArray 와 ConstBitStream 을 다루어 보도록 하겠습니다.

### BitArray

BitArray 는 Hex String (0x0001, 0xff 등), Binary String (0b0101010, ... 등), int (12, 13, ... 등), Raw Byte 를 입력받아 처리할 수 있습니다. 한번 예시를 볼까요?

```python
from bitstring import BitArray, ConstBitStream
# Hex String
[15] : BitArray(hex='000001b3').hex
'000001b3'
# Binary String
[16] : BitArray(bin='0011 00').bin
'001100'
# uint (정수)
[17] : BitArray(uint=45, length=12).bin
'000000101101'
# Bytes
[18] : BitArray(bytes=b'\x01\x02\x03\x04\x05', length=32, offset=8).bytes
b'\x02\x03\x04\x05'
[18] : BitArray(bytes=b'\x01\x02\x03\x04\x05', length=32, offset=4)
BitArray('0x10203040')
```

{% include advertisements.html %}

위에서 BitArray 의 offset 속성은 좌측에서 offset 비트 수만큼 건너뜀을 의미합니다. 즉 처음을 0 이라고 한다면 4 비트 건너뛰어서 데이터를 읽어냅니다. 그리고 length 는 데이터에서 얼마만큼 읽어올 것인가를 지정합니다. 32 라고 기입한 경우 4 Bytes 를 읽습니다. 

`BitArray(bytes=b'\x01\x02\x03\x04\x05', length=32, offset=4)` 의 경우 `Bits 에서 4 bits 만큼 건너뛴 위치에서 32 bits 만큼을 읽어온다.` 라고 해석할 수 있습니다.

### ConstBitStream

ConstBitStream 은 대표적으로 아래의 메서드와 프로퍼티를 제공합니다. 

- pos : Bit Stream 에서 포인터의 위치를 가리킵니다.
- peek : 현재의 포인터 위치에서 포인터를 변경하지 않고 지정한 bit 수 만큼 데이터를 읽어옵니다.
- read : 현재의 포인터 위치에서 포인터를 변경하면서 지정한 bit 수 만큼의 데이터를 읽어옵니다.

{% include advertisements.html %}

#### read 메서드

read 메서드는 아래의 Return Format 을 지정할 수 있습니다. 즉, 특정 길이만큼 데이터를 읽어온다면 이를 출력하는 타입을 지정할 수 있음을 의미합니다. 지원하는 포맷은 아래와 같습니다.

- `int:n`
  - n bits as a signed integer.
- `uint:n`
  - n bits as an unsigned integer.
- `hex:n`
  - n bits as a hexadecimal string.
- `bin:n`
  - n bits as a binary string.
- `bits:n`
  - n bits as a new bitstring.
- `bytes:n`
  - n bytes as bytes object.

- 아래는 샘플 예시 입니다. 

```python
# read('uint:n') 
[1] : s = ConstBitStream('0x1234')
[2] : s.read('uint:4')
1
[3] : s.read('uint:4')
2
[4] : s.read('uint:4')
3
[5] : s.read('uint:4')
4
```

```python
# read('bin:n') 
[1] : s = ConstBitStream('0x1234')
[2] : s.read('bin:4')
'0001'
[3] : s.read('bin:4')
'0010'
[4] : s.read('bin:4')
'0011'
[5] : s.read('bin:4')
'0100'
```

### 응용하기 MP4 파일 처리하기

ConstBitStream 을 이용하면 Raw 데이터를 쉽게 처리할 수 있을 것이라는 확신이 들기 시작합니다. 그렇다면 MP4  동영상 데이터를 다운로드 받은 뒤에 이를 Bit Stream 처럼 처리해 보겠습니다.

hexdump 와 결합하니 가시성도 나아지고 Raw 데이터가 손에 잡힌 듯 합니다. Raw Packet 데이터를 읽어와서 다룰 때에도 매우 좋을 것으로 생각됩니다.

{% include advertisements.html %}

```python
from requests import get
from os import path

def download_file_from_url(url, rename_as=None):
    """ Url 로부터 파일을 다운로드 받습니다. """
    if not rename_as:
        rename_as = url.split('/')[-1]
    
    fullpath = path.join(path.abspath(path.curdir), rename_as)
    
    with open(rename_as, 'wb') as wf:
        with get(url, stream=True) as response:
            response.raise_for_status()
            content_length = response.headers.get('content-length')
            for chunk in response.iter_content(8192):
                wf.write(chunk)
    return path.join(path.abspath(path.curdir), rename_as)

MP4_SAMPLE = 'https://www.bogotobogo.com/FFMpeg/images/concat/yosemiteA.mp4'
download_file_from_url(MP4_SAMPLE) # 파일 다운로드 및 현재 디렉터리에 저장

with open('./yosemiteA.mp4', 'rb') as rf:
    # 240 bytes 만큼을 mp4 데이터에서 읽어오고, BitStream 은 120*8*2 bits 만큼 읽어옵니다.
    stream = ConstBitStream(bytes = rf.read(120*2), length=120*8*2)
    print("0x%x" % stream.pos)
    hexdump(stream.read(120*8*2).bytes)
    # 포인터(=pos) 값을 변경하여 다시 읽어올 수 있습니다.
    stream.pos = 0
    print("pos: 0x%x \n bitpos: 0x%x " % (stream.pos, stream.bitpos ))
    
    hexdump(stream.read(120*8).bytes)
```

- 아래는 출력 데이터입니다.

{% include advertisements.html %}

```bash
0x0
00000000: 00 00 00 18 66 74 79 70  6D 70 34 32 00 00 00 00  ....ftypmp42....
00000010: 69 73 6F 6D 6D 70 34 32  00 01 1D 5B 6D 6F 6F 76  isommp42...[moov
00000020: 00 00 00 6C 6D 76 68 64  00 00 00 00 CF 38 D9 61  ...lmvhd.....8.a
00000030: CF 38 D9 61 00 00 02 58  00 02 2B F9 00 01 00 00  .8.a...X..+.....
00000040: 01 00 00 00 00 00 00 00  00 00 00 00 00 01 00 00  ................
00000050: 00 00 00 00 00 00 00 00  00 00 00 00 00 01 00 00  ................
00000060: 00 00 00 00 00 00 00 00  00 00 00 00 40 00 00 00  ............@...
00000070: 00 00 00 00 00 00 00 00  00 00 00 00 00 00 00 00  ................
00000080: 00 00 00 00 00 00 00 00  00 00 00 03 00 00 00 15  ................
00000090: 69 6F 64 73 00 00 00 00  10 07 00 4F FF FF 29 15  iods.......O..).
000000A0: FF 00 00 64 F9 74 72 61  6B 00 00 00 5C 74 6B 68  ...d.trak...\tkh
000000B0: 64 00 00 00 0F 00 00 00  00 CF 38 D9 69 00 00 00  d.........8.i...
000000C0: 01 00 00 00 00 00 02 2B  ED 00 00 00 00 00 00 00  .......+........
000000D0: 00 00 00 00 00 00 00 00  00 00 01 00 00 00 00 00  ................
000000E0: 00 00 00 00 00 00 00 00  00 00 01 00 00 00 00 00  ................
pos: 0x0 
 bitpos: 0x0 
00000000: 00 00 00 18 66 74 79 70  6D 70 34 32 00 00 00 00  ....ftypmp42....
00000010: 69 73 6F 6D 6D 70 34 32  00 01 1D 5B 6D 6F 6F 76  isommp42...[moov
00000020: 00 00 00 6C 6D 76 68 64  00 00 00 00 CF 38 D9 61  ...lmvhd.....8.a
00000030: CF 38 D9 61 00 00 02 58  00 02 2B F9 00 01 00 00  .8.a...X..+.....
00000040: 01 00 00 00 00 00 00 00  00 00 00 00 00 01 00 00  ................
00000050: 00 00 00 00 00 00 00 00  00 00 00 00 00 01 00 00  ................
00000060: 00 00 00 00 00 00 00 00  00 00 00 00 40 00 00 00  ............@...
00000070: 00 00 00 00 00 00 00 00                           ........
```

{% include advertisements.html %}

## 결론

지금까지 Raw 데이터를 bit 수준으로 다루는 bitstring 에 대해서 알아보았습니다. BitStream 이 제공하는 메서드와 프로퍼티를 확인해보니 Raw Packet 데이터를 읽어와 Protocol Spec 에 기록된 필드의 데이터를 읽어들여 출력하는 Packet Decoder 프로그램도 쉽게 작성할 수 있을 것으로 생각됩니다. 지금까지 **코마** 였습니다.

구독해주셔서 감사합니다. 더욱 좋은 내용으로 찾아뵙도록 하겠습니다. 감사합니다

# 참조

이번 시간에 참조한 링크는 아래와 같습니다. 잘 정리하셔서 필요할 때 사용하시길 바랍니다.

- [git-scm : Git On the Server](https://git-scm.com/book/en/v2/Git-on-the-Server-Setting-Up-the-Server)

