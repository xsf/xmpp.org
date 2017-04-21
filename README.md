xmpp.org
========
[![Build Status](https://travis-ci.org/xsf/xmpp.org.png?branch=master)](https://travis-ci.org/xsf/xmpp.org)

Please log any [issues](https://github.com/xsf/xmpp.org/issues/new).

Any editorial questions: [Laura Gill](xmpp:laura.gill@surevine.com) or [Simon Tennant](xmpp:simon@buddycloud.com) can help

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
