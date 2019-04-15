VENV := $(shell which virtualenv)
PYTHON3 := $(shell which python3)
PWD := $(shell pwd)

.SILENT:

$(VENV):
	pip install --user virtualenv

install:
	if [ -d venv ]; then \
		echo "Virtualenv already exists"; \
	else \
		$(VENV) -p $(PYTHON3) venv ; \
	fi
	/bin/bash -c "source venv/bin/activate && pip install . && ln -sf $(PWD)/venv/bin/nexusCli ~/.local/bin/nexusCli"
