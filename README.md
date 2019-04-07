xmpp.org
========
[![Build Status](https://travis-ci.org/xsf/xmpp.org.svg?branch=master)](https://travis-ci.org/xsf/xmpp.org)
[![Docker Build Status](https://img.shields.io/docker/build/xmppxsf/xmpp.org.svg)](https://hub.docker.com/r/xmppxsf/xmpp.org/builds/)
[![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://subgit.com/files/subgit-3.3.5.zip?template=https://github.com/rauchg/slackin/tree/0.7.3) [![Deploy to Azure](http://azuredeploy.net/deploybutton.svg)](https://azuredeploy.net/)
​[![Code Coverage Status](https://img.shields.io/pypi/v/sphinx.svg)](https://pypi.org/project/Sphinx/) [![CircleCI Build Status](https://circleci.com/gh/electron/electron/tree/master.svg?style=shield)](https://circleci.com/gh/electron/electron/tree/master) [![AppVeyor Build Status](https://windows-ci.electronjs.org/api/projects/status/nilyf07hcef14dvj/branch/master?svg=true)](https://windows-ci.electronjs.org/project/AppVeyor/electron/branch/master) [![Code Coverage Status](https://codecov.io/gh/sphinx-doc/sphinx/branch/master/graph/badge.svg)](https://codecov.io/gh/sphinx-doc/sphinx)
<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License</a>.

https://subgit.com/files/subgit-3.3.5.zip
[![asciicast](https://asciinema.org/a/14.png)](https://asciinema.org/a/14)


Please log any [issues](https://github.com/xsf/xmpp.org/issues/new).

Contributing new content and updates
------------------------------------
 
* Fork the [code](https://github.com/xsf/xmpp.org/fork) to your own git repository.
* Make your changes in `/content/pages` or [directly](https://github.com/xsf/xmpp.org/tree/master/content/pages) in GitHub. 
* When you are happy with your updates, submit a [pull request](https://github.com/xsf/xmpp.org/pulls) describing the changes.
* **IMPORTANT** :- Before sending a **Pull Request** make sure that your forked repo is in sync with the base repo.
* The updates will be reviewed and merged in.

Communication forum
-------------------

Please use [xsf@muc.xmpp.org](xmpp:xsf@muc.xmpp.org?join) for discussions about the site, content, generation etc.

Site generation
---------------

* Commits to the master branch generate a new build.
* Builds are visible at https://travis-ci.org/xsf/xmpp.org/builds
* Changes will be visible on http://xmpp.org after the next update

## Software Requirements

* Pelican 3.3
* ghp-import
* Markdown 2.3.1

## Gentle introduction to Pelican

Pelican's [QUICKSTART](http://docs.getpelican.com/en/latest/quickstart.html) page is a good place to learn about the basics of Pelican (installation, project skeleton, development cycle, etc.).

## Installation instructions 

Two types of installations are documented: a regular one, and one that creates a virtual environment via Vagrant.

### Regular installation
To run a development server on your local computer, follow these basic steps:

```bash
git clone ssh://git@github.com/xsf/xmpp.org.git
# install Pelican and dependencies
cd xmpp.org
```

Running the server in development mode:

```bash
make serve
```

If you want the server to autoreload whenever a file change, you can instead do:

```bash
make devserver
```

View at `http://localhost:8000`

### Docker-based installation

The Makefile will build the website completely by running `make -f MakefileDocker`. It'll do
the following:

* Create a build Docker image (`make builder`) which is a development
environment with a complete set of dependencies ready.

* Run this docker image on the xmpp.org directory locally. This directory
is presumed to contain a checked out repository for the website. (`make site`)

* From the newly created static files in `deploy/output`, it will then create
a minimalist docker image to actually serve the website. (`make deployer`)

For development convenience, you can run the website on port 8080 by `make -f MakefileDocker serve`

### Vagrant-based installation
For your convenience, this repository ships with a basic Vagrantfile, which allows you to create virtual machine with all the dependencies required for local development.

Assuming your computer has [Vagrant](https://www.vagrantup.com/) installed, the following will get you a running server:
```bash
git clone ssh://git@github.com/xsf/xmpp.org.git
cd xmpp.org
vagrant up
vagrant ssh
cd /vagrant/
make devserver
```

Now, the wesite should be available at `http://localhost:8000`

## Configuration

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

## Site generation

To just generate a new version (without starting up a local webserver) just do:

`make html`


Theme development
-----------------

You can modify the theme (layout and styling) in the [xmpp.org-theme](https://github.com/xsf/xmpp.org/tree/master/xmpp.org-theme/sass) directory.

Make changes to Sass files, *not* compiled CSS.

`npm i` then run `grunt` to compile Sass.
