---
title: The XMPP Newsletter, 03 August 2018
date: 2018-08-03
author: jcbrand
categories: ["Newsletter"]
aliases:
    - "/2018/08/the-xmpp-newsletter-03-august-2018/"
---

Welcome to the latest edition of the XMPP newsletter!

If you have an article, tutorial or blog post you'd like us to include in the
newsletter, please [submit it on the XMPP wiki](https://wiki.xmpp.org/web/News_and_Articles_for_the_next_XMPP_Newsletter).

## News

[Slack has acquired HipChat's (and Stride's) intellectual property from
Atlassian](https://techcrunch.com/2018/07/26/atlassians-hipchat-and-stride-to-be-discontinued-with-slack-buying-up-the-ip/).
HipChat was a proprietary service based on non-federated XMPP.

Prosody has added various [PEP improvements](https://blog.prosody.im/pep-improvements-in-trunk/)
which will be included in a future 0.11 release.

The Java XMPP library [Smack now has OpenPGP support](https://blogs.fsfe.org/vanitasvitae/2018/07/30/summer-of-code-smack-has-openpgp-support/).

The Freedombone project now supports automatic [XMPP notifications](https://blog.freedombone.net/xmpp-notifications)
in addition to email notifications. Since publication of this post, Bob Mottram has informed us that
notifications are now sent out as "headline" messages.

[Dino has received a "filter expressions" feature](https://gnomegsoc2018.wordpress.com/2018/07/22/filter-expressions/)
as part of a Google Summer of Code project, allowing advanced search through messages.

[Skype for Business Server will deprecate XMPP Gateways in 2019](https://docs.microsoft.com/en-us/SkypeForBusiness/deprecated).

{{< newsletter-subscribe >}}

## Guides and Howtos

In [XMPP With Node.js](https://ackso.net/post/xmpp-with-nodejs/), Jeremy
Jackson documents how he sets up a development environment for writing an XMPP echo bot in server-side JavaScript.

Divya Prajapati has published a two-part guide on how to create an XMPP Android client:
* [Part 1: OpenFire server installation](https://androworldblog.wordpress.com/2018/07/29/implementing-xmpp-xtensible-messaging-and-presence-protocol-part-1-open-fire-server-installation/)
* [Part 2: Creating an Android XMPP client](https://androworldblog.wordpress.com/2018/07/29/implementing-xmpp-xtensible-messaging-and-presence-protocol-part-2-setup-android-client/)

## Videos

Daniel Gakwaya has made a video showing how to [send and receive files with XMPP](https://www.youtube.com/watch?v=87ioCEG2x1g) using HTTP-upload.

## Software releases

### Servers

* [Jackal 0.3](https://github.com/ortuman/jackal/releases/tag/0.3)
    - Jackal is a relatively new XMPP server written in Go.
      This release adds server-to-server federation support.
* [MongooseIM 3.1](https://www.erlang-solutions.com/blog/mongooseim-3-1-inbox-got-better-testing-got-easier.html)
    - Amongst other things, the `Inbox` feature has received new features, such as MSSQL support and
      support for MUC groupchats.

## Clients

* [Salut à Toi 0.7 alpha](https://www.goffi.org/b/Uj5MCqezCwQUuYvKhSFAwL/salut-alpha-contributors,-take-your-keyboards)
    - Features include forums, photo albums, file sharing and issue tracking.

## Libraries

* [Babbler 0.8.0](https://babbler-xmpp.blogspot.com/2018/07/babbler-080-released.html)
    - Adds support for [XEP-0390: Entity Capabilities 2.0](https://xmpp.org/extensions/xep-0390.html) and [XEP-0392: Consistent Color Generation](https://xmpp.org/extensions/xep-0392.html).
* [aioxmpp 0.10](https://github.com/horazont/aioxmpp)
    An XMPP library for use with Python 3.4+ asyncio.

## Other

* [XMPP Cloud Auth v1.1.0](https://www.jsxc.org/blog/2018/07/24/xcauth-v1.1.0-released.html)
    - Allows you to use Nextcoud as authentication service for XMPP servers.
* [Real-Time Benchmark](https://blog.process-one.net/announcing-rtb-an-open-source-real-time-protocols-benchmark-tool/)
    - An open source benchmarking tool to stress-test real-time protocols, such as XMPP.
* [XMPP Echo bot written in SED](https://github.com/horazont/xmpp-echo-bot)
    - This project received some admiration in this [Hacker News discussion](https://news.ycombinator.com/item?id=17601761)

## New Services

* [Muclumbus](https://muclumbus.jabbercat.org/)
    - A search engine for public Multi-User Chat Rooms
