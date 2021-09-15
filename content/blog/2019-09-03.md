---
title: The XMPP Newsletter, 03 September 2019
date: 2019-09-03
author: nyco
categories: ["Newsletter"]
aliases:
    - "/2019/09/newsletter-03-september/"
---

Welcome to the September edition of the XMPP Newsletter!

Loads of news for these two months of July and August: two events in Lyon and Stockholm (more to come), new tools, new server releases (Openfire, ejabberd), lots of client releases (Kaidan, Salut à Toi, Xabber Android, Movim, Converse, Beagle IM and Siskin IM). We also experiment a new section about XEP, or specifications.

Please [submit your XMPP/Jabber articles, tutorials or blog posts](https://wiki.xmpp.org/web/News_and_Articles_for_the_next_XMPP_Newsletter) on our wiki.

{{< newsletter-subscribe >}}

## Articles

Georg Lukas posted an article about the [10 years of yaxim](https://yaxim.org/blog/2019/08/23/happy-birthday/)!

Marek Foss of ProcessOne, details the story on how they have [deployed an XMPP geocluster](https://blog.process-one.net/uniting-global-football-fans-with-an-xmpp-geocluster/) for the FIFA World Cup in Brazil.

Cyril Brulebois wrote a short piece on [Sending HTML messages with Net::XMPP](https://mraw.org/blog/2019/08/17/Sending_HTML_messages_with_Net_XMPP/) (Perl).

## Events

Maxime “pep.” Buquet reports on the [XMPP sprint in Lyon](https://bouah.net/2019/07/new-sprint-new-goodies/) in July held at Wisolv's offices: DOAP - Description Of A Project, Reactions, Occupant-id, and more.

The next [XMPP sprint in Stockholm](https://wiki.xmpp.org/web/Sprints/2019_September_Stockholm) will be held on September 28th and 29th, in the Nacka Municipality.

A few [XMPP hackers met in Ziegeleipark, Mildenberg, Germany](https://wiki.xmpp.org/web/Camp2019) in August, for the Chaos Communication Camp 2019, an open-air hacker camp and party that takes place every four years, organized by the Chaos Computer Club (CCC).

The regular meetups in Bavaria is held every third Monday every month. Next will [take place 2019-09-16](https://wiki.xmpp.org/web/Meetups/Bavaria).

If you organise an event in your city, please [submit your meetups on the wiki](https://wiki.xmpp.org/web/Meetups).

## Software releases

### Servers

[Prometheus XMPP Blackbox Exporter](https://github.com/horazont/prometheus-xmpp-blackbox-exporter) (Apache license 2.0) allows you to probe XMPP services and export metrics from the probes to Prometheus.

The igniterealtime community has announced multiple releases:

* [Openfire 4.4.1](https://discourse.igniterealtime.org/t/openfire-4-4-1-release/85857)
* [Monitoring Service 1.8.0 and inVerse 4.2.0.1 plugins](https://discourse.igniterealtime.org/t/monitoring-service-1-8-0-and-inverse-4-2-0-1-plugins-released/85601)
* [Thread Dump 1.0.0 plugin](https://discourse.igniterealtime.org/t/thread-dump-1-0-0-plugin-released/85794)

Antonino Siena has announced [xmpp-http-upload](https://gitlab.com/nifker/xmpp-http-upload), a lightweight and efficient HTTP upload server for XMPP (MIT license).

Mickaël Rémond has announced [ejabberd 19.08](https://blog.process-one.net/ejabberd-19-08/), with JSON Web Token, configuration validator, improved scalability, and more.

Jérôme "Goffi" Poisson has announced [SàT PubSub 0.3.0](https://www.goffi.org/b/XL5aGAa6wymUt4mAhnzGpm/pubsub-been-released), a server independent PEP/PubSub XMPP service, which aims to be complete and universal.

### Clients

[Kaidan 0.4.0](https://www.kaidan.im/2019/07/08/kaidan-0.4.0/) and [0.4.1](https://www.kaidan.im//2019/07/16/kaidan-0.4.1/) have been released, and is available to download on Linux, Windows, and macOS (and experimental Android and Ubuntu Touch).

Jérôme "Goffi" Poisson has released [Salut à Toi v0.7 « La Commune »](https://www.goffi.org/b/N29CuUQS4U4TK36JFuTQ5Q/salut-commune) with tons of changes (and writes regular [SàT progress notes](https://www.goffi.org/b/Gjm7Z5AUt4xh8gciV6wWSe/progress-note)).

[Xabber Android 2.6.4 (634)](https://www.xabber.com/android/) has been released on Google Play, with improved message archive synchronization, improved startup speed, support of references in messages (files, forwards, markup (bold, italic, etc), mentions, quotes), image compression setting, visual changes, and more.

Timothée Jaussoin has released [Movim 0.15 – Donati](https://nl.movim.eu/?post/pubsub.movim.eu/Movim/fd1921c6-219f-477b-a4be-ebb25e4cccc5), with reactions, publication sharing, and more.

JC Brand has released Converse, the web based XMPP/Jabber chat client, in versions [5.0.0](https://github.com/conversejs/converse.js/releases/tag/v5.0.0) and [5.0.1](https://github.com/conversejs/converse.js/releases/tag/v5.0.1), with lots of improvements.

Wojciech Kapcia, of Tigase, has announced two versions of [Beagle IM from macOS and Siskin IM for iOS](https://tigase.net/blog-entry/beagleim-32-and-siskin-im-52-released).

### Libraries

Lance "legastero" Stout has released [StanzaJS](https://stanzajs.org) (formely known as Stanza.io), the JS XMPP library with a JSON API, in multiple versions 12.x.

JC Brand has released the [strophejs library in version 1.3.4](https://github.com/strophe/strophejs/releases/tag/v1.3.4).

Florian "Flow" Schmaus has [announced the extension of the jXMPP library](https://discourse.igniterealtime.org/t/announcing-the-xmpp-strings-testframework/85954) by a testframework for “XMPP-Strings”, as well as [Smack 4.4.0-alpha2](https://discourse.igniterealtime.org/t/smack-4-4-0-alpha2-released/85670).

## Services

Sadly, Arc Games has [announced an XMPP sunset](https://www.arcgames.com/en/forums/startrekonline/#/discussion/1250600/xmpp-sunset): "As of September 19th, 2019, Star Trek Online will no longer be supporting connection to our internal chat system via an XMPP client."


## Extensions and specifications

This section of the newsletter is new and experimental: please let us know what you think.

We start with the XEPs in "LAST CALL", since these are the highest priority in terms of feedback.
We move on to the new XEPs so you can learn of their existence, and then the obsoleted ones so you phase them out.
We finally finish with the updates.
On more section: the friendly specifications.

### Last Call

#### XEP-0353: Jingle Message Initiation

Title: Jingle Message Initiation

Abstract: This specification provides a way for the initiator of a Jingle session to propose sending an invitation in an XMPP message stanza, thus taking advantage of message delivery semantics instead of sending IQ stanzas to all of the responder's online resources or choosing a particular online resource.

URL: https://xmpp.org/extensions/xep-0353.html

This Last Call begins today and shall end at the close of business on 2019-08-13.

#### XEP-0300: Use of Cryptographic Hash Functions in XMPP

Title: Use of Cryptographic Hash Functions in XMPP

Abstract: This document provides a common wire format for the transport of cryptographic hash function references and hash function values in XMPP protocol extensions.

URL: https://xmpp.org/extensions/xep-0300.html

This Last Call begins today and shall end at the close of business on 2019-08-13.

### New

#### XEP-0421: Anonymous unique occupant identifiers for MUCs

Version 0.1.0 of XEP-0421 (Anonymous unique occupant identifiers for MUCs) has been released.

Abstract: This specification defines a method that allows clients to identify a MUC participant across reconnects and renames. It thus prevents impersonification of anonymous users.

Changelog:
Accepted by vote of Council on 2019-07-17. (XEP Editor (jsc))

URL: https://xmpp.org/extensions/xep-0421.html

#### XEP-0420: Stanza Content Encryption

Version 0.1.0 of XEP-0420 (Stanza Content Encryption) has been released.

Abstract: The Stanza Content Encryption (SCE) protocol is intended as a way to allow clients to securely exchange arbitrary extension elements using different end-to-end encryption schemes.

Changelog:
Accepted by vote of Council on 2019-06-26. (XEP Editor (jsc))

URL: https://xmpp.org/extensions/xep-0420.html

### Obsoleted

#### XEP-0387: XMPP Compliance Suites 2018

Version 1.0.0 of XEP-0387 (XMPP Compliance Suites 2018) has been released.

Abstract: This document defines XMPP protocol compliance levels.

Changelog:
Move to Draft as per Council vote on 2018-01-24. (XEP Editor (jwi))

URL: https://xmpp.org/extensions/xep-0387.html

### Updated

* Version 0.3.0 of XEP-0414 (Cryptographic Hash Function Recommendations for XMPP)
* Version 1.1.0 of XEP-0368 (SRV records for XMPP over TLS)
* Version 0.3.0 of XEP-0380 (Explicit Message Encryption)
* Version 1.4.0 of XEP-0184 (Message Delivery Receipts)

### Friendly specs

This one may be of interest to this community; it's in Last Call at the IETF currently: https://datatracker.ietf.org/doc/draft-ietf-tls-sni-encryption/

## This is it

This edition was long, we hope you loved it.

You can also show your support by relaying it online, on your blogs, newsletters, or social media.
