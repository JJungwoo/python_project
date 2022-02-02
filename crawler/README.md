# python crawler

## requests 

Python 에서 제공하는 HTTP 라이브러리

- requests 설치

```
pip install requets
```

또는

```
pip3 install requets
```

>github: https://github.com/psf/requests

### requests 사용 방법

requests 라이브러리 추가

```python
>>> import requests
```

requests 로 특정 사이트에 html get 요청 후 결과 받아오기

```python
>>> response = requests.get('https://finance.naver.com/')
```

response 타입에서 정보 가져오기

- 요청 성공 결과 200 반환

```python
>>> response.status_code
200
```

- html 문서 반환

```python
>>> response.text
<html> ... 
```

- 파라미터 추가 요청 

```python
>>> response = requests.get('https://finance.naver.com/item/main.naver/', params={'code':'005930'})
```

>참고: https://docs.python-requests.org/en/latest/
