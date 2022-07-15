# **Git 이란?**

분산 버전 관리 프로그램

# **Githhub는?**

분산 버전 관리 프로그램 서비스

## CLI 기본적인 명령어

`touch` : 생성

`Mkdir` : 새 폴더. make directory의 줄임말

`ls` : 현재 작업중인 디렉토리의 폴더, 파일 목록을 보여주는 명령어

`cd` :현재 작업중인 디렉토리의 위치를 변경하는 명령어. change directory의 약어

`start`, `open` : CLI를 이용해 GUI에 해당 폴더를 여는 명령어. 윈도우는 `start`, 맥은 `open`이다.

`rm` : remove의 약어로 파일을 삭제하는 명령어. -r 옵션을 주어 폴더를 삭제 할 수 있다. 이 때의 r은 재귀적이라는 의미.

`.` : 나 자신

`..` : 부모

## 1. Git 기본기

### Working Directory

이름 그대로 일하는 폴더.

### Staging Area

변경 사항이 임시저장되는 곳.

### Repository

버전을 저장하는 곳

## 2. Git의 버전 관리 방법

1. `git init`으로 .git 만들면 시작.
2. 파일을 새로 만들면 untracked 상태.
3. git.add로 ""변경 사항들""을 staging area로 옮긴다.
4. untracked 상태가 staged 상태로 변경되며 untracked 상태에서 tracked 상태가 됨. staging 되서 깃으로 버전관리를 하는 상태가 됨.
5. `git.commit` 명령어로 커밋들이 저장되고 repository로 저장.
6. 수정 하면 다시 modified 상태가 됨. untracked는 최초 1회. 추적을 하고 있는 상태라면 modified 상태가 됨. commit된 것을 보고 수정된 commit을 바라보며 둘이 같은지 확인.
7. 반복 (modified-add-commit)되며 commit 1,2,3... 저장됨.

## 3. add commit push pull clone : 매일 해라 짜식들아. 짱 중요하니까 메모 해라

- `git.add` : WD에서 SA로 올리는 기능
- `git.commit` : SA를 R로 옮기는 것.
- `git.push` : local에 있는 commit을 remote로 올리는 것.
- `git.pull` : 
- `git.clone` : remote에 있는 repository를 local로 땡겨오는 명령어. clone 뒤에 주소를 복사해서 붙여넣으면 된다.



* git status : 현재 git으로 관리되고 있는 파일들의 상태를 알 수 있다. 이거 안했는데? + 솔루션마저 제공. version을 바꾸기 위해서는 너가 누군지 알려야 한다. `  git config --global user.email "you@example.com"`
  `  git config --global user.name "Your Name"` 을 이용해서.

- `git log`와 `git diff` : `git log`는 변경 유무를 확인 할 수 있고, `git diff` 는 실제 변경 된 사항을 확인 할 수 있다. `git diff` 다음 자리에는 고유 아이디가 들어간다. (`git log`의 노란색 커밋 아이디. 너무 길기 때문에 앞 4자리로만 입력해도 된다.) 앞의 아이디에 비해 뒤의 어디가 달라졌는지를 확인한다.
   `git diff`를 개이쁘게 보여주는 툴들이 많다. 깃허브도 이쁘고 다른 프로그램 잘 쓰면 더 이쁘게 나온다.

## 4.  Local / Remote Repository

 **로컬**은 작업하는 **repository**, **리모트**는 깃 등 클라우드에 **원격으로 존재**하는 **repository**.

로컬에서 commit 히스토리를 commit 단위로 던지고 리모트가 받는다.

## 5. 깃에서 새 파일 만들기
깃에서 뉴 repository 해서 만든다
repo 이름 정하고
public은 내가 생성한 remote repo에 다른 누가 commit은 불가능. 보는거 가져가는거는 가능
private은 다 안됨.

## 6. `git remote add origin {remote_repo}` (origin = <repo_name>의 별명. 관례상 오리진. 중괄호 빼라.)
 origin 과 remote repo 이름만 달라짐. 한개의 로컬이 여러곳의 리모트 레포를 push 할 수 있다. 싸피에서 필요 없다.
{remote_repo} 는 인터넷 주소. 저기로 던져라 라고 하는데 너무 길어서 별명인 origin을 주어준다. 등록은 관례상 origin이라 적는다.
 위치 저장한다고 보면 됨.

`git push -u origin master`

`git push A B` : A는 어디로 push 할지. origin으로 던지고, B는 로컬에 있는 브랜치의 이름. 브랜치는 일종의 flux 서순표시 같은 느낌. 큰 흐름이 master라는 이름으로 잡혀 있다. master를 푸시할 때 B라는 자리에 적는다.

깃헙 sign in 하면 컴퓨터에 자동으로 저장하고 푸쉬 해준다. 자격 증명을 새로 해줘야 한다ㅠ

 `git push -u origin master`

`git push --set-upstream origin master` -u 로 설정 가능.

## 7. 깃헙에서부터 repository를 받아 생성하기.

 그렇게 할 시 로컬과 깃헙을 동기화 할 필요가 없다.
**더 자주 쓰는 방법이다!**

1. 깃헙에서부터 레포지토리 생성. 생성 시 레포지터리 branch 이름을 자동으로 master가 아니라 main으로 만들 것이다. (master는 master slave가 떠올라서 main이라고 바꿨음. setting에 들어가서 바꿀 수 있음.)

description : readme에 내용을 넣어준다.

initial commit이 깃헙이 찍어서 repository를 만들어 주었다.

2. Local 땡겨오기.

**git push**
`git clone 코드주소`
-> clone_test 땡겨져 옴. 즉 깃에서 직접 만들고 클론을 받아오면 버전 관리를 조금 더 쉽게 받아 올 수 있다.

`code .` 위치의 폴더를 vs code로 열어준다.

clone으로 땡겨왔기에 어디로 push 할 줄 알고, branch를 알기 때문에 그냥 `git push`만 해줘도 된다.