# Python 프로젝트 템플릿

프로젝트에서 범용적으로 사용할 수 있는 템플릿입니다.

패키지 관리 도구로 Rye를 사용합니다.

# 기반 소프트웨어

아래 소프트웨어를 사용하므로 미리 설치해야 합니다.

- rye

아래 rye를 통해 자동으로 설치됩니다.

- python 3.10+
- pre-commit

# How to use

env파일을 복사하여 생성합니다.

```bash
cp .env.example .env
```

필요한 패키지를 설치합니다.

```bash
make install
```

동작확인을 위해 main.py파일을 실행합니다.

```bash
make run_main
```
