# 주의사항

---

- 현재 버젼에서는 파이썬이 설치가 되어있어야 사용이 가능합니다. 파이썬을 설치 하면서라도 쓰실 분은 아래의 주소에서 다운받아 설치 하시면 됩니다.  
[https://www.python.org/downloads/](https://www.python.org/downloads/)  
추후에 파이썬이 아니어도 할 수 있도록 만들겠습니다.  

# Notion에서의 Markdown

일반적으로 코드 블락이 담겨있는 Markdown을 보시면 아래와 같이 코드의 앞뒤로 주석들이 적혀있습니다. (앞 뒤로 주석'''를 넣으려했지만, 여기 MD에선 자꾸 주석처리가 되어버려 앞에 #을 넣었음을 이해바랍니다)

```shell
#```python    
#sentence = 'hello world'
#print(sentence)
#```
```

하지만 Notion에서 Export All as Markdown을 해서 압축된 파일을 풀고 Markdown을 열어보면 그 안에 Code Block이 아래와 같이 되어있는 것을 확인 하실 수 있습니다. 


```shell
#sentence = 'hello world'
#print(sentence)
```


# 사용법

---

## Pandoc 설치

가장 먼저 아래의 주소에서 pandoc을 다운 받고 설치 합니다. 

[https://pandoc.org/installing.html](https://pandoc.org/installing.html)

## 변환기로 변환하기


```shell
md_converter.py와 변환하고 압축푼 폴더와 같은 경로에 위치해주고, cmd창을 열어서 해당 경로로 이동해줍니다.   
이동 했으면 `python md_converter.py`로 파이썬 파일을 실행해줍니다. 
```

그럼 md 파일들과 같이 아래와 비슷한 결과물이 print 되는 것을 보실 수 있습니다. 

```shell
pandoc -o ../원하는e북이름.epub --highlight-style tango --epub-cover-image ./sources/커버버이미지.png 변환할MD파일.md
```

- 원하는e북이름.epub: 추출할 epub 이름
- —highlight-style: 원하는 코드블럭 스타일
- —epub-cover-image: 원하는 커버이미지 경로
- 변환할MD파일.md: 변환할 md파일. 이는 한 개의 md 뿐만 아니라 여러 md 파일을 연속적으로 넣으면 한번에 변환이 가능합니다.

cmd 창 안에서 print된 위의 코드를 복사하고 md_files라는 폴더로 이동하여 다시 붙여넣기 후 엔터를 쳐줍니다. 


```shell
cd md_files
pandoc -o ../원하는e북이름.epub --highlight-style tango --epub-cover-image ./sources/커버버이미지.png 변환할MD파일.md
```
