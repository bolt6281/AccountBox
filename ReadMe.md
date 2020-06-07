# Account Box

## __만들게 된 계기__

나는 가입해놓은 서비스가 많은데 각각 아이디어나 비밀번호가 다르다. 모든 비밀번호를 똑같게 하는 게 보안상 좋지 않기도 하고 그 때 그 때 생각나는 걸로 계정을 만들기 때문이다.
그래서 그 많은 계정 정보들을 여태 accounts.txt라는 파일에 보관했는데, 이에는 여러 문제가 있다.
1. 사람이 많은 곳에서 그 파일을 여는게 부담스러움
2. 메모장이라 조잡하게 생김(하이픈으로 계정 구분)
3. 메모장의 ctrl+F에 검색을 의존해야함(매우 불편)
4. 남이 내 노트북으로 accounts파일에 접근 가능
5. 내 PC가 해킹 당하면 accounts파일은 무방비로 노출

이러한 이유들 때문에 암호화도 할겸 더욱 뛰어난 계정 정보
보관용 프로그램이 필요하다고 생각했다.

## __프로그램 개요__


### 1. _Cryptography를 통한 암호화_
    1. 암호 파일 보관 위치 지정
    2. 암호 파일 생성

[참고 영상](https://www.youtube.com/watch?v=H8t4DJ3Tdrg)
### 2. _새로운 계정 등록_

### 3. _계정 정보 확인_
    1. 두 단으로 이루어짐
    2. 왼쪽 단 : 수직 리스트, 검색 기능
    3. 오른쪽 단 : 선택한 서비스에 대한 계정 정보 확인
    아이디, 비밀번호를 보여줌
    4. 클립보드에 복사

### 4. _옵션_
    1. 화면 밝기 조절
    2. 아아디, 비밀번호 보이기 ON/OFF(OFF시 클립보드 복사만 존재)
    3. 