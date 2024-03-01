PY := python3
FLAGS := -b
SRC_DIR := src
TESTS_DIR := tests

MAIN_SCRIPT := $(SRC_DIR)/main.py
TEST_SCRIPT := $(TESTS_DIR)/test.py


.PHONY: freeze init test main

freeze:
	pip freeze > requirements.txt


init:
	pip install -r requirements.txt


main:
	$(PY) $(FLAGS) $(MAIN_SCRIPT)


test:
	$(PY) $(FLAGS) $(TEST_SCRIPT)


