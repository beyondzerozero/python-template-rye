# .PHONY로 정의하여 태스크 러너를 쉽게 정의함 

# install
.PHONY: install
install:
	rye pin 3.10
	rye sync
	rye run pre-commit install

# main.py실행 
.PHONY: run_main
run_main:
	python src/main.py

# pre-commit을 명시적으로 실행 
.PHONY: pre-commit
pre-commit:
	rye run pre-commit run --all-files

.PHONY: test
test:
	rye run pytest tests
