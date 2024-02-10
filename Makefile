PY := python3
FLAGS := -b
SRC_DIR := src
TESTS_DIR := tests

MAIN_SCRIPT := $(SRC_DIR)/main.py
TEST_SCRIPT := $(TESTS_DIR)/test.py


.PHONY: run init test freeze


run:
	$(PY) $(FLAGS) $(MAIN_SCRIPT)


init:
	pip install -r requirements.txt


test:
	$(PY) $(FLAGS) $(TEST_SCRIPT)


freeze:
	pip freeze > requirements.txt
