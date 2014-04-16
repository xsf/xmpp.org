xmpp.org
========
[![Build Status](https://travis-ci.org/xsf/xmpp.org.png?branch=master)](https://travis-ci.org/xsf/xmpp.org)

This repo generates the xmpp.org site (temproarily visible on new.xmpp.org until the grand-switch-over).

Contributing new content and updates
------------------------------------

* Site tasks are visibile on [Trello](https://trello.com/b/ml9e82sE/xmpp-org-website)
* To update, please [fork](https://github.com/xsf/xmpp.org/fork) and submit a pull request
* Editorial questions: [Laura Gill](laura.gill@surevine.com) or [Simon Tennant](simon@buddycloud.com) can help


Site generation
---------------

* Commits to the master branch generate a new build.
* Builds are visible on https://travis-ci.org/xsf/xmpp.org
* New content is deployed to [gh-pages branch](https://github.com/xsf/xmpp.org/tree/gh-pages)
* and visible on new.xmpp.org

Communication forum
-------------------

Please use [members@muc.xmpp.org](xmpp:members@muc.xmpp.org?join) for discussions about the site, content, generation etc.


## Gentle introduction to Pelican

Pelican's [GETTING STARTED](http://docs.getpelican.com/en/latest/getting_started.html/) page is a good place to learn about the basics of Pelican (installation, project skeleton, development cycle, etc.).

### Installation instructions
```bash
git clone ssh://git@github.com/xsf/xmpp.org.git
# install Pelican and dependencies
cd xmpp.org
```
### Requirements

* Pelican 3.3
* ghp-import
* Markdown 2.3.1

### Runing the server in development mode

```bash
make serve
```

If you want the server to autoreload whenever a file change, you can instead do:

```bash
make devserver
```
View at `http://localhost:8000`

### Configuration

```
<repo>
  fabfile.py
  develop_server.sh
  Makefile
  README.md
  pelicanconf.py (development configuration)
  publishconf.py (production configuration)
  output
    <generated files - published to gh-pages branch>
  content
    pages
      <website page files>
  pelican-bootstrap3
    <website theme>
```

### Site generation

To just generate a new version (without starting up a local webserver) just do:

`make html`
