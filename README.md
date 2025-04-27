# xmpp.org

[![Build Website](https://github.com/xsf/xmpp.org/actions/workflows/build-website.yml/badge.svg)](https://github.com/xsf/xmpp.org/actions/workflows/build-website.yml)

Please log any [issues](https://github.com/xsf/xmpp.org/issues/new).

## Contributing new content and updates

* Fork the [code](https://github.com/xsf/xmpp.org/fork) to your own git repository.
* Make your changes in `/content` or [directly via GitHub](https://github.com/xsf/xmpp.org/tree/master/content).
* When you are happy with your updates, submit a [pull request](https://github.com/xsf/xmpp.org/pulls) describing the changes.
* **IMPORTANT:** Before sending a **Pull Request** make sure that your forked repo is in sync with the base repo.
* The updates will be reviewed and merged in.

## Communication forum

Please use [xsf@muc.xmpp.org](xmpp:xsf@muc.xmpp.org?join) for discussions about the site, content, generation etc.

## Site generation

* Commits to the master branch generate a new build.
* Builds are visible at [Github Actions](https://github.com/xsf/xmpp.org/actions).
* Changes will be visible on [xmpp.org](https://xmpp.org) after the next update.

### Build instructions

Clone this repository:

```bash
git clone ssh://git@github.com/xsf/xmpp.org.git
cd xmpp.org
```

Build locally or via Docker:

* [Local (regular) build](#regular-build)
* [Docker container build](#docker-build)

#### Regular build

To run a development server on your local machine, follow these basic steps.
You need to have the following dependencies installed:

* Hugo
* Python >=3.13
* lua (>=5.2) and lua-expat

The development server will automatically rebuild the page whenever a file is changed:

```bash
make serve
```

View at `http://localhost:1313`

#### Docker build

To build and serve the website locally, simply run:

```bash
docker build -t xmpp-org --build-arg BASEURL=http://localhost/ --build-arg BUILDFUTURE=--buildFuture .
```

It will do the following:

* Build a Docker image with a complete set of dependencies ready.
* Generate the website from the locally checked out xmpp.org repository (`make publish`). This includes rules from `deploy/xsf.conf`.

For development convenience, you can serve the website locally:

```bash
docker run -p 80:80 -t -i xmpp-org
```

View at `http://localhost:80`

## Development

### Repository structure

```
<repo>
  public
    <generated files>
  content
    <website page files>
  themes
    <website theme>
```

### Introduction to Hugo

Hugo’s [quickstart](https://gohugo.io/getting-started/quick-start/) page is a good place to learn about the basics of Hugo (setup, project skeleton, development cycle, etc.).

### Theme development

xmpp.org's theme makes use of:

* [Bootstrap 5.3](https://getbootstrap.com/docs/5.3)
* [FontAwesome 6](https://fontawesome.com/v6/docs)

The theme (layout and styling) can be customized in the [/themes/xmpp.org directory](https://github.com/xsf/xmpp.org/tree/master/themes/xmpp.org).

You can directly modify styles in [themes/xmpp.org/assets/css/style.css](https://github.com/xsf/xmpp.org/blob/master/themes/xmpp.org/assets/css/style.css).
