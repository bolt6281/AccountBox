# Account Box

## __만들게 된 계기__

나는 가입해놓은 서비스가 많은데 각각 아이디어나 비밀번호가 다르다. 서비스마다 요구하는보안 단계나 원하는 특수기호의 종류와 수가 다르기 때문이다.
그래서 그 많은 계정 정보들을 여태 accounts.txt라는 파일에 보관했는데, 이에는 여러 문제가 있다.

1. 사람이 많은 곳에서 그 파일을 여는게 부담스러움
2. 메모장이라 조잡하게 생김(하이픈으로 계정 구분)
3. 메모장의 ctrl+F에 검색을 의존해야함(매우 불편)

편하고 보기 좋게 계정 정보를 보관하고, 굳이 비밀번호를 확인하지 않아도
클립보드로 복사시켜줘서 사람이 많은 곳에서도 마음 놓고 계정 정보를 이용할 수 있게
해주는 프로그램이 있으면 좋겠다고 생각했다.

## __프로그램 개요__

### 1. _새로운 계정 등록_
    1. 서비스명
    2. ID
    3. 비밀번호(보이기/안 보이기 체크박스)
    4. JSON 형태로 저장


### 2. _계정 정보 확인 및 수정_
    수직 정렬
    1. 왼쪽 단 : 수직 리스트, *검색 기능
    2. 오른쪽 단 : 선택한 서비스에 대한 계정 정보 확인
    아이디, 비밀번호를 보여줌, 클립보드에 복사
    2-1. 수정하기
    2-2. 삭제하기


### 3. _옵션_
    그리드 레이아웃
    1. 파일 저장 위치 선택, 불러오기(선택 미리 안 하면 폴더에 자동으로 생성)

+config 파일이 담는 요소
계정 정보 파일 위치


## __추후 추가 기능__

### 1. _다양한 형태의 정보 등록_
    계정 뿐만 아니라 공인인증서, 카드 번호 등등 기억하기 어려운
    값들도 손쉽게 저장할 수 있게

    저장하는 파일의 형태를 바꾸고 UI에서는 콤보박스(또는 직접 입력)으로 입력
    입력하는 값의 종류의 수를 정할 수 있게(1~3)

    처음 add창 들어가면 ID password만 있음(삭제 및 변경 가능)
    3번째부턴 add -> 콤보박스에서 id 선택

### 2. _프로그램 자체 비밀번호_
    
