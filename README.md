# xmpp.org

[![Build Status](https://travis-ci.com/xsf/xmpp.org.png?branch=master)](https://travis-ci.com/xsf/xmpp.org)
[![Docker Build Status](https://img.shields.io/docker/cloud/build/xmppxsf/xmpp.org)](https://hub.docker.com/r/xmppxsf/xmpp.org/builds/)

Please log any [issues](https://github.com/xsf/xmpp.org/issues/new).

## Contributing new content and updates

* Fork the [code](https://github.com/xsf/xmpp.org/fork) to your own git repository.
* Make your changes in `/content` or [directly](https://github.com/xsf/xmpp.org/tree/master/content) in GitHub.
* When you are happy with your updates, submit a [pull request](https://github.com/xsf/xmpp.org/pulls) describing the changes.
* **IMPORTANT:** Before sending a **Pull Request** make sure that your forked repo is in sync with the base repo.
* The updates will be reviewed and merged in.

## Communication forum

Please use [xsf@muc.xmpp.org](xmpp:xsf@muc.xmpp.org?join) for discussions about the site, content, generation etc.

## Site generation

* Commits to the master branch generate a new build.
* Builds are visible at [Travis-CI](https://travis-ci.com/xsf/xmpp.org/builds)
* Changes will be visible on [xmpp.org](https://xmpp.org) after the next update

## Software Requirements

* Hugo
* Python

## Introduction to Hugo

Hugo’s [quickstart](https://gohugo.io/getting-started/quick-start/) page is a good place to learn about the basics of Hugo (installation, project skeleton, development cycle, etc.).

## Installation instructions

Multiple types of installations are documented:

* Local (regular)
* Docker container
* Vagrant virtual machine

### Regular installation

To run a development server on your local computer, follow these basic steps:

```bash
git clone ssh://git@github.com/xsf/xmpp.org.git
# install Hugo
cd xmpp.org
```

Running the server in development mode (reloads whenever a file is changed):

```bash
make serve
```

View at `http://localhost:1313`

### Docker-based installation

The Makefile will build the website completely by running:

```bash
make -f MakefileDocker
```

It'll do the following:

* Create a build Docker image (`make builder`) which is a development environment with a complete set of dependencies ready.

* Run this docker image on the xmpp.org directory locally. This directory is presumed to contain a checked out repository for the website. (`make site`)

* From the newly created static files in `deploy/output`, it will then create a minimalist docker image to actually serve the website. (`make deployer`)

For development convenience, you can run the website on port 80:

```bash
make -f MakefileDocker serve
```

### Vagrant-based installation

For your convenience, this repository ships with a basic Vagrantfile, which allows you to create virtual machine with all the dependencies required for local development.

Assuming your computer has [Vagrant](https://www.vagrantup.com/) installed, the following will get you a running server:

```bash
git clone ssh://git@github.com/xsf/xmpp.org.git
cd xmpp.org
vagrant up
vagrant ssh
cd /vagrant/
make serve
```

Now, the website should be available at `http://localhost:1313`

## Configuration

```
<repo>
  Dockerfile
  fabfile.py
  MakefileDocker
  Makefile
  README.md
  public
    <generated files>
  content
    <website page files>
  themes
    <website theme>
```

## Local site generation

To just generate a new version (without starting up a local webserver) just do:

```bash
make publish
```

Pages will be available in the /public folder.

## Theme development

You can directly modify the theme (layout and styling) in the [themes/xmpp.org](https://github.com/xsf/xmpp.org/tree/master/themes/xmpp.org/static/css/) directory.
