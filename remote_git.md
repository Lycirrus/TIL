# 원격 저장소
코드와 버전 관리 이력을 온라인 상에 저장
- 협업 시에 코드를 공유할 수 있는 저장 공간
- ---
### README
git에 대한 설명을 하는 markdown 파일
- 이름이 ***README***이여야 함

### git 함수(2)

`git remote add nickname url` : 로컬 저장소에 원격 저장소 추가

origin : 추적하는 원격 저장소 별칭 (관행적인 첫번째 연결 원격 저장소 - 암묵적인 룰)

orgin이라는 저장소에 등록

`git push nickname master` : 원격 저장소에 commit 목록을 업로드

-> commit을 올리는 것. 파일을 새로 생성했다면, commit으로 올린 다음에 push해야 됨.

- push 역시도 변경된 만큼의 commit만 원격 저장소에 올림
- 모든 작업은 로컬에서 진행되어야 함
- commit 작업은 단방향으로 이루어져야 함
  
- `clone`은 비어있는 로컬에 처음 받을 때 사용하고, `pull`은 이후 변경된 부분만 받을 때 사용한다.

`git clone url` : 원격 저장소 전체를 다운로드
> git init을 하지 말아야 한다

- 이미 master인 디렉토리를 받은 것이기에 다른 로컬 컴퓨터에 받은 디렉토리도 master가 된다

`git pull` : 새로운 변경 내용을 받음

- 이미 clone에서 원격저장소와 연결되었기 때문에 추가적으로 입력할 필요가 없음
- 다만 연결 저장소가 1개일 경우에만 적용