PY=python3
HUGO=hugo

BASEDIR=$(CURDIR)
INPUTDIR=$(BASEDIR)/content
OUTPUTDIR=$(BASEDIR)/public
TOOLSDIR=$(BASEDIR)/tools

FTP_HOST=localhost
FTP_USER=anonymous
FTP_TARGET_DIR=/

SSH_HOST=localhost
SSH_PORT=22
SSH_USER=root
SSH_TARGET_DIR=/var/www

S3_BUCKET=my_s3_bucket

CLOUDFILES_USERNAME=my_rackspace_username
CLOUDFILES_API_KEY=my_rackspace_api_key
CLOUDFILES_CONTAINER=my_cloudfiles_container

DROPBOX_DIR=~/Dropbox/Public/

help:
	@echo 'Makefile for a hugo web site                                           '
	@echo '                                                                       '
	@echo 'Usage:                                                                 '
	@echo '   make html                        (re)generate the web site          '
	@echo '   make clean                       remove the generated files         '
	@echo '   make publish                     generate using production settings '
	@echo '   make serve                       serve site at http://localhost:1313'
	@echo '   make prepare_docker              prepare site for serving via docker'
	@echo '   make ssh_upload                  upload the web site via SSH        '
	@echo '   make rsync_upload                upload the web site via rsync+ssh  '
	@echo '   make dropbox_upload              upload the web site via Dropbox    '
	@echo '   make ftp_upload                  upload the web site via FTP        '
	@echo '   make s3_upload                   upload the web site via S3         '
	@echo '   make cf_upload                   upload the web site via Cloud Files'
	@echo '   make github                      upload the web site via gh-pages   '
	@echo '                                                                       '

html:
	$(HUGO)

clean:
	[ ! -d $(OUTPUTDIR) ] || rm -rf $(OUTPUTDIR)

serve:
	$(PY) $(TOOLSDIR)/prepare_xep_list.py
	$(HUGO) version
	$(HUGO) server --bind=0.0.0.0 --baseURL="http://localhost/"

prepare_docker:
	$(PY) $(TOOLSDIR)/prepare_xep_list.py
	$(HUGO) version
	$(HUGO) --baseURL="http://localhost/"

publish:
	$(PY) $(TOOLSDIR)/prepare_xep_list.py
	$(PY) $(TOOLSDIR)/lint-list.py clients.json
	$(PY) $(TOOLSDIR)/lint-list.py servers.json
	$(PY) $(TOOLSDIR)/lint-list.py libraries.json
	$(HUGO) version
	$(HUGO)

ssh_upload: publish
	scp -P $(SSH_PORT) -r $(OUTPUTDIR)/* $(SSH_USER)@$(SSH_HOST):$(SSH_TARGET_DIR)

rsync_upload: publish
	rsync -e "ssh -p $(SSH_PORT)" -P -rvz --delete $(OUTPUTDIR)/ $(SSH_USER)@$(SSH_HOST):$(SSH_TARGET_DIR) --cvs-exclude

dropbox_upload: publish
	cp -r $(OUTPUTDIR)/* $(DROPBOX_DIR)

ftp_upload: publish
	lftp ftp://$(FTP_USER)@$(FTP_HOST) -e "mirror -R $(OUTPUTDIR) $(FTP_TARGET_DIR) ; quit"

s3_upload: publish
	s3cmd sync $(OUTPUTDIR)/ s3://$(S3_BUCKET) --acl-public --delete-removed

cf_upload: publish
	cd $(OUTPUTDIR) && swift -v -A https://auth.api.rackspacecloud.com/v1.0 -U $(CLOUDFILES_USERNAME) -K $(CLOUDFILES_API_KEY) upload -c $(CLOUDFILES_CONTAINER) .

github: publish
ifeq ($(TRAVIS_PULL_REQUEST), false)
	ghp-import -n $(OUTPUTDIR)
	mkdir /tmp/xep-images
	curl -o /tmp/xep-images/xmpp-text.pdf  https://xmpp.org/images/xmpp-text.pdf
	curl -o /tmp/xep-images/xmpp.pdf       https://xmpp.org/images/xmpp.pdf
	git clone https://github.com/xsf/xeps /tmp/xeps
	git clone https://github.com/xsf/xsf-tools /tmp/xsf-tools
	export PYTHONPATH=$PYTHONPATH:/usr/local/lib/python2.7/dist-packages/
	/tmp/xsf-tools/build.py -d -x /tmp/xeps -o /home/travis/build/xsf/xmpp.org/output/extensions --imagespath /tmp/xep-images
	@git push -fq https://${GH_TOKEN}@github.com/$(TRAVIS_REPO_SLUG).git gh-pages > /dev/null
endif
.PHONY: html help clean serve publish ssh_upload rsync_upload dropbox_upload ftp_upload s3_upload cf_upload github
