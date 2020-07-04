
# Baskin Robbins Sariwon 프로젝트 소개 _ Back-End

매월 다양한 맛의 아이스크림을 제공하는 **<a href="https://www.baskinrobbins.co.kr/" style="text-decoration:none; color:orange">배스킨 라빈스 31</a>** 클론 프로젝트

## 개발 인원 및 기간
- 기간 : 2주
- 인원 : 프론트엔드 3명, 백엔드 2명
- <a href=https://github.com/wecode-bootcamp-korea/BR-Sariwon-frontend style="color:orange; text-decoration:none;">프론트엔드 github</a>

## 목적
- 카테고리에 따라 제품이 분류되는 데이터 시스템을 제대로 클론할 것
- 다양한 검색 조건과 그에 따른 결과를 충족시키는 로직을 작성할 것
- 효율적인 쿼리문을 사용하여 메모리와 캐시를 적절히 활용할 것

## 데모영상
<a href="https://www.youtube.com/watch?v=U8hu7C2NRjE&feature=youtu.be">![youtube](https://user-images.githubusercontent.com/42701133/76162146-07089d00-617e-11ea-8702-dfdf34d563a8.png) </a>

<span style="color:gray; display:block; text-align:center">*클릭*</span>

---

# 적용 기술 및 구현 기능
## 적용 기술
- Python, Django web framework
- Beautifulsoup, urllib
- Bcrypt
- Json Web Token
- AWS EC2, RDS
- CORS headers
## 구현 기능
#### User
- 회원가입 및 로그인 (Bcrypt 암호화 및 JWT Access Token 전송) 기능 구현
- 회원가입 유효성 검사 기능 구현
#### Product
- 제품 카테고리별로 메뉴 목록 표출 구현
- 카테고리, 알레르기 유발 요인, 상품 이름에 따라 제품 검색 구현
#### Store
- 전국 매장 위치 표출 구현
- 지역구 필터에 맞춘 매장 검색 구현
- 매장별로 서로 다르게 제공하는 서비스 구현

## API documents (POSTMAN)
1. https://sariwon.postman.co/collections/10479109-bf1cd5af-1652-4246-9616-c10a11a0c514?version=latest&workspace=d1eba454-a49a-4dcf-9e97-ef49ad650bc1

2. https://sariwon.postman.co/collections/10479109-64934c46-4fba-4d50-b1d5-6bb3303a1250?version=latest&workspace=d1eba454-a49a-4dcf-9e97-ef49ad650bc1

## DB 모델링 (AQuery Tool)
![AQuery](https://user-images.githubusercontent.com/42701133/76162153-0d971480-617e-11ea-8d1d-326ca16e5431.png)

---

