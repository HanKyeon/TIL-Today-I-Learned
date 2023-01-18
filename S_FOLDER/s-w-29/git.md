## 깃 사용 순서

1. `git branch -a` : branch 리스트 확인

2. `git checkout -t origin/develop/FE` : remote branch를 local로 가져오기

3. `git switch develop/FE` : develop/FE 브랜치로 이동

4. `git branch feature/FE/기능이름` : 기능 브랜치 생성

5. `git switch feature/FE/기능이름` 으로 브랜치 이동 후 작업.

6. `git add .` : 스테이징으로 올리기

7. `git commit` : 입력 후 i 키를 입력하여 git message & 내용 편집. esc 이후 :wq 입력 후 엔터하면 커밋.
   7-1. 만약 작업이 끝나지 않았거나 local branch를 remote로 올리고 싶을 경우에는 `git push origin feature/FE/기능이름` 으로 remote로 branch를 올린다.

8. `git switch develop/FE` : develop/FE 브랜치로 이동

9. `git merge feature/FE/기능이름` : develop/FE 브랜치를 feature/FE/기능이름 브랜치와 merge
   9-1. 만약 conflict가 났다면 모여서 맞춰야함!

10. `git push` : develop/BE 브랜치임을 확인한 뒤 push하면 됨.

11. `git branch -d feature/FE/기능이름` : 로컬에서 사용한 브랜치 삭제.
    10-1. 리모트 브랜치를 삭제하고 싶다면? `git push origin --delete 브랜치명`

3~11 반복.
