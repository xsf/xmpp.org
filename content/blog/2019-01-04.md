---
title: The XMPP Newsletter, 4 January 2019
date: 2019-01-04
author: jcbrand
categories: ["Newsletter"]
aliases:
  - "/2019/01/the-xmpp-newsletter-4-january-2019/"
---

Happy 2019 and welcome to the XMPP newsletter.

If you have an article, tutorial or blog post you'd like us to include in the
newsletter, please [submit it on the XMPP wiki](https://wiki.xmpp.org/web/News_and_Articles_for_the_next_XMPP_Newsletter).

## News

Today is [Jabber's 20th anniversary](https://fr.movim.eu/?blog%2Fdebacle%40movim.eu%2Fhappy-birthday-xmpp-20th-anniversary-of-1st-jabber-server-IBmtu8)!
Jabber would later be standardized and renamed to XMPP.

If you'd like a trip down memory lane, have a look at this [2001 Linux Magazine interview with Jeremie Miller](http://www.linux-mag.com/id/902/)
or the [original Slashdot release announcement](https://slashdot.org/story/99/01/04/1621211/open-real-time-messaging-system) by him on 4 January 1999.

Linux Journal has published an article [Lessons in Vendor Lock-in: Messaging](https://www.linuxjournal.com/content/lessons-vendor-lock-messaging),
reflecting on the last 20 years of instant messaging and 
the fact that vendor lock-in is still as relevant an issue as ever.

---

{{< newsletter-subscribe >}}

The Prosody team has written a blog post [welcoming 2019](https://blog.prosody.im/welcoming-2019/)
where they look back at the progress made in 2018 and forward towards what can be expected in 2019.
It also contains a [community survey](https://goo.gl/forms/L1AKnTLXjIAfP27W2) to help the developers
guide their effort for the future.

Tumblr started blocking adult content on December 17th, which caused
many users to complain of false positives and prompted some to look for alternatives.
In response Timothée Jaussoin wrote a [blog post suggesting that Tumblr users migrate to Movim](https://nl.movim.eu/?node/pubsub.movim.eu/Movim/hey-tumblr-users-here-is-why-movim-could-be-the-best-platform-to-migrate-to-BpGnsH).
The post was subsequently [discussed on Hacker News](https://news.ycombinator.com/item?id=18601515)
and was on its front page for a while.

Logitech's Harmony Hub home automation device uses XMPP and they
apparently inadvertently allowed local access to customers.
When a 3rd party cyber security firm found multiple vulnerabilities,
[Logitech made a firmware update that disabled XMPP access](https://arstechnica.com/gadgets/2018/12/logitech-firmware-update-breaks-locally-controlled-harmony-hub-systems/)
thereby angering many users who had added extra functionality via XMPP.
In response Logitech has created a new
[XMPP beta program](https://community.logitech.com/s/question/0D55A00008D4bZ4SAJ/harmony-hub-firmware-update-fixes-vulnerabilities)
that will give users access to the local controls that were removed and they
plan to release an official firmware update with XMPP controls this month.


## Howtos

* [How to configure HAProxy and ejabberd together](https://blog.process-one.net/proxy-protocol-in-ejabberd/).

## Announcements

ProcessOne have [announced](https://blog.process-one.net/new-year-service-cleanup) that they will shut down their free XMPP servers oneteam.im and talkr.im. 

## Videos

In episode [S3E08 of Matrix Live](https://www.youtube.com/watch?v=B0faoVdw0ak),
developer Half-Shot talks about bridging Matrix and XMPP with [matrix-appservice-purple](hTtps://github.com/matrix-org/matrix-appservice-purple).

## Recent Events

Maxime Buquet wrote a [short summary of the XMPP meetup](https://mail.jabber.org/pipermail/members/2018-December/008930.html)
held at the recent Chaos Communication Congress in Leipzig, Germany.

## Upcoming Events

* The [Brussels UX sprint](https://wiki.xmpp.org/web/Sprints/2019_January_Brussels) will be held on Wednesday the 30th of January.
* The [23rd XMPP Summit](https://wiki.xmpp.org/web/Summit_23) will be held on January 31st & February 1st in Brussels.

## Software releases

### Servers

* Ejabberd versions [18.12](https://blog.process-one.net/ejabberd-18-12/) and [18.12.1](https://blog.process-one.net/ejabberd-18-12-1/)
  which add support for XML compression in message archive storage and converting bookmarks from private XML to PEP.
* Openfire version [4.3.0 beta](https://discourse.igniterealtime.org/t/openfire-4-3-0-beta-release/83533)
* Jackal version [0.4.0](https://github.com/ortuman/jackal/releases/tag/v0.4.0) which adds cluster mode support.

### Clients

* BeagleIM version [1.1](https://itunes.apple.com/us/app/beagleim-by-tigase-inc/id1445349494?l=pl&ls=1&mt=12). A new lightweight XMPP client for MacOS.
* ChatSecure version [4.3.6](https://chatsecure.org/blog/chatsecure-v436/)

### Bridges

* [matrix-appservice-purple](https://github.com/matrix-org/matrix-appservice-purple).
   Despite the name, the XMPP stack being used is [XMPP.js](https://github.com/xmppjs/xmpp.js/issues/523) rather than libpurple
