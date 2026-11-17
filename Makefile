BASEDIR=$(CURDIR)
INPUTDIR=$(BASEDIR)/content
OUTPUTDIR=$(BASEDIR)/public

BASEURL=https://xmpp.org/
BUILDFUTURE=""

help:
	@echo 'Makefile for xmpp.org                                                  '
	@echo '                                                                       '
	@echo 'Usage:                                                                 '
	@echo '   make clean                       remove the generated files         '
	@echo '   make serve                       serve site at http://localhost:1313'
	@echo '   make publish                     generate using production settings '
	@echo '                                                                       '

clean:
	[ ! -d $(OUTPUTDIR) ] || rm -rf $(OUTPUTDIR)

serve:
	uv sync
	pre-commit install
	uv run xmpp_org build_xep_list
	uv run xmpp_org build_rfc_list
	uv run xmpp_org build_software_list
	hugo version
	hugo server --bind=0.0.0.0 --baseURL="http://localhost/" --buildFuture

publish:
	uv sync
	uv run xmpp_org build_xep_list
	uv run xmpp_org build_rfc_list
	uv run xmpp_org lint_software_list
	uv run xmpp_org build_software_list
	hugo version
	hugo --baseURL=$(BASEURL) $(BUILDFUTURE)

.PHONY: help clean serve publish
