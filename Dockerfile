# Dockerfile to build a docker image from XSF/xmpp.org Master
#
# Dave Cridland <dave.cridland@surevine.com>
# Copyright 2017 Surevine Ltd

# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#
FROM gliderlabs/alpine:3.3

MAINTAINER Dave Cridland <dave.cridland@surevine.com>

RUN apk --no-cache add \
    py-pip \
    nginx \
    build-base \
  && pip install pelican==3.3 markdown ghp-import \
  && adduser -D -u 1000 -g 'www' www \
  && mkdir -p /var/www/html \
  && chown -R www:www /var/lib/nginx \
  && chown -R www:www /var/www/html 

WORKDIR /var/tmp/src/xmpp.org
COPY . /var/tmp/src/xmpp.org
RUN cd /var/tmp/src/xmpp.org \
  && make publish \
  && make html \
  && cp -prv output/* /var/www/html \
  && rm -rf /var/tmp/
COPY deploy/nginx.conf /etc/nginx/nginx.conf

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
