.POSIX:
.PHONY: clean all
.SUFFIXES: .tr .ps .pdf .png .dot

all: doc/en.pdf doc/ro.pdf graph/net.png graph/ex.png
clean:
	-rm -r graph doc/*.ps doc/en.pdf doc/ro.pdf

.tr.ps:
	TROFFONTS="$(PWD)/font" troff -mcolor -mpictures $< | dpost > $@
.ps.pdf:
	ps2pdf $< $@
.dot.png:
	-sfdp -x -Tpng $< > $@

doc/en.tr doc/ro.tr: doc/logo.eps

graph/net.dot: graph/data.json
	echo 'strict graph net {' > $@
	echo 'ratio=1.41' >> $@
	echo 'overlap=scale' >> $@
	echo 'edge [penwidth=0.5 color="gray25"]' >> $@
	echo 'node [penwidth=2.0 shape="point"]' >> $@
	jq -r '.edges.[] | "\"\(.from)\" -- \"\(.to)\""' graph/data.json >> $@
	echo '}' >> $@
graph/data.json: graph
	curl -s https://xmppnetwork.goodbytes.im/data.json > $@
graph:
	mkdir graph
