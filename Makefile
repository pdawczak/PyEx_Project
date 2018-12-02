PYPATH_SET=PYTHONPATH=./Pyrlang
PY=$(PYPATH_SET) PYRLANG_ENABLE_LOG_FORMAT=1 PYRLANG_LOG_LEVEL=DEBUG python3

.PHONY: start_first_python
start_first_python:
	$(PY) py_app/first.py
