CONTENT_DIR=$(CURDIR)/content
OUTPUT_DIR=$(CURDIR)/output
CONF_FILE=$(CURDIR)/pelicanconf.py
PUBLISH_CONF=$(CURDIR)/PUBLISH_CONF.py
PUBLISH_DIR=$(CURDIR)/site
PELICAN_OPTS=

DEBUG ?= 0
ifeq ($(DEBUG), 1)
	PELICAN_OPTS += -D
endif

RELATIVE ?= 0
ifeq ($(RELATIVE), 1)
	PELICAN_OPTS += --relative-urls
endif

PORT ?= 0
ifneq ($(PORT), 0)
	PELICAN_OPTS += -p $(PORT)
endif


help:
	@echo 'Makefile for a pelican Web site                                           '
	@echo '                                                                          '
	@echo 'Usage:                                                                    '
	@echo '   make clean                          remove all the generated files     '
	@echo '   make dev [PORT=8000]                serve and regenerate together      '
	@echo '   make publish                        regenerate site files              '
	@echo '                                                                          '
	@echo 'Set the DEBUG variable to 1 to enable debugging, e.g. make DEBUG=1 html   '
	@echo 'Set the RELATIVE variable to 1 to enable relative urls                    '
	@echo '                                                                          '

clean:
	rm -rf output && find ./site/ -type f ! -name "README.md" -delete

dev:
	pelican -lr "$(CONTENT_DIR)" -o "$(OUTPUT_DIR)" -s "$(CONF_FILE)" $(PELICAN_OPTS)

publish:
	make clean && pelican -d "$(CONTENT_DIR)" -o "$(OUTPUT_DIR)" -s "$(CONF_FILE)" $(PELICAN_OPTS) --ignore-cache && cp output/* site/

.PHONY: help clean dev publish