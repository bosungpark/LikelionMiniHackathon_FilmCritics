# Likelion_MiniHackathon
'멋쟁이 사자처럼' 미니 해커톤에서 구현한 영화 평론 사이트입니다.

![image](https://user-images.githubusercontent.com/81157873/147315631-8d95d7c5-affb-4456-8b4e-a20fceeba993.png)

장고를 이용해 개발하였습니다.

영화의 데이터는 JSON을 이용하여 불러왔습니다.

## 주요 기능

-영화 평론 기능

-계정 관련 기능

## 설치 방법

IDE는 VS Code를 기준으로 합니다.

깃에서 초기 파일을 내려 받는 방법 (VS code에서 빈 폴더 생성 후)

```
$ git clone https://github.com/bosungpark/Likelion_MiniHackathon.git
```

가상환경 생성하기 및 켜기

```
$ cd Likelion_MiniHackathon
$ python3 -m venv myvenv
$ source myvenv/bin/activate      //Mac
$ source myvenv/scripts/activate  // Windows
```

#### 프로젝트에 필요한 패키지 다운로드
```
$ pip install -r requirements.txt
```
#### .env 파일 생성 
  - 프로젝트 루트 디렉토리 (`/Likelion_MiniHackathon`)에 작성
```
$ touch .env
```
  - 필요 환경변수
  ```bash
  SECRET_KEY=
  ```

확인 및 실행

```
$ cd movie
$ python manage.py runserver
```

## 사용 예제

1.자유롭게 영화 평론을 할 수 있다.


## 개발 환경 설정

```
$ pip install -r requirements.txt
```

* 0.0.1
    * 작업 진행 중

## 정보

박보성 – [@블로그에서 영상 확인하기](https://blog.naver.com/qkrqhtjd0806/222445259729) – 이메일: qkrqhtjd0806@naver.com


## 기여 방법

1. (<https://github.com/yourname/yourproject/fork>)을 포크합니다.
2. (`git checkout -b feature/fooBar`) 명령어로 새 브랜치를 만드세요.
3. (`git commit -am 'Add some fooBar'`) 명령어로 커밋하세요.
4. (`git push origin feature/fooBar`) 명령어로 브랜치에 푸시하세요. 
5. 풀 리퀘스트를 보내주세요.
