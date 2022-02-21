.PHONY: run
run:
	-pytest-3 test_run_command.py
	-pytest-3 test_write_file.py

.PHONY: lint
lint:
	for i in isort flake8 black pylint ; do $$i *.py ; done
