CREATE TABLE users (
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    age INTEGER NOT NULL,
    country TEXT NOT NULL,
    phone TEXT NOT NULL,
    balance INTEGER NOT NULL
);


SELECT first_name, age FROM users; -- 이름 나이 출력

SELECT * FROM users; -- 전체 조회

SELECT rowid, first_name FROM users; -- rowid와 이름 조회

SELECT first_name, age FROM users ORDER BY age ASC; -- 나이가 어린 순으로 이름 나이 조회
SELECT first_name, age FROM users ORDER BY age DESC; -- 나이가 많은 순으로 이름 나이 조회

-- 이름 나이 계좌 잔고를 나이가 어린 순으로, 같은 나이라면 계좌 잔고가 많은 순으로 정렬해서 조회
SELECT first_name, age, balance FROM users ORDER BY age, balance DESC;

-- 지역 조회하기 
SELECT country FROM users;
-- 중복 없이 모든 지역 조회하기
SELECT DISTINCT country FROM users;
-- 지역 순으로 내림차순 정렬하여 중복없이 모든 지역 조회하기
SELECT DISTINCT country FROM users ORDER BY country;

-- 이름과 지역이 중복 없이 모든 이름과 지역 조회하기. 둘 따로 중복제거를 하는 것이 아니라, 둘을 세트로 본다.
SELECT DISTINCT first_name, country FROM users;
-- 이름과 지역 중복 없이 지역순으로 내림차순 정렬
SELECT DISTINCT first_name, country FROM users ORDER BY country DESC;

----------------------------------------------------
--WHERE

-- 나이가 30살 이상인 사람들의 이름, 나이, 계좌 잔고 조회하기
SELECT first_name, age, balance FROM users WHERE age >= 30;
-- 나이가 30살 이상인 사람들의 이름, 나이, 계좌 잔고 조회하기 이제 잔고가 50만원 초과하는
SELECT first_name, age, balance FROM users WHERE age >= 30 AND balance > 500000;

----------------------------------------------------
-- LIKE : 문장의 패턴을 맞추는 것. 패턴 일치 기반. 대소문자 구분 안함.
-- SELECT, DELETE, UPDATE와 같이 쓰인다.
-- SQLite는 패턴 구성을 위한 두개의 와일드카드 제공. % : 0개 이상의 문자가 올 수 있다. _ : 단일 문자가 있음을 의미.
-- '김%' : 김으로 시작하는 모든 단어들. 김치, 김준호, 김 등
-- '김_' : 김으로 시작하는 두 글자 단어만 허용. 김치, 김밥 등. 
-- '%도' : 도로 끝나는 모든 것
-- '%강원%' : 강원이 포함되는 모든 단어들
-- 섞어서 사용 가능. _2% , 1___, 2_%_% or 2__% 등
-- 와일드카드 문 : 파일을 지정 할 때 여러 파일을 동시에 지정 할 목적으로 사용하는 기호. 언패킹 연산자* 라던가 ?라던가 등. 특정 패턴이 있는 문자열을 찾거나 할 때 사용.

-- 이름에 호가 든 사람 조회
SELECT first_name, last_name FROM users WHERE first_name LIKE '%호%';
-- 이름이 준으로 끝나는 사람 조회
SELECT first_name, last_name FROM users WHERE first_name LIKE '%준';
-- 서울 지역 전화번호를 가진 사람들의 이름과 전화번호 조회
SELECT first_name, phone FROM users WHERE phone LIKE '02-%';
-- 나이가 20대인 사람들의 이름과 나이
SELECT first_name, age FROM users WHERE phone LIKE '2-';
-- 전화번호 중간 4자리가 51로 시작하는 사람들의 이름과 전화번호 조회
SELECT first_name, phone FROM users WHERE phone LIKE '%-51__-%';

------------------------------
-- IN : NOT IN으로 부정 가능
-- 값이 값 목록 결과에 있는 값과 일치하는지 확인
-- 경기도나 강원도에 있는 사람들
SELECT first_name, country FROM users WHERE country IN ('경기도', '강원도');
SELECT first_name, country FROM users WHERE country ='경기도' OR country = '강원도';
-- 안사는
SELECT first_name, country FROM users WHERE country NOT IN ('경기도', '강원도');

----------------------------
-- BETWEEN : 값이 값 범위에 있는지 테스트.
-- 20살 이상 30살 이하 사람
SELECT first_name, age FROM users WHERE age BETWEEN 20 AND 30;
SELECT first_name, age FROM users WHERE age >= 20 AND age <= 30;
-- 20살이상 30살 이하 아닌 사람
SELECT first_name, age FROM users WHERE age NOT BETWEEN 20 AND 30;
SELECT first_name, age FROM users WHERE age < 20 OR age > 30;

-------------------------------
-- LIMIT : 행 수를 제한 할 수 있다.
-- 10명만
SELECT rowid, first_name FROM users LIMIT 10;
-- 부자 순위 탑10
SELECT first_name, balance FROM users ORDER BY balance DESC LIMIT 10;

--------------------------------
-- OFFSET : 리밋절은 지정한 수의 데이터, OFFSET은 특정 지정된 위치에서부터 데이터 조회 리밋과 ㅎ마께 사용.
-- 11부터 20까지
SELECT rowid, first_name FROM users LIMIT 10 OFFSET 10;
-- SELECT *, COUNT(like_users)*10 + (vote_average * 100) + (vote_count) AS sample_score FROM movies_movie ORDER BY sample_score DESC
-----------------------------------
-- GROUP BY : 특정 그룹으로 묶인 결과 생성
-- 좋은 기능인데 깊게 나갈 수는 없다. 데이터를 정리해주는 것이다.
-- 지역을 조회하는데 지역으로 묶어서 집계함수 COUNT를 이요한다. SUM AVERAGE 같은 집계함수 등등.
-- COUNT(*)에 대한 컬럼을 늘려준다.
-- COUNT는 집계 함수이다. Aggregate function. AVG() MAX() MIN() SUM() COUNT()가 있는데 count를 제외하고는 전부 다 숫자로 계산되어야 하기 때문에 INTEGER가 되어야 한다.
-- 만들어지는 컬럼 이름이 바뀔 것이다. 그룹으로 묶어서 카운팅하는 것이기 때문에 조회하는 컬럼을 어떤 이름으로 하느냐에 따라 달라지는 것이 없다. COUNT는. AS 키워드를 통해 컬럼 이름을 바꿔줄 수 있따.
SELECT country, COUNT(*) FROM users GROUP BY country;
SELECT country, COUNT(*) AS number_of_name FROM users GROUP BY country;

-- CRUD CRUD CRUD CRUD
-- C
-- 컬럼 목록은 생략 가능. 생성. 컬럼을 생략하면 모든 컬럼이므로 VALUES의 갯수가 컬럼의 갯수와 같아야 한다.
INSERT INTO 테이블 이름 (어떤컬럼에, 넣을지, 컬럼 목록, 작성) VALUES (컬럼 목록 순서에, 맞춰서, 값을, 넣어준다.)
-- 여러 행 삽입은 column 목록을 나열하여 넣으면 된다. VALUES (), (), (), ();

-- U
-- SET와 WHERE를 쓴다.
-- 여기서 WHERE를 걸지 않으면 모두 다 변경이 된다. 조건이 없으므로.
SET 컬럼1 = 새 값,
    컬럼2 = 새값2
WHERE 조건 걸기;

--D
-- DELETE FROM과 WHERE를 쓴다.
-- 마찬가지로 WHERE가 없으면 전부 다 지워버린다.
DELETE FROM 테이블 이름 WHERE 검색 조건;




