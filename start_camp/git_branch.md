# Branch
## Git Branch
작업 공간을 나누어 독립적으로 진행하기 위한 Git의 도구

## Branch 장점
1. master는 원본이자 최종 제출본
2. 손쉽게 생성 가능

## Branch Commend
- `git branch` : 브랜치 목록 확인
- `git branch -r` : 원격 저장소의 브랜치 목록 확인
- `git branch <name>` : 새로운 브랜치 생성
- `git branch -d <name>` : 브랜치 삭제 (병합된 브랜치만)
- `git branch -D <name>` : 브랜치 삭제 (강제 삭제)

- `git switch <other name>` : 다른 브랜치로 전환
- `git switch -c <other name>` : 새 브랜치 생성 후 전환
- `git switch -c <other name> <commit ID>` : 특정 커밋에서 새 브랜치 생성 후 전환

## Git merge
여러 branch들을 하나로 병합

- `git merge <병합 브랜치 이름>` : 상대방 브랜치 이름을 입력

> HEAD 확인 필수
> 
> 수신 위치에 HEAD가 위치해야 함
> 
> 최신커밋인지 확인

### Fast-Forward Merge
- 브랜치를 실제로 병합하는 대신 현재 브랜치 상태를 대상 브랜치 상태로 이동

- 병합이 완료된 branch는 수명이 다했다고 간주하여 삭제

### 3-Way Merge
- 병합하는 병합하는 각 브랜치의 commit 2개와 공통 조상 commit 하나를 사용하여 병합

## 협업
### Feature Branch Workflow
각 사용자가 원격 저장소의 소유권을 공유 받는 방식

### Forking Workflow
원본 저장소를 복제하여 사용