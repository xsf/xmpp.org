---
title: The XMPP Newsletter, 30 November 2018
date: 2018-11-30
author: jcbrand
categories: ["Newsletter"]
aliases:
      - "/2018/11/the-xmpp-newsletter-30-november-2018/"
---

Welcome to the XMPP newsletter.

If you have an article, tutorial or blog post you'd like us to include in the
newsletter, please [submit it on the XMPP wiki](https://wiki.xmpp.org/web/News_and_Articles_for_the_next_XMPP_Newsletter).

## News

In the Netherlands a commercial chat service based on XMPP and a modified version of
the open-source Xabber client for Android was compromised when the Dutch police gained
access to the server and implemented a man-in-the-middle (MITM) attack on encrypted conversations
that used Off-The-Record (OTR) encryption.

OTR and other encryption technologies such as OMEMO only guarantee end-to-end
security if you are able to verify the fingerprints of your contacts' encryption keys. In
this case it appears users did not verify and ignored warnings (which were too small and easily missed),
and this opened the door to a MITM attack by anyone with access to the server.

The attack in this instance was for law enforcement. However it serves to highlight the
importance of designing user interfaces that encourage good security practices, and educating
users. It also highlights problems with centralized services - all IronChat users were on a
single XMPP server, which meant a single place to compromise and access all IronChat
conversations. A federated network does not have a single point through which all messages
pass.

It seems the service was popular with criminals, which is why the police got involved,
and various arrests were made. Here's the [original article in Dutch](https://nos.nl/artikel/2258309-beveiliging-door-politie-gekraakte-cryptofoons-was-twijfelachtig.html)
and here's a [Google machine-translated version](https://translate.google.com/translate?hl=&sl=nl&tl=en&u=https%3A%2F%2Fnos.nl%2Fartikel%2F2258309-beveiliging-door-politie-gekraakte-cryptofoons-was-twijfelachtig.html).

---

{{< newsletter-subscribe >}}


Paul Schaub has written about a [QR-code generator for OMEMO](https://blog.jabberhead.tk/2018/11/03/qr-code-generator-for-omemo/)
which he has been working on. It encodes the Jabber-ID of the owner as well as any OMEMO
fingerprints they choose to include.

JC Brand has written about the [recent XMPP sprint held in Dusseldorf](https://opkode.com/blog/xmpp-sprint-dusseldorf/).
Featuring sushi, ramen, whiskey, protocol discussions, translations, bugfixes, documentation, releases, hacks and coding.

The [Monal iOS and MacOS client now shows a simple introduction to
XMPP](https://monal.im/blog/the-welcome-screen/) with
lovely illustrations of Peter rabbit, as he enters and escapes Mr McGregor's garden.
There are also new [empty state screens](https://monal.im/blog/the-empty-state/) with similar illustrations.

The well-known Kuketz blog in Germany wrote an article [XMPP is not the savior - but a solution](https://translate.google.com/translate?hl=&sl=auto&tl=en&u=https%3A%2F%2Fwww.kuketz-blog.de%2Fmessenger-xmpp-ist-nicht-der-heilsbringer-aber-eine-loesung%2F)
(Google machine-translated version). Here's the [original German version](https://www.kuketz-blog.de/messenger-xmpp-ist-nicht-der-heilsbringer-aber-eine-loesung/).
It's in part a response to [XMPP: Admin-in-the-middle](https://infosec-handbook.eu/blog/xmpp-aitm/), written by the InfoSec Handbook
which details how XMPP server administrators have access to user's metadata and
other sensitive information.

The German email provider mailbox.org, has [unveiled a revamped website](https://mailbox.org/en/post/a-new-logo-a-new-website-new-software-versions-and-new-features-at-mailbox-org)
with new features, including migration to a new XMPP chat server (Ejabberd)
and deployment of [Converse.js](http://conversejs.org/) as webchat.

German IT website Golem.de has written about Daniel Gultsch's new free Android app
[Quicksy](https://play.google.com/store/apps/details?id=im.quicksy.client)
which allows users to sign up with their cellphone number.
Here's the [Google machine-translated
version](https://translate.google.com/translate?hl=&sl=de&tl=en&u=https%3A%2F%2Fwww.golem.de%2Fnews%2Fquicksy-mit-der-telefonnummer-ins-jabber-netz-1811-137855.html)
and the [original German article](https://www.golem.de/news/quicksy-mit-der-telefonnummer-ins-jabber-netz-1811-137855.html).

This Stardust blog post explains how you can [Write an XMPP bot in half an hour](https://starbeamrainbowlabs.com/blog/article.php?article=posts%2F327-Write-an-XMPP-bot-in-half-an-hour.html)

Andrea Schäfer provided a [technical update and demo of Chatty](https://puri.sm/posts/librem5-progress-report-19/),
the XMPP-capable chat client that is being developed for the upcoming Purism phone.
This was posted already a while ago, but only came to my attention recently.

## Upcoming Events

The [23rd XMPP Summit has been announced](https://xmpp.org/2018/11/xmpp-summit-23/).
It will be held on the 31st of January and 1st of February 2019 in Brussels,
Belgium. These are the two days preceding FOSDEM 2019.

## Software releases

### Servers

* [MongooseIM 3.2](https://www.erlang-solutions.com/blog/mongooseim-3-2-meet-our-inbox.html)
* [Prosody 0.10.3](https://blog.prosody.im/prosody-0-10-3-released/), [0.11](https://blog.prosody.im/prosody-0-11-0-released/) and [0.11.1](https://blog.prosody.im/prosody-0-11-1-released/) - The 0.11 release features a rewrite of their MUC component and lots of PubSub improvements.

### Clients

* [Converse 4.0.5](https://github.com/conversejs/converse.js/releases/tag/v4.0.5)
* [Gajim 1.1.0](https://dev.gajim.org/gajim/gajim/blob/gajim-1.1.0/ChangeLog)
* [Opa 0.1.0](https://github.com/credija/opa/releases/tag/0.1.0) - A new webchat client based on Vue.js, Nuxt.js and ElementUI.
* [Quicksy](https://quicksy.im/) - A spin-off of Conversations, but with automatic contact discovery.
* [Yaxim 0.9.3](https://yaxim.org/download/) - Via FDroid or Google Play

### Libraries

* The Prosody project has made various [Lua5.2 comptatible backports for Prosody 0.11](https://blog.prosody.im/lua52-compatible-package-backports/)
* [Strophe 1.3.1](https://github.com/strophe/strophejs/releases/tag/v1.3.1)

### Other software

* [xmpp-websocket-proxy](https://www.ag-software.net/2018/11/19/xmpp-websocket-connection-manager/) - A new XMPP websocket connection manager using using DotNetty and MatriX vNext.
* [Movim 0.14](https://nl.movim.eu/?node/pubsub.movim.eu/Movim/movim-0-14-scotty-anniversary-edition-J8qk3N) - Movim is 10 years old this month and this release has been 9 months in the making.

### Services:

The Public MUC search tool Muclumbus now lives at [search.jabber.network](https://search.jabber.network/)
