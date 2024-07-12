## Git revert
특정 commit을 없었던 일로 만드는 작업

`git revert <commit id>` : revert 명령어
- commit의 message가 아닌 id(컴퓨터를 위한)임을 유의

### Git revert 작동 원리
- 시점 자체가 없었던 일로 취급해야 한다.
- 기록에서 commit이 없어지는 것은 아님
- 마지막 commit에서 특정 시점이 없어진 경우의 결과가 나온다.

git revert를 했을 때 나오는 이상한 창 => **VIM**

>VIM이 왜 떳나요?
>> revert를 쓰면 새로운 미래에 해당하는 commit이 나온다.
>>
>> 그러나 그 commit은 message를 지정하지 않았다!!
>> '이름을 지정해주세요'라는 의미로 나온 것
>>
>> 다만 git에서 자동 생성하는 이름이 있고, 보통 이를 쓴다고 한다.

### git의 모드
- 입력모드와 명령모드가 존재
- vim이 떴을 때는 명령모드 상태로 입력이 안됨
- `i` 키로 입력모드로 들어갈 수 있음
- 명령모드에서 `:`를 하면 커맨드 입력 가능
- `w`는 write, `q`는 quit
- `wq`는 저장하고 나가기
  
### Revert는 왜 commit을 남길까
- 원격 저장소와 commit이 달라져 push가 안됨
- 다른 협업자와의 충돌 발생

### 추가적인 Revert 기능
- id를 나열하여 여러개의 commit을 revert할 수 있다
- `git revert id[0]..id[4]`를 하면 첫 번째에서 다섯 번째 commit까지 revert 할 수 있다
- `git revert --no-edit id`를 사용하면 vim을 띄우지 않고 git이 자동으로 하게끔 할 수 있다
- `git revert --no-commit id`를 하면 미래에 해당하는 변경사항이 Repository에 올라가지 않고 staging area에 머문다. 물론 추후 commit은 따로 해줘야 한다
  > 여러 commit을 revert하면, 여러 미래 commit이 생길 수 있는데, 번거로우니 하나의 미래 commit으로 만드는데 유용할 것이다.

## Git reset
특정 commit으로 돌아가는 작업

`git reset [옵션] <commit id>`

### Git reset 작동 원리
- 되돌리기
- 특정 commit으로 되돌아갔을 때 그 이후 commit은 모두 삭제

### Git의 옵션
commit에 기록된 역사적 사실(파일)들은 옵션을 통해 조절할 수 있음

=> 삭제되는 commit들의 기록을 어떤 영역에 남겨둘 것인가 (working directory, staging area, repository)

`--soft` : 삭제된 commit의 기록을 staging area에 남김
- add가 되어있는 상태로 둠
  
`--mixed` : 삭제된 commit의 기록을 working directory에 남김(Default)

`--hard` : 삭제된 commit의 기록을 남기지 않음

- soft와 mixed는 파일을 살려둔다
- 그러나 하드는 삭제시킨다
- 다행히도 git은 백업을 해놓는다
- `git reflog` : HEAD가 이전에 가리켰던 모든 commit을 보여줌
- 조회하여 복구할 수 있다

## Index
- 파일 내용을 수정 전으로 되돌리기
- Staging area에 올라간 파일을 Unstage하기

### git restore
modified 상태의 파일 되돌리기
- Working Directory에서 파일을 수정한 뒤 파일의 수정사항을 취소하고, 원래 모습으로 되돌리는 작업
- 코드는 내가 어디를 수정했는지 파악하기 어려우니 restore의 힘을 빌린다

`git restore <file>` : file을 modified 전 상황으로 되돌림(마지막 수정사항 제거)
- restore는 수정 전 파일로 덮어쓰는 원리이기에 복구할 수가 없다

### git unstage
- 방법에는 두가지가 있음
- `git rm --cached` or `git restore --staged`

`git rm --cached <file>` : git 저장소에 **<span style='background-color:ff00af'>commit이 없을 경우</span>** staging area에서 unstage

`git restore --staged` : git 저장소에 **<span style = 'background-color:ff00af'>commit이 존재할 경우</span>** staging area에서 unstage

## 궁금한 점
- `git revert`를 이미 revert된 commit이나 revert로 생성된 commit에 적용하면 어떻게 되는가?
- commit한 파일을 gitignore 하기 위해서도 `git rm --cached`을 사용한다. 해당 명령어의 정확한 역할

## 질문에 대해 생각해보기
- 이미 revert된 commit에 다시 revert를 했을 때는 $ 왼편에 'x'아이콘이 뜨면서 실패했고 아무런 변화가 없었다.
- revert로 생성된 미래 commit에 다시 revert를 하였더니 revert 이전 형태로 복구된 것처럼 나타났다
  - 다만 이 역시도 미래 commit이 제거되고 그 이후 미래 commit이 새롭게 생성된 것이라 봐야할 것이다.
- `git rm --cached`은 일반적으로 어떤 파일을 로컬에서는 유지하고 원격 저장소에서는 제거하고 싶을 때 사용한다고 한다
- commit이 있는 경우에는 위 기능과 충돌할 수 있으니 사용하지 않는 것으로 생각된다.

## 공부 내용 돌아보기
revert와 reset은 그 강력한 기능에 비례하여 위험도가 높았다. 그리고 revert의 방식은 신기했다. revert가 commit을 남기는 이유가 특히 그러했다. push는 로컬과 원격 저장소에 새로운 변경사항을 제외한 commit을 공통적으로 가져야 진행되기에 revert가 commit을 날려버리면 작동이 되지 않는 것이다.

repository에 올라온 commit의 변경 방법이 있다면, 그 이전 수정 내역에 대해 되돌리는 방법도 있었다. 그 과정에서 git rm의 기능도 더 확인하게 된 것 같다. git rm은 로컬과 원격 저장소 모두에서 파일을 제거하므로 상황에 따라 조심히 사용해야 할 것이다. 