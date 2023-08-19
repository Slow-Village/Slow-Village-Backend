# Slow-Village Backend

## 환경 설정

`.env` 파일에 아래 내용을 설정합니다.

```text
MONGODB_USERNAME=<DB 사용자 이름>
MONGODB_PASSWORD=<DB 사용자 비밀번호>
```

## 실행 방법

```bash
docker-compose up -d
```

만약 mongodb만 별도로 실행하고 싶은 경우 다음과 같이 입력해주세요

```bash
docker-compose up -d mongo
```
