실사용법

1. 가상환경 사용하기
`python -m venv venv` : 가상환경 선언? 설정?
`source ./venv/Scripts/activate` : 활성화
2. 설치
`pip list` : 이 환경에 있는 설정 보기.
`pip install django` : 최신 버전의 장고 설치. 최신버전 안쓸거니 `==3.2.13` 붙여서 입력하자.
`pip freeze > requirements.txt` : 현재 사용하는 툴의 버전들을 requirements에 기록하기.
`pip install -r requirements.txt` : 클론 한 프로젝트 같은 것의 명시된 최적화 버전 설치.
3. 프로젝트 생성
`django-admin startproject 파일명(==프로젝트 이름)` : 디렉토리가 새로 생기면서 그 안에 프로젝트 폴더 및 manage.py 생성.
`django-admin startproject 파일명(==프로젝트 이름) .` : 디렉토리가 생기지 않고 현재 폴더에 manage.py 및 프로젝트 폴더 생성. 차이는 딱 폴더 하나가 감싸고 있느냐 없느냐 차리.
4. 서버 실행
`python manage.py runserver` : `starting development server at 웹주소` 라는 말이 배쉬창에 뜨는데, 웹주소를 ctrl클릭하면 장고의 로켓 화면 확인 가능.

5. 어플리케이션 App 생성.
`python manage.py startapp 파일명(일반적으로 복수형을 사용한다.` : 파일명의 앱 디렉토리 생성.
주의점 : 앱 생성 후, `settings.py`의 `INSTALLED_APPS`에 프로젝트가 사용하는 앱 목록이 있다. 이곳에 앱 일므을 추가해야 한다. `INSTALLED_APPS` 같은 경우, 커스텀 app, 서드파티app, 장고 기본app 순으로 배치해라.

6. 장고의 코딩 순서는 흘러가는대로 설계한다. url을 받고, view를 통해 제어문을 만들어주고, 반환할, 확인 할 template 혹은 model 이후 https response 순서로 한다.

`path('index/', views.리턴값)`를 추가해 urls에서 view를 지정 가능
view에서 각 함수의 return값은 `render(request, '파일명.html'(파일명에 맞는), context(딕셔너리 자료형))` 형태이다.

6. 장고 템플릿 랭귀지 DTL. 실무에서 안쓰지만 시험에 나옴.

 - Variable : {{키}}를 통해 밸류에 접근 가능
 - Filters : {{키|필터내용}} 간단한 내장함수 같은 느낌.
 - Tags : {% tag %} 다양한 기능 사용 가능. extends로 base를 지정해 중복을 줄일 수 있으며, block으로 또 줄인다. 상속에 이용 가능.
 - Comments : 주석이다. 그냥. ctrl + / 누를 줄 알면 자동 사용됨.

폴더를 만들고 찾을 때는
TEMPLATES에서 DIRS에 추가해도 된다. `BASE_DIR / '폴더명'`을 써도 됨. 트레일링 콤마, appended 콤마를 적어주는걸 습관 들이면 좋다.

7. form
 - label의 for 속성과 input의 id 속성이 세트. input의 name은 `request.GET.get('message')` 리퀘스트에서 부르는 message값과 동일해야함. 서버에서 무슨 기능을 하는 데이터인지 알게 하는 첫번째 관문 같음.
 - form의 속성에서 `target="_blank"`로 주면 새 탭에서 열림.

 8. Trailing slash, Trailing comma : 써라

 9. Variable routing
 - path를 import 하는 경로에 include를 추가로 import해서 사용.
 - `path(url, include('어플이름.urls')` 이런식으로 앱에 맞게 보내줄 수 있다.
 - `path(url(index/ 등), views.index(view에 지정해주는 함수. 리턴값으로 request, html, context를 보낸다.))` 이렇게 처리 했는데 Variable routing을 하면 `path('hello/<str:name>', views.뷰)` 이런식으로 가능하고 아무것도 안적고 <name> 하면 str으로 처리된다.

 - 각 함수의 urls.py에 `app_name = "앱이름"`을 추가하고, 각 path의 인자값 끝에 `name="이름"` 설정해주면, html 파일에서 `<a>앵커 태그</a>`에 `href="{% url 'articles:greeting' %}` url + tab을 이용하고 앱이름:path이름 을 통해 앞 이름이 같은 연결들을 모두 연결 가능하다.


8. 같은 이름의 url들? html파일들?을 비교하는 법

app폴더/templates/앱폴더 동일명칭폴더 -> 샌드위치 구조를 통해 구분.
앱폴더.파일명.html 이런식으로 부르게 된다.














참고1. 장고에서 프로젝트를 만들면 생성되는 기본 파일들
 - 디렉토리 :
    1.` __pycache__` :
    디렉토리. 만들면 생기는 임시 폴더.
    2. `__init__.py` :
    이 폴더를 패키지로 인식하도록 하는 역할.
    3. `asgi.py` :
    애스기. 동기적이냐 비동기적이냐 관리하는 파일.
    4. `settings.py` :
    장고 프로젝트 전반에 대한 세팅들을 지정하게 된다. SECRET_KEY : 프로젝트마다 다르다. 고유의 키이다. 여러 역할 함. 여러가지 세팅을 장고가 미리 잡아뒀다. 중간에 DB, Password, Language code. ko-KR로 한국어 가능. TIME_ZONE 등 하나하나 배울 것이다.
    5. `urls.py` :
    주소 들어온 것을 확인하는 것. urls를 분기해서 알맞는 view에다가 쏙쏙 꽂아주는 것. 장고 공식 문서에는 우편 배달부 역할이라 적혀 있다.
    5-1. 파일에 있는 urlpatterns에 추가하여 처리하는 방법을 추가한다. `admin\` url 기본 제공.
    6. `wsgi.py` :
    기본적으로 실행되는 것. 애스기와 마찬가지로 동기적이냐 비동기적이냐 관리. 위즈기?
 - manage.py : 장고 프로젝트 전반적인 명령어를 내릴 수 있는 기본적인 파일. runserver 등. 수정 안함.
 - db.sqlite3 : 데이터 베이스. 데이터가 들어있는 것. 이 파일이 AWS나 Asure에 있으면  DB가 거기 있는 것이다.

참고2. 앱을 만들면 생성되는 기본 파일들
 - 디렉토리
 오늘은 디렉토리 내의 views.py만 얘기 할 것이다. Model Template View 할 때 그 View다. Template는 직접 만들어줘야 한다. Model은 Models.py가 기본.
1. migrations : 커밋 히스토리와 동일. 데이터베이스의 변경 목록을 migrations을 모아둔다. 커밋 단위가 마이그레이션 단위인 것이다. 나중에 하니 패스
2. init 패스
3. admin : 관리자 관련 건들일 없음 패스
4. apps : 건들 일 없음 패스
5. tests : 건들 일 없음. 테스트 코드를 넣어주면 장고 프로젝트에서 테스트를 해주는 기능.
6. models.py : 데이터 관련










