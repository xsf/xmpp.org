#!/usr/bin/env bash

# This script builds the complete website.
# This includes:
#	- building XHTML + PDF versions of the XEPs
#	- put output in content/extensions
#	- put prettify.(js/css) and xmpp.css in content/extensions
#	- building pelican website
#	- fixing pelican website to include a current list of XEPs
#

# Required python packages:
# sudo pip install pelican ghp-import markdown
set -e

PELICAN=pelican
PELICANOPTS=

BASEDIR=$PWD
INPUTDIR=$BASEDIR/content
OUTPUTDIR=$BASEDIR/output
CONFFILE=$BASEDIR/pelicanconf.py
PUBLISHCONF=$BASEDIR/publishconf.py


# create build directory
# this will contain xeps, xsf-tools and texml
mkdir -p build
cd build
if [ -d "xeps" ]; then
	cd xeps
	git pull
	cd ..
else
	git clone https://github.com/xsf/xeps
fi
if [ -d "xsf-tools" ]; then
	cd xsf-tools
	git pull
	cd ..
else
	git clone https://github.com/xsf/xsf-tools
fi
if [ ! -d "texml-2.0.2" ]; then
	wget http://mirror.pnl.gov/macports/distfiles/texml/texml-2.0.2.tar.gz
	tar xfzv texml-2.0.2.tar.gz
	cd texml-2.0.2
	python setup.py build
	cd ..
fi
cd ..

export PYTHONPATH="$PWD/build/texml-2.0.2/build/lib.linux-x86_64-2.7:$PYTHONPATH"
$PWD/build/xsf-tools/build.py -d -x $PWD/build/xeps -o $PWD/content/extensions --imagespath $PWD/build/xeps/resources
cp $PWD/build/xeps/prettify.css $PWD/content/extensions
cp $PWD/build/xeps/prettify.js $PWD/content/extensions
cp $PWD/build/xeps/xmpp.css $PWD/content/extensions
$PELICAN $INPUTDIR -o $OUTPUTDIR -s $PUBLISHCONF $PELICANOPTS
sed -e '/<!--REPLACE_XEPLIST_TABLE_HERE-->/ {' -e 'r content/extensions/xeplist.txt' -e 'd' -e '}' -i output/extensions/index.html
