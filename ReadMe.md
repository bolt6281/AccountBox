![AccountBox](https://user-images.githubusercontent.com/41158977/92348128-0d67d980-f10d-11ea-9472-92fe9a8677cc.png)

AccountBox
==============

## __프로그램 개요__

### 계정 정보 관리 - Tag방식

<img src="https://user-images.githubusercontent.com/41158977/92348777-080b8e80-f10f-11ea-9757-d75f09affc71.png" alt="image" style="zoom: 67%;" />

Account Box는 Tag라는 개념으로 데이터를 관리하고, 분류한다. Tag는 사용자가 직접 제작하고 관리할 수 있는데, 이미지와 같이 이 태그를 이용하는 데이터는

어떤 값을 가지고, 어떤 값은 암호화하고 안 보이게 처리해야 하는지 지정한다. 슬롯은 1개부터 5개까지 늘릴 수 있다.

태그는 필수적으로 1개 이상 존재하며, common은 ID와 Password로 이루어져 있는 기본 태그이다.



### 계정 정보 관리 - 계정 추가

<img src="C:\Users\bolt6281\AppData\Roaming\Typora\typora-user-images\image-20200907133718956.png" alt="image-20200907133718956" style="zoom: 50%;" /><img src="https://user-images.githubusercontent.com/41158977/92348930-8bc57b00-f10f-11ea-9e5e-d5a4be27c10d.png" alt="image" style="zoom: 50%;" />

Add 페이지에서 태그를 고르고, 태그에서 필요한 데이터를 입력하여 계정 정보를 추가할 수 있다.



### 계정 정보 관리 - 조회

<img src="https://user-images.githubusercontent.com/41158977/92349571-7e10f500-f111-11ea-8049-e9ac61d5c4cc.png" alt="image" style="zoom:50%;" /><img src="https://user-images.githubusercontent.com/41158977/92349599-95e87900-f111-11ea-9fe1-67cd2ec0f3fb.png" alt="image" style="zoom: 50%;" />

Retrieve(조회)페이지의 데이터 리스트에서 조회하고자 하는 데이터를 선택하면 우측에 해당 데이터의 정보가 나온다.

불편하게 ctrl+c + ctrl+v를 이용하지 않아도 copy to clipboard버튼을 클릭하여 안전하게 데이터를 복사할 수 있다.

Edit 버튼을 통해 바로 해당 데이터를 수정하는 모드로 넘어갈 수 있다.



### 설정

<img src="https://user-images.githubusercontent.com/41158977/92349619-a39dfe80-f111-11ea-8e30-1f886f137d4d.png" alt="image" style="zoom: 67%;" />

설정 페이지에서는 데이터 관리와 Key 변경이 가능하다.

Reassign data는 기존에 쓰던 데이터를 저장하고, Restore account data는 AccountBox가 있는 폴더에 초기화된 account data파일을 생성한다.

Change는 기존 비밀번호로 데이터를 복호화하고, New key로 새롭게 암호화한다.



### 보안(AES256 Algorithm)

<img src="https://user-images.githubusercontent.com/41158977/92348580-73089580-f10e-11ea-929b-bf166e79cbd2.png" alt="image" style="zoom:50%;" /><img src="https://user-images.githubusercontent.com/41158977/92350005-ab11d780-f112-11ea-8941-ab2fb019b29d.png" alt="image" style="zoom:50%;" />

프로그램을 실행하면 다음과 같이 Key를 입력하는 화면이 나온다. AccountBox는 사용자가 Invisible로 설정해놓은 데이터에 한해 AES256 알고리즘으로 암호화하여 시스템 해킹과 같은 위협으로부터 데이터를 보호한다. 데이터를 읽고, 저장하는 모든 과정에서 데이터의 암호화, 복호화가 진행된다.



-----------

### 실행하는 법

AccountBox2 폴더의 main.exe파일을 직접 실행시키거나 main.exe에 대한 바로가기를 만들어 이용하십시오.

바로가기 파일에 icons폴더의 '64x64 icon.ico'파일을 아이콘으로 적용하여 작업표시줄에서 프로그램의 로고를  볼 수 있습니다.
